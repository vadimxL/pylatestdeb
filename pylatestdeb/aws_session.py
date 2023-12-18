from diskcache import Cache
import boto3
from oathtool import generate_otp

EXPIRE_TIME = 129600  # 36 hours


def _get_aws_credentials(mfa_serial_number, mfa_totp, sts_client):
    """
    Gets a session token with MFA credentials and uses the temporary session
    credentials to list Amazon S3 buckets.

    Requires an MFA device serial number and token.

    :param mfa_serial_number: The serial number of the MFA device. For a virtual MFA
                              device, this is an Amazon Resource Name (ARN).
    :param mfa_totp: A time-based, one-time password issued by the MFA device.
    :param sts_client: A Boto3 STS instance that has permission to assume the role.
    """
    if len(mfa_serial_number) < 6:
        print("Serial number must be at least 6 characters long.")
        exit(1)
    else:
        response = sts_client.get_session_token(
            SerialNumber=mfa_serial_number, TokenCode=mfa_totp, DurationSeconds=EXPIRE_TIME  # 36 hours
        )

    return response


def get_aws_credentials(mfa_serial_number, mfa_secret_key, aws_access_key_id, aws_secret_access_key):
    # check if cached json/aws_credentials.json exists
    # if not, get new credentials
    with Cache('aws') as aws_credentials_cache:
        aws_credentials = aws_credentials_cache.get('aws_credentials')
        if not aws_credentials:
            mfa_code = generate_otp(mfa_secret_key)
            boto3.client('sts', aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key)
            aws_credentials = _get_aws_credentials(mfa_serial_number, mfa_code, boto3.client('sts'))
            aws_credentials_cache.set('aws_credentials', aws_credentials, expire=EXPIRE_TIME)
        return aws_credentials


if __name__ == '__main__':
    print(get_aws_credentials(mfa_serial_number="", mfa_secret_key=""))

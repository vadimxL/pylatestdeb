from diskcache import Cache
import boto3
from oathtool import generate_otp

EXPIRE_TIME = 129600  # 36 hours
MFA_SN = "arn:aws:iam::871066970550:mfa/work"
MFA_SECRET_KEY = "BIHQU5L5GMWPT6TKEQSPQT7GKDB2EQBWQXMG4BAY56XZBPFIK3E2FXNN6KC5GD6B"


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


def get_aws_credentials(mfa_serial_number=MFA_SN, mfa_secret_key=MFA_SECRET_KEY):
    # check if cached json/aws_credentials.json exists
    # if not, get new credentials
    with Cache('aws') as aws_credentials_cache:
        aws_credentials = aws_credentials_cache.get('aws_credentials')
        if not aws_credentials:
            mfa_code = generate_otp(mfa_secret_key)
            aws_credentials = _get_aws_credentials(mfa_serial_number, mfa_code, boto3.client('sts'))
            aws_credentials_cache.set('aws_credentials', aws_credentials, expire=EXPIRE_TIME)
        return aws_credentials


if __name__ == '__main__':
    print(get_aws_credentials())

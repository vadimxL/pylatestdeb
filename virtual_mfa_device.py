import boto3

from aws_session import get_aws_credentials


def create_virtual_mfa():
    credentials = get_aws_credentials()
    session = boto3.session.Session(aws_access_key_id=credentials["Credentials"]["AccessKeyId"],
                      aws_secret_access_key=credentials["Credentials"]["SecretAccessKey"],
                      aws_session_token=credentials["Credentials"]["SessionToken"])
    iam_client = session.client('iam')

    response = iam_client.create_virtual_mfa_device(
        Path='/service-user/',
        VirtualMFADeviceName='kjh-SuperDuperUser'
    )

    string_seed = response['VirtualMFADevice']['Base32StringSeed']

    qrbytes = response['VirtualMFADevice']['QRCodePNG']
    with open('kjh-SuperDuperUser.png', mode='wb') as f:
        f.write(qrbytes)
        f.close()


if __name__ == '__main__':
    create_virtual_mfa()

from aws_session import get_aws_credentials
from download_latest import download_file


def main():
    mfa_sn = input("Enter MFA serial number and press Enter to continue...")
    mfa_secrety_key = input("Enter MFA secret key and press Enter to continue...")
    download_file(get_aws_credentials(mfa_serial_number=mfa_sn, mfa_secret_key=mfa_secrety_key), check_if_exists=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

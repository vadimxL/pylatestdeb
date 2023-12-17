from aws_session import get_aws_credentials
from download_latest import download_file
from configparser import ConfigParser


def main():
    config = ConfigParser()
    conf_list = config.read('config.ini')

    if len(conf_list) == 0:
        print("Config file not found.")
        mfa_sn = input("Enter MFA serial number: ")
        mfa_secret_key = input("Enter MFA secret key: ")
        config['credentials'] = {'mfa_serial_number': mfa_sn,
                                 'mfa_secret_key': mfa_secret_key}
    else:
        mfa_sn = config.get('credentials', 'mfa_serial_number')
        mfa_secret_key = config.get('credentials', 'aws_access_key_id')

    print(mfa_sn)
    print(mfa_secret_key)

    download_file(get_aws_credentials(mfa_serial_number=mfa_sn, mfa_secret_key=mfa_secret_key), check_if_exists=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

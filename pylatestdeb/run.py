from configparser import ConfigParser
from pylatestdeb.aws_session import get_aws_credentials
from pylatestdeb.download_latest import download_file


def main():
    config = ConfigParser()
    conf_list = config.read('config.ini')

    if len(conf_list) == 0:
        print("Config file not found.")
        mfa_sn = input("Enter MFA serial number: ")
        mfa_secret_key = input("Enter MFA secret key: ")
        config['credentials'] = {'mfa_serial_number': mfa_sn,
                                 'mfa_secret_key': mfa_secret_key}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    else:
        mfa_sn = config.get('credentials', 'mfa_serial_number')
        mfa_secret_key = config.get('credentials', 'mfa_secret_key')

        if not mfa_sn or not mfa_secret_key:
            print("MFA credentials not found in config file.")
            exit(1)

    download_file(get_aws_credentials(mfa_serial_number=mfa_sn, mfa_secret_key=mfa_secret_key), check_if_exists=False,
                  type_='unprotected', prefix='development/')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

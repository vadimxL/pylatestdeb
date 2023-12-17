from aws_session import get_aws_credentials

from download_latest import download_file


def main():
    download_file(get_aws_credentials(), check_if_exists=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

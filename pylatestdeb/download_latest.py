import os
from tqdm import tqdm
import boto3
from boto3.s3.transfer import TransferConfig


def download_file(credentials, check_if_exists=True, type_='unprotected', prefix='releases/'):
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3', aws_access_key_id=credentials["Credentials"]["AccessKeyId"],
                      aws_secret_access_key=credentials["Credentials"]["SecretAccessKey"],
                      aws_session_token=credentials["Credentials"]["SessionToken"])

    # Retrieve the list of objects in the 'releases/' prefix
    response = s3.list_objects_v2(Bucket='convexum-debs', Prefix=prefix)

    # Initialize variables to store information about the latest file
    latest_file = None
    latest_time = None

    for obj in response.get('Contents', []):
        # Filter for files with type in their key and get the latest one
        if type_ in obj['Key']:
            if latest_time is None or obj['LastModified'] > latest_time:
                latest_file = obj
                latest_time = obj['LastModified']

    print(f'Latest file: {latest_file.get("Key")} ({latest_time})')
    print()

    total_length = int(latest_file.get('Size', 0))
    downloaded = 0

    # Download the latest unprotected file
    if latest_file:
        file_key = latest_file.get('Key')
        if file_key:
            file_name = file_key.split('/')[-1]
            tokens = file_name.split('.')
            name = "".join(tokens[:-2])  # Extract filename from the key
            suffix = "." + ".".join(tokens[-2:])

            directory = 'downloads/'

            # Creating the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)

            file_name = directory + name + latest_time.strftime("-%m-%d-%Y") + suffix
            # the filename
            config = TransferConfig(max_concurrency=5)
            if check_if_exists and os.path.isfile(file_name):
                print(f"File already exists: {file_name}")
                return
            with tqdm(total=total_length, unit='B', unit_scale=True, desc='Downloading') as pbar:
                def progress_callback(chunk):
                    nonlocal downloaded
                    downloaded += chunk
                    pbar.update(downloaded - pbar.n)

                with open(file_name, 'wb') as f:
                    s3.download_fileobj('convexum-debs', file_key, f, Config=config, Callback=progress_callback)
                    print()
                    print(f"Downloaded latest unprotected file: {file_name}")
        else:
            print("Unable to get file key for the latest file.")
    else:
        print("No unprotected files found.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    aws_credentials = boto3.client('sts').get_session_token()
    download_file(credentials=aws_credentials)


import os
from tqdm import tqdm
import pysftp


def find_latest_tar_gz_file_in_current_folder():
    current_folder = os.getcwd()
    latest_file = None
    latest_time = None

    for file in os.listdir(current_folder):
        if file.endswith('.tar.gz'):
            file_path = os.path.join(current_folder, file)
            file_time = os.path.getmtime(file_path)
            if latest_time is None or file_time > latest_time:
                latest_file = file_path
                latest_time = file_time

    return latest_file


def sftp_put_with_progress(local_path, remote_path, hostname, username, password):
    with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
        with tqdm(total=os.path.getsize(local_path), unit='B', unit_scale=True, desc='Uploading') as pbar:
            def progress_callback(transferred, total):
                pbar.update(transferred - pbar.n)

            sftp.put(local_path, remote_path, callback=progress_callback)


def transfer_file_paramiko():
    file_name = find_latest_tar_gz_file_in_current_folder()
    print(file_name)

    sftp_put_with_progress(file_name,
                           f"/home/convexum/{file_name.split('/')[-1]}",
                           "192.168.0.100", "convexum", "cvx2017")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transfer_file_paramiko()

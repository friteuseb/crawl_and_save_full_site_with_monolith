import os
import ftplib
from urllib.parse import urlparse

def upload_to_ftp(ftp_host, ftp_user, ftp_pass, local_dir, remote_dir):
    ftp = ftplib.FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_pass)
    ftp.cwd(remote_dir)

    for root, dirs, files in os.walk(local_dir):
        for dirname in dirs:
            try:
                ftp.mkd(os.path.join(remote_dir, dirname))
            except ftplib.error_perm as e:
                print(f"Directory {dirname} already exists")

        for filename in files:
            local_filepath = os.path.join(root, filename)
            remote_filepath = os.path.join(remote_dir, os.path.relpath(local_filepath, local_dir))
            with open(local_filepath, 'rb') as file:
                ftp.storbinary(f'STOR {remote_filepath}', file)

    ftp.quit()

if __name__ == "__main__":
    ftp_host = input("Enter FTP host: ").strip()
    ftp_user = input("Enter FTP username: ").strip()
    ftp_pass = input("Enter FTP password: ").strip()
    local_dir = input("Enter local directory to upload: ").strip()
    remote_dir = input("Enter remote directory to upload to: ").strip()

    upload_to_ftp(ftp_host, ftp_user, ftp_pass, local_dir, remote_dir)

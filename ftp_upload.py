import os
import ftplib
from urllib.parse import urlparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def upload_to_ftp(ftp_host, ftp_user, ftp_pass, local_dir, remote_dir):
    ftp = ftplib.FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_pass)
    ftp.cwd(remote_dir)
    logging.info(f"Connected to FTP server {ftp_host}")

    override_all = False
    skip_all = False

    for root, dirs, files in os.walk(local_dir):
        for dirname in dirs:
            remote_path = os.path.join(remote_dir, os.path.relpath(os.path.join(root, dirname), local_dir))
            try:
                ftp.mkd(remote_path)
                logging.info(f"Created directory {remote_path}")
            except ftplib.error_perm:
                logging.warning(f"Directory {remote_path} already exists")

        for filename in files:
            local_filepath = os.path.join(root, filename)
            remote_filepath = os.path.join(remote_dir, os.path.relpath(local_filepath, local_dir))

            if not override_all and not skip_all:
                try:
                    ftp.size(remote_filepath)
                    while True:
                        action = input(f"File {remote_filepath} already exists. [O]verwrite, [S]kip, [R]ename, [A]ll Overwrite, [K] All Skip? ").strip().lower()
                        if action == 'o':
                            break
                        elif action == 's':
                            logging.info(f"Skipped uploading {local_filepath}")
                            continue
                        elif action == 'r':
                            base, ext = os.path.splitext(remote_filepath)
                            counter = 1
                            new_remote_filepath = f"{base}_{counter}{ext}"
                            while True:
                                try:
                                    ftp.size(new_remote_filepath)
                                    counter += 1
                                    new_remote_filepath = f"{base}_{counter}{ext}"
                                except ftplib.error_perm:
                                    remote_filepath = new_remote_filepath
                                    break
                            break
                        elif action == 'a':
                            override_all = True
                            break
                        elif action == 'k':
                            skip_all = True
                            logging.info(f"Skipped uploading {local_filepath}")
                            continue
                except ftplib.error_perm:
                    pass

            if not skip_all:
                logging.info(f"Uploading {local_filepath} to {remote_filepath}")
                with open(local_filepath, 'rb') as file:
                    ftp.storbinary(f'STOR {remote_filepath}', file)

    ftp.quit()
    logging.info("FTP upload complete")

if __name__ == "__main__":
    ftp_host = input("Enter FTP host: ").strip()
    ftp_user = input("Enter FTP username: ").strip()
    ftp_pass = input("Enter FTP password: ").strip()
    local_dir = input("Enter local directory to upload: ").strip()
    remote_dir = input("Enter remote directory to upload to: ").strip()

    upload_to_ftp(ftp_host, ftp_user, ftp_pass, local_dir, remote_dir)

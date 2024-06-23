# Crawl and Save Full Site with Monolith

This Python script allows you to crawl a website, save its pages using Monolith, and adjust the links for local navigation. It is especially useful for backing up sites hosted on platforms like Squarespace, which can be challenging for traditional website scrapers.

## Prerequisites

- Python 3.x
- Monolith installed (`sudo snap install monolith`)

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/friteuseb/crawl_and_save_full_site_with_monolith.git
    cd crawl_and_save_full_site_with_monolith
    ```

2. Run the script to crawl and save the site:
    ```bash
    python download_and_adjust.py
    ```

3. Enter the URL of the site you want to crawl and the maximum number of pages to crawl (0 for no limit).

4. Run the script to upload the saved site via FTP:
    ```bash
    python ftp_upload.py
    ```

5. Enter the FTP host, username, password, local directory to upload, and remote directory to upload to.

## How It Works

- The script uses Monolith to save each page of the site.
- It adjusts the links to point to the saved HTML files for local navigation.
- The `<base>` tag is removed if present to ensure local links work correctly.
- This method is effective for sites hosted on platforms like Squarespace, where traditional site scrapers may fail.

## Example

When prompted, enter the URL of the site you want to crawl (e.g., `https://www.example-website.com`) and the number of pages to crawl (e.g., `0` for no limit).

## Putting the Backup Online

To put the backup of your site online, you can use a static site hosting service like GitHub Pages, Netlify, or any other web hosting service that supports static sites.

### Using GitHub Pages

1. Create a new repository on GitHub.
2. Push your backed-up site to this repository.
3. Go to the repository settings and enable GitHub Pages by selecting the `main` branch as the source.
4. Your site will be available at `https://<your-username>.github.io/<your-repository-name>/`.

### Using Netlify

1. Sign up for a Netlify account.
2. Drag and drop your backed-up site folder onto the Netlify dashboard.
3. Follow the prompts to deploy your site.
4. Your site will be available at a Netlify subdomain, or you can configure a custom domain.

### Using FTP

1. Run the `ftp_upload.py` script included in this repository.
2. Enter the FTP host, username, password, local directory to upload, and remote directory to upload to.
3. The script will upload your backed-up site to the specified FTP server.

## Notes

- Ensure Monolith is installed and accessible from your PATH.
- The script creates a directory based on the URL of the site to store the downloaded pages.

## Author

Cyril Wolfangel

## License

This project is licensed under the MIT License.

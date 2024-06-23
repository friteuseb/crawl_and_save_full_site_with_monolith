# Crawl and Save Full Site with Monolith

This Python script allows you to crawl a website, save its pages using Monolith, and adjust the links for local navigation.

## Prerequisites

- Python 3.x
- Monolith installed (`sudo snap install monolith`)

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/friteuseb/crawl_and_save_full_site_with_monolith.git
    cd crawl_and_save_full_site_with_monolith
    ```

2. Run the script:
    ```bash
    python download_and_adjust.py
    ```

3. Enter the URL of the site you want to crawl and the maximum number of pages to crawl (0 for no limit).

## How It Works

- The script uses Monolith to save each page of the site.
- It adjusts the links to point to the saved HTML files for local navigation.
- The `<base>` tag is removed if present to ensure local links work correctly.

## Example

When prompted, enter the URL of the site you want to crawl (e.g., `https://www.example-website.fr`) and the number of pages to crawl (e.g., `0` for no limit).

## Notes

- Ensure Monolith is installed and accessible from your PATH.
- The script creates a directory based on the URL of the site to store the downloaded pages.

## Author

Cyril Wolfangel

## License

This project is licensed under the MIT License.

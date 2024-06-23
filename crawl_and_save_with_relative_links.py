import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def save_page(url, output_dir):
    filename = urlparse(url).path.replace('/', '_') + '.html'
    os.system(f"monolith {url} -o {os.path.join(output_dir, filename)}")

def adjust_links_in_file(filepath, base_url):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Remove <base> tag if present
        base_tag = soup.find('base')
        if base_tag:
            base_tag.decompose()

        for tag in soup.find_all(['a', 'img', 'link', 'script']):
            attr = 'href' if tag.name in ['a', 'link'] else 'src'
            if tag.has_attr(attr):
                original_url = tag[attr]
                if original_url.startswith(base_url):
                    parsed_url = urlparse(original_url)
                    if parsed_url.path and parsed_url.path.strip('/'):
                        # Create path without directory, just the file name
                        file_name = parsed_url.path.replace('/', '_') + '.html'
                        tag[attr] = file_name

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"Adjusted links in {filepath}")
    except Exception as e:
        print(f"Failed to adjust links in {filepath}: {e}")

def crawl(url, base_url, output_dir, max_pages):
    if max_pages > 0 and len(visited) >= max_pages:
        return
    if url in visited:
        return
    visited.add(url)
    print(f"Crawling: {url}")
    save_page(url, output_dir)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all('a', href=True):
            next_url = urljoin(base_url, link['href'])
            if base_url in next_url and next_url not in visited:
                crawl(next_url, base_url, output_dir, max_pages)
    except Exception as e:
        print(f"Failed to crawl {url}: {e}")

def adjust_all_links(output_dir, base_url):
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                adjust_links_in_file(filepath, base_url)

if __name__ == "__main__":
    base_url = input("Enter the URL of your site: ").strip()
    max_pages = int(input("Enter the maximum number of pages to crawl (0 for no limit): ").strip())
    
    # Create output directory based on base URL
    url_parts = urlparse(base_url)
    base_dir_name = url_parts.netloc.replace('.', '_')
    output_dir = os.path.join(os.getcwd(), base_dir_name)
    os.makedirs(output_dir, exist_ok=True)
    
    visited = set()
    crawl(base_url, base_url, output_dir, max_pages)
    adjust_all_links(output_dir, base_url)

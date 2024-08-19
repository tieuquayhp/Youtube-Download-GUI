import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def download_chapter(chapter_url, folder_name):
    """Tải nội dung một chương truyện và lưu vào file."""
    response = requests.get(chapter_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    chapter_title = soup.find('h1', class_='chapter-title').text.strip()
    chapter_content = soup.find('div', class_='chapter-c').text.strip()

    file_name = f"{folder_name}/{chapter_title}.txt"
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(chapter_content)

def download_story(story_url):
    """Tải toàn bộ truyện."""
    response = requests.get(story_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    story_title = soup.find('h1', class_='story-title').text.strip()
    folder_name = story_title.replace(' ', '_')  # Tạo thư mục lưu truyện
    os.makedirs(folder_name, exist_ok=True)

    chapter_links = soup.find_all('a', class_='chapter-name')
    total_chapters = len(chapter_links)

    with tqdm(total=total_chapters, desc="Downloading", unit="chapter") as pbar:
        for chapter_link in chapter_links:
            chapter_url = chapter_link['href']
            download_chapter(chapter_url, folder_name)
            pbar.update(1)

if __name__ == "__main__":
    story_url = input("Nhập URL truyện trên truyenfull.vn: ")
    download_story(story_url)

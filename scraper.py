import requests
from bs4 import BeautifulSoup

def scrape_article_content(url):
    try:
        # Send a GET request to fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from <p> tags
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])

        # Return the extracted content
        return content if content.strip() else "No content found"
    except Exception as e:
        print(f"Error while scraping: {e}")
        return None

# Test the function
url = "https://www.bbc.com/news/articles/czxk05lz4d0o"  
article_content = scrape_article_content(url)
print(article_content)

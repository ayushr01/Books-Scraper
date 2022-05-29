import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    # With the 8s it will make sure all the level names have same width
    # s at the end is to tell python they are strings
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('scraping')  # The name of our logger is scraping

logger.info('Loading books list...')

print('Loading books list...')
page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)  # Adds the new list to the end of the new list

import re
import logging

from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
from locators.page_count import PageCountLocator
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_books_page')
# Child of the logger we defined

class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing the page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`.')
        return [BookParser(book) for book in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self): 
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(PageCountLocator.COUNT).string
        logger.info(f'Found number of catalogue pages available: `{content}`.')
        expression = 'Page [0-9]+ of ([0-9]+)'
        page_count = re.search(expression, content)
        pages = int(page_count.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`.`')
        return pages
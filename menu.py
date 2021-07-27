import logging

from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''

book_generator = (book for book in books)


def print_best_books():
    logger.info('Finding best book by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    # Takes books and it sorts by using the function rating, This is also going to give only top 10
    # We multiply by -1 to reverse the order
    # If we did lambda x: (x.rating * -1, x.price)
    # it would first sort by rating and then it would sort each rating by price
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(book_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print("Please enter a valid option!")
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')


menu()

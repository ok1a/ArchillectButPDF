import fitz
import os
import random
import asyncio
from twbot import poststatus
from colorama import init as init_colorama, Fore, Back, Style


init_colorama(autoreset=True)

inputFormat = ".pdf"
outputFormat = ".png"
path = './books'


session_counter = 0

bookPaths = []

bookFiles = os.listdir(path)

for book in bookFiles:
    if (book[-4:] == inputFormat):
        full_path = os.path.join(path, book)
        bookPaths.append(full_path)


bookCount = len(bookPaths) - 1

# pyramid.pdf. obituary for frater recnartus
# corrupt: q.pdf
# Book selected: ./books/case,whitty - 32 paths of w.pdf Book selected: ./books/The Equinox Vol 5 No 4 - Sex and Religion.pdf


async def media_loop():

    running = True

    while running:

        originalBookAndPage = False
        while not originalBookAndPage:

            validBookAndPageOpened = False
            while not validBookAndPageOpened:

                validBookFound = False
                while not validBookFound:
                    randomBook = random.randint(0, bookCount)

                    bookToPrint = bookPaths[randomBook]
                    print(f"Book selected: {bookToPrint}")

                    try:
                        book = fitz.open(bookToPrint)
                        totalPages = book.pageCount
                        print(f"Book loaded. Page count: {totalPages}")
                        validBookFound = True
                    except RuntimeError as e:
                        print(f"Error with book somewhere. {e}")

                # books that don't have valid table of contents page selection process
                randomLow = int(totalPages * 0.04)

                # randomPageNumber = random.randint(randomLow, totalPages - 8)
                randomPageNumber = random.randint(
                    randomLow, totalPages - randomLow)

                if randomPageNumber == 0:
                    randomPageNumber = 1

                pageNumber = randomPageNumber
                try:
                    page = book.loadPage(pageNumber)
                    print(f"Page loaded: {pageNumber}")
                    validBookAndPageOpened = True
                except RuntimeError as e:
                    print(f"Error loading page: {pageNumber}. {e}")

            try:
                zoom = 2
                matrix = fitz.Matrix(zoom, zoom)
                picOfPage = page.getPixmap(matrix=matrix)
                output = f"{bookToPrint}-{pageNumber}.png"

                if os.path.isfile(output):
                    print(
                        f"{Fore.RED}\nCOLLISION:\nPage {pageNumber} of {bookToPrint}\n")
                else:
                    originalBookAndPage = True
            except:
                print(f"{Fore.RED}: Error in checking for collision")

        picOfPage.writePNG(output)
        status = poststatus(output)
        if status:
            print(
                f"{Fore.GREEN}\nSUCCESS\nUploaded: {output}\n")
            # print(status.created_at)
        else:
            print(f"{Fore.RED}\nFailure updating status\n")

        print(f"{Fore.BLUE} VALID EVERYTHING")

        minutes = .01

        time = minutes * 60
        print(f"{Fore.YELLOW}{Style.BRIGHT}Sleep for {minutes}m")

        await asyncio.sleep(time)


asyncio.run(media_loop())

import fitz
import os
import random
import asyncio
from twbot import poststatus
from colorama import init as init_colorama, Fore, Back, Style
from PIL import Image

init_colorama(autoreset=True)

inputFormat = ".pdf"
outputFormat = ".png"
path = './books'


bookPaths = []

bookFiles = os.listdir(path)

for book in bookFiles:
    if (book[-4:] == inputFormat):
        full_path = os.path.join(path, book)
        bookPaths.append(full_path)


bookCount = len(bookPaths) - 1


async def media_loop():

    running = True

    while running:
        randomBook = random.randint(0, bookCount)

        bookToPrint = bookPaths[randomBook]

        book = fitz.open(bookToPrint)
        totalPages = book.pageCount

        # books that don't have valid table of contents page selection process
        randomPageNumber = random.randint(15, totalPages-8)

        # doc = book.getToC()
        pageNumber = randomPageNumber
        page = book.loadPage(pageNumber)

        # page resolution stuffs
        zoom = 2
        matrix = fitz.Matrix(zoom, zoom)
        # picOfPage = page.getPixmap()
        picOfPage = page.getPixmap(matrix=matrix)
        # page end
        output = f"{bookToPrint}-{pageNumber}.png"

        if os.path.isfile(output):
            print(f"{Fore.RED}\nCOLLISION:\nPage {pageNumber} of {bookToPrint}\n")
        else:

            picOfPage.writePNG(output)

            status = poststatus(output)
            if status:
                print(
                    f"{Fore.GREEN}\nSUCCESS\nUploaded: {output}\n")
                # print(status.created_at)
            else:
                print(f"{Fore.RED}\nFailure updating status\n")

        minutes = 0.1

        time = minutes * 60
        print(f"{Fore.YELLOW}{Style.BRIGHT}Sleep for {minutes}m")

        await asyncio.sleep(time)

asyncio.run(media_loop())

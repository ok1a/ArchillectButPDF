import fitz
import os
import random
import asyncio
from twbot import poststatus, poststatus2
from PIL import Image

inputFormat = ".pdf"
outputFormat = ".png"
path = './books'

# for book in os.listdir('./books'):
#     print(book)

bookPaths = []

bookFiles = os.listdir(path)

for book in bookFiles:
    if (book[-4:] == inputFormat):
        full_path = os.path.join(path, book)
        bookPaths.append(full_path)


# print(bookPaths)

bookCount = len(bookPaths) - 1

# randomBook = random.randint((0, len(bookPaths)))


async def runitup():

    running = True

    while running:
        randomBook = random.randint(0, bookCount)

        # bookToPrint = bookPaths[1]
        bookToPrint = bookPaths[randomBook]

        book = fitz.open(bookToPrint)
        totalPages = book.pageCount

        # print(totalPages)

        # books that don't have valid table of contents page selection process
        randomPageNumber = random.randint(15, totalPages-8)
        print(f"RANDOM: {randomPageNumber}")
        # end

        # doc = book.getToC()
        # pageNumber = 33
        pageNumber = randomPageNumber
        page = book.loadPage(pageNumber)

        # page resolution stuffs
        zoom = 2
        matrix = fitz.Matrix(zoom, zoom)
        # picOfPage = page.getPixmap()
        picOfPage = page.getPixmap(matrix=matrix)
        # page end
        output = f"{bookToPrint}-{pageNumber}.png"
        # print(doc)

        if os.path.isfile(output):
            print("File already exists!")
            print(f"Not printing: {output}")
        else:
            print("Did not exist before. New upload!")
            print(f"Uploading: {output}")
            # Works vv
            picOfPage.writePNG(output)
            # poststatus(str(pageNumber), output)
            # Works ^^
            # pictura = picOfPage.writePNG(output)
            # writtenfile = Image.open(output)
            # print(writtenfile)

            status = poststatus2(output)
            if status:
                print(status.created_at)
            else:
                print("Failure somewhere")

            # poststatus2(pictura)
            # poststatus2(picOfPage.writePNG(output))
            # poststatus(output)
            # poststatus(picOfPage.writePNG(output)
            #            )
            # poststatus(pageNumber, picOfPage.writePNG(output))

        minutes = 2

        time = minutes * 60
        print(f"Sleep for {minutes} minutes")

        await asyncio.sleep(time)

asyncio.run(runitup())

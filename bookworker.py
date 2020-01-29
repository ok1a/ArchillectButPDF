import os
import random
import asyncio
import pickle
from mediaworker import poststatus
from colorama import init as init_colorama, Fore, Back, Style
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
import pdf2image
init_colorama(autoreset=True)

inputFormat = ".pdf"
outputFormat = ".png"
path = './books'


session_counter = 0

bookPaths = []

bookFiles = os.listdir(path)


with open('lib_history.pickle', 'rb') as handle:
    book_history = pickle.load(handle)

# print(book_history)


def book_in_history(book, page):
    if book in book_history:
        # print("Book is in history")
        if page in book_history[book]:
            print("Page is in history. Collision.")
            return False
        else:
            book_history[book][page] = 1
    else:
        # print("Book not in history yet.")
        book_history[book] = {}
        # print("Book now in history")
        book_history[book][page] = 1
        # print("Page is now in book")

    with open('lib_history.pickle', 'wb') as handle:
        pickle.dump(book_history, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return True


for book in bookFiles:
    if (book[-4:] == inputFormat):
        full_path = os.path.join(path, book)
        bookPaths.append(full_path)


bookCount = len(bookPaths) - 1


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
                        book = PdfFileReader(bookToPrint)           #this is the new change
                        totalPages = book.getNumPages()             #this is also a new change
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
                    page = book.getPage(pageNumber)
                    print(f"Page loaded: {pageNumber}")
                    validBookAndPageOpened = True
                except RuntimeError as e:
                    print(f"Error loading page: {pageNumber}. {e}")

#            try:
            writer = PdfFileWriter() #added these two
            writer.addPage(page) #added this one too
            zoom = 2
            #matrix = writer.zoom(zoom)            #new change here thank me later
            with open('outfile.pdf', 'wb') as outfile: #had to add this
                writer.write(outfile)

            picOfPage = pdf2image.convert_from_path('./outfile.pdf') #i changed this too
            output = f"{bookToPrint}-{pageNumber}.png"

            if not book_in_history(bookToPrint, pageNumber):
                print(
                    f"{Fore.RED}\nCOLLISION:\nPage {pageNumber} of {bookToPrint}\n")
                # if os.path.isfile(output):
                #     print(
                #         f"{Fore.RED}\nCOLLISION:\nPage {pageNumber} of {bookToPrint}\n")
            else:
                originalBookAndPage = True
            #except:
                #print(f"{Fore.RED}: Error in checking for collision")

        picOfPage[0].save(output) ##had to add this
        status = poststatus(output)
        if status:
            print(
                f"{Fore.GREEN}\nSUCCESS\nUploaded: {output}\n")

            try:
                os.remove(output)
                print("File removed succesfully")
            except OSError as e:
                print(f"Error removing file: {e}")
            # print(status.created_at)
        else:
            print(f"{Fore.RED}\nFailure updating status\n")

        print(f"{Fore.BLUE} VALID EVERYTHING")

        minutes = 15

        time = minutes * 60
        print(f"{Fore.YELLOW}{Style.BRIGHT}Sleep for {minutes}m")

        await asyncio.sleep(time)


asyncio.run(media_loop())

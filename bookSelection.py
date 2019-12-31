import fitz
import os
import random

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


print(bookPaths)

bookToPrint = bookPaths[1]

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
picOfPage = page.getPixmap()
output = f"{bookToPrint}-{pageNumber}.png"
# print(doc)

if os.path.isfile(output):
    print("File already exists!")
else:
    print("Did not exist before. New upload!")
    picOfPage.writePNG(output)

import fitz
import os

path = './books'

# for book in os.listdir('./books'):
#     print(book)

bookPaths = []

bookFiles = os.listdir(path)

for book in bookFiles:
    full_path = os.path.join(path, book)
    # print(book)
    # print(full_path)
    bookPaths.append(full_path)


print(bookPaths)

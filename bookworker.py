import json
import pickle


class BookWorker:
    def __init__(self):
        pass


# library = {
#     "book1" = {
#         # pages : times uploaded
#         10: 1,
#         2: 1,
#         1: 1
#     },
#     "book2" = {
#         25: 1,
#         3: 20,
#         1: 1
#     }
# }

library = {
    "book1": {
        217: 1,
        10: 2,
        3: 1,
        128: 1,
        384: 2
    },
    "book2": {
        182: 2,
        2: 1,
        38: 2,
        22: 1,
        387: 2,
        92: 2,
        48: 1
    }
}

# with open('ex_pick.pickle', 'wb') as handle:
#     pickle.dump(library, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('ex_pick.pickle', 'rb') as handle:
    b = pickle.load(handle)

print(b)
print(library == b)

book = 'book3'
page = '2'
# if b.has_key(book):
#     print("Book is here")
#     print(b[book])

# else:
#     print("No book")
#     # print(b[book])

if book in b:
    print("Key here")
    if page in b[book]:
        print("Page here. Collide")
    else:
        b[book][page] = 1
else:
    print("Key not here")
    b[book] = {}
    print("Now it is")
    b[book][page] = 1
    print("page too")

print(b)


with open('ex_pick.pickle', 'wb') as handle:
    pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Saved")

# print(b.keys())

# print(b.has_key('book1'))
library2 = {
    "book8484": {
        217: 1,
        10: 2,
        3: 1,
        128: 1,
        384: 2
    },
    "book2": {
        182: 2,
        2: 1,
        38: 2,
        22: 1,
        387: 2,
        92: 2,
        48: 1
    }
}

# library3 = {library2}
# print(library3)

# with open("ex_play.json", "w") as write_file:
#     json.dump(library3, write_file)

# json_string = json.dumps(library2)
# print(json_string)

# with open("lib_store_ex.json", "r") as read_file:
#     data = json.load(read_file)

# # print(data)

# libraryHT = data['library']

# # print(data['library'])
# # print(libraryHT)

# randBook = 'example-book-44'
# randNum = '4'

# # if (libraryHT[randBook]):
# #     print("Yes")
# #     # print(libraryHT[randBook])
# #     # if libraryHT[randBook][str(randNum)]:
# #     if not libraryHT[randBook][randNum]:
# #         print("nope. not posted.")
# #     else:
# #         print("Already posted once")
# # else:
# #     libraryHT[randBook] = {
# #         randNum: 1
# #     }

# # print(libraryHT)
# if not (data['library'][randBook]):
#     print("no")
#     # print(libraryHT[randBook])
#     # if libraryHT[randBook][str(randNum)]:
#     if not (data['library'][randBook][randNum]):
#         print("Already posted once")
#     else:
#         print("nope. not posted.")
# else:
#     data['library'][randBook] = {
#         randNum: 1
#     }

# print(data['library'])

# print(library)
# print(library["book1"])
# # print(library['book3'])
# library['book3'] = {}
# print(library['book3'])
# # print(library['book3'][393])
# library['book3'][393] = 1
# library['book3'][393] = library['book3'][393] + 1
# print(library['book3'][393])

# Doing a nested hash table will also allow me to store upload counts which I can use to implement a recycling content policy based on a config.json or something. "max_times_allowed_dupe_content". same pic, twice max. no more.

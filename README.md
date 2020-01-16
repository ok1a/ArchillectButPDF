# ArchillectButPDF

ArchillectButPDF is a bot built in Python3 that will scan a directory of PDFs and upload a randomly selected page from a randomly selected book to Twitter in image format. Uploads are logged so content may be recycled to a limit, or non-recyclable.

Inspired by, but having nothing to do with, the Twitter bot [@archillect](https://twitter.com/archillect).

View the bot in action: [@Neuroccult](https://twitter.com/Neuroccult).

## Installation

After cloning this repository, install dependencies:

Using the package manager [pip](https://pip.pypa.io/en/stable/),

```bash
pip3 install -r requirements.txt
```

or

```bash
pip install -Ur requirements.txt
```

## Setup

Initialize the project with a .env file containing your [Twitter API credentials](https://apps.twitter.com/app/new):

```env
CONSUMER_KEY=
CONSUMER_SECRET=
ACCESS_TOKEN_KEY=
ACCESS_TOKEN_SECRET=
```

Place PDFs in project directory:
`'./books'`

Configure minutes between every post [default: 5] by modifying line 135 of `'./bookworker.py'`:

```python
minutes = 5 #Integer
```

Run the bot by:

```bash
python3 bookworker.py
```

and kick back and relax. Success messages and potential collisions or errors will be outputted to console.

## Logging

Book history is stored in a [pickled](https://docs.python.org/3/library/pickle.html) nested hash table, `'./lib_history.pickle'`. Because the bot utilizes pickling, data stored is not human readable.

To view stored data for debugging purposes, you may run the script:

```python
python3 p2j.py
```

which will output a JSON representation of the stored data to `'./lib_history.pickle.json'`.

Example of structured data:

```json
{
  "./books/My first book name example.pdf": {
    "23": 1
  },
  "./books/A really good book name example.pdf": {
    "24": 1,
    "26": 1,
    "32": 1,
    "71": 1,
    "85": 1,
    "117": 1,
    "118": 1,
    "119": 1,
    "125": 1,
    "126": 1,
    "137": 1,
    "138": 1,
    "169": 1,
    "172": 1,
    "179": 1,
    "206": 1,
    "211": 1,
    "223": 1,
    "241": 1,
    "262": 1
  },
  "./books/A final Example.pdf": {
    "1": 1,
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
    "7": 1,
    "8": 1,
    "9": 1,
    "10": 1
  }
}
```

Page numbers and their upload counter are stored in an object representing the book, which is then stored in a library object that holds all books.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

##### I do not own, nor claim to own, either [@Neuroccult](https://twitter.com/Neuroccult) or [@archillect](https://twitter.com/archillect). Furthermore, I not am not responsible for and do not claim any media that this bot may be used to upload.

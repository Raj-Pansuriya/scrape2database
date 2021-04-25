# scrape2database

### A web scraper which uses sqlite database to store the scraped data

## Dependancies

- Python

    Any python 3 derivative

- sqlite

    No need of any explicit installation, comes preinstalled with python as a standard library

- curses

    It is a python library used to create interactive and rich looking Terminal User Interface (TUI).

- sqlite browser (optional)
    
    Sqlite browser is an open-source software to browse and manipukate sqlite databases.
    
    The whole project follows TUI but still if user wants to have a Graphical User Interface (GUI) they can install `sqlite-browser` from their github repo given below
    
    [sqlitebrowser/git](https://github.com/sqlitebrowser/sqlitebrowser)


- Pandas

    We have used pandas for organising and formatting the collected data into dataframes so that it would be easy to convert them into database tables.
    
    Pandas can be installed as 
```
pip install pandas 
```

- BeautifulSoup

    `BeautifulSoup` library is used to scrape data from web and to get well formatted html pages.
    
    It provides us with a rich arsenal of various methods and function by which we can get the required data very easily from any web-page.
    
    Without `BeautifulSoup` we would have to manually format the broken `html` pages from the web and also have to filter the page for the required data.
    
    Though we could do that using regular expressions by importing python standard module `re` but that can sometimes be a really tedious job so we use `BeautifulSoup`
    
    `BeautifulSoup` can be installed as
```
pip install beautifulsoup4
```


- A html parser ( preferably `lxml` )

    Beautiful soup provides us a default html parser but that's not very efficient and can provide unwanted parsed data for some large and complexly written html pages
    
    It can even fail to detect the data if the html page is broken, So I suggest to install another parser named `lxml`
    
    I have used `lxml` parser in the `scraper.ipynb` file which basically scrapes the data and stores it into a sqlite data base, you can just remove the `lxml` parameter given to `beautifulsoup` and leave the place as blank; `beautifulsoup` will use the default parser i.e., `html` parser that comes preinstalled with it

```
for url in urls:
    page = urllib.request.urlopen(url)
    soup = bs(page,"lxml")
```

`lxml` can be installed as

```
pip install lxml
```

## Code structure

There are total 5 python scripts and 1 python notebook.

1. The python notebook by name `scraper.ipynb` contains the code to scrape official python documentation. Once you run all the cells of this notebook you will get a database in your current working directory by name `python_doc.db`

2. `tui.py` is the frontend code for our desktop app. Python `curses` module is used to design our terminal frontend

3. `traverse.py` contains the code to connect our backend with our frontend. It contains functions which returns data corresponding to the parameters they get.

4. There are three files related to admin functionalities namely add an admin,remove an admin and verify a user as admin as `add_admin.py`, `remove_admin.py` and `verify_admin.py` respectively.


## Installation
There is no need of installation for this app, simply clone the repository and you are good to go.

clone the repository
```
git clone https://github.com/Raj-Pansuriya/scrape2database.git
```

change your `pwd` to the  cloned repo.
```
cd scrape2database
```

to run the program, you will first have to run each and every cell of `scraper.ipynb` so that you have a `python_doc.db` ready to be traversed.

once you do that, run `tui.py`.

If you want to enjoy the admin privilege functions there are few credentials already present in the `admin.db` database, out of which, you can use `user=user` and `password=password` to get the admin privilages. Once you get that power, you can add your name and password and then you can login using those credentials.

# Note

The app has some linux specifc and environment specific dependancies so this will mot work on a windows machine...(at least for now)
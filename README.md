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



# Scrapy Tutorial

## Installation

Make sure Python is installed and PyCharm

Open Pycharm

file New Project >> "Name Of Project"

* Make sure venv is selected.
* inherit global packages.

File > Settings > Project Interpreter > Search for "Scrapy" and install package.

* Wait a few minutes for installation successful.

Also install win32 (pywin32)

Open Terminal (Make sure venv is active)

cd venv > cd Scripts > activate

cd ..

cd ..

CD back to the folder BEFORE venv.

Write scrapy startproject [Project Name]

Once installed open up terminal then enter > scrapy startproject {Project Name} wait until "You can start your first spider with:
    cd quotetutorial
    scrapy genspider example example.com"  is shown.

OR right click on spider and New > Python File

##############################################################################################
Make sure you cd into the folder where the scrapy.cfg file lies..

Your running python code needs to go into "spiders"/ The project files need to go in the Spiders folder.

Setting,py = Self Explanatory, Change the settings for srcaping

Items.py = Defining the fields name in this file

Pipelines.py = Ensures where the web scraped data goes to the right place.

Middleware.py = Proxies implementation adding additional data etc.

Settings = Settings for the scraper.  For larger websites:  Set Concurrent Requests to 1. May also want to add a user-agent here.

Scraped Data > Item Containers > Pipieline > SQL DB

Scraped Data > Item Containers > JSON/CSV

scrapy shell "URL"  = is used to see what is possible to be scraped, use the response option.

>> = the shell

Id use the "#" sign
for a class use a "." sign

example:

for a span class use:

response.css('span.[FIELDNAME}::text').get()

for a link using the "a" tag:

response.css('a.product-item-link::attr(href)').get()

for a title tag:
 response.css('a[title=Next]::attr(href)').get()

Nested value in a class (Example, the class of next contains the href for next):

 The "A" tag is situated in the li class called "Next".
response.css('li.next a::attr(href)').get()

A response code of "200" suggests that the scraping action is available.

Make sure to change the USER_AGENT in Settings.py to:

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"

######## MyFirst Quotes Tutorial Python File Coding #########

Running using the terminal, scrapy crawl {Name variable below},Make sure you are in the folder just before "spiders" Right Click > Open in termninal.
Importing Scrapy
Creating a class and inheriting the scrapy.Spider inheritance. Alway use (scrapy.Spider):
Defining a parse file, Self (refer to) = the url,  response = the page source.
Tutorial #9 <https://www.youtube.com/watch?v=FQv-whbCfKs&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=9>

````python
import scrapy

class QuoteSpider(scrapy.Spider):

    #What are we naming the spider.
    #What URL we want to scrape
    #Must always be called name and start_urls

    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    #Must always be called parse, self = the url above?
    def parse(self, response):

        #Defining what we want to extract, go to the source code, find the title tag and extract
        #Yield = Return Keyword. the value, defining what we want to extract.
        title = response.css('title::text').extract()
        yield {'titletext' : title}
````

## Web Scraping using classes in python code

Running using the terminal, scrapy crawl {Name variable below},Make sure you are in the folder just before "spiders" Right Click > Open in termninal.
Importing Scrapy
Creating a class and inheriting the scrapy.Spider inheritance
Defining a parse file, Self (refer to) = the url,  response = the page source.
Tutorial #11 - <https://www.youtube.com/watch?v=cC9aFbViT_c&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=11>

```` python
import scrapy

class QuoteSpider(scrapy.Spider):

    #What are we naming the spider.
    #What URL we want to scrape
    #Must always be called name and start_urls

    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    #Must always be called parse, self = the url above?
    def parse(self, response):

        #Specify the class to go inside. (Everything grouped by this class?)
        all_div_quotes = response.css('div.quote')

        #To group title/author/tag together, use a for loop (For each quote, group.)
        for quotes in all_div_quotes:

        #Specify the classes inside the main class above.

            quote = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            yield {
                'quote' : quote,
                'author' : author,
                'tag' : tag
            }
````

## Amazon Product Scraping

Running using the terminal, scrapy crawl {Name variable below},Make sure you are in the folder just before "spiders" Right Click > Open in termninal.
Importing Scrapy
Creating a class and inheriting the scrapy.Spider inheritance
Defining a parse file, Self (refer to) = the url,  response = the page source.
Last modified 02/07/2021

```` python
import scrapy

class QuoteSpider(scrapy.Spider):

    #What are we naming the spider.
    #What URL we want to scrape
    #Must always be called namae and start_urls

    name = "quotes"
    start_urls = [
        'https://www.amazon.co.uk/s?k=book&ref=nb_sb_noss_1'
    ]

    #Must always be called parse, self = the url above?
    def parse(self, response):

      #Specify the class to go inside. (Everything grouped by this class?)
        information = response.css('.s-border-bottom')

        #To group product together

        #Specify the classes inside the main class above.

            productname = information.css('.a-color-base.a-text-normal::text').extract()
      

            yield {
                'Product Name' : productname,
           
            }

````

## Storing scraped data into Item containers

Open up items.py

define the links in the pre-created class, and import ..items in the main python file.

Define here the models for your scraped items

See documentation in <https://docs.scrapy.org/en/latest/topics/items.html>

```` python
import scrapy

class QuotestutorialItem(scrapy.Item):
    # define the fields for your containters here:
    quote = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()

# Open your main project file

# Running using the terminal, scrapy crawl {Name variable below},Make sure you are in the folder just before "spiders" Right Click > Open in termninal.
# Importing Scrapy
# Creating a class and inheriting the scrapy.Spider inheritance
# Defining a parse file, Self (refer to) = the url,  response = the page source.
# Tutorial #11 - <https://www.youtube.com/watch?v=QksUFT2Cmlo&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=12>
# Last modified 05/07/2021

# Keep the names consistent throughout the project. Items.py, Extract using the same name and define the links.

import scrapy

# importing the items file container

from ..items import QuotestutorialItem

class QuoteSpider(scrapy.Spider):

    #What are we naming the spider.
    #What URL we want to scrape
    #Must always be called name and start_urls

    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    #Must always be called parse, self = the url above?
    def parse(self, response):

        #Storing the container inside a class.
        items = QuotestutorialItem()

        #Specify the class to go inside. (Everything grouped by this class?)
        all_div_quotes = response.css('div.quote')

        #To group title/author/tag together, use a for loop (For each quote, group.)
        for quotes in all_div_quotes:

        #Specify the classes inside the main class above. Store the css against a class name.

            quote = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            #Linking the items to the contianers to the css data above.
            items['quote'] = quote
            items['author'] = author
            items['tag'] = tag

            yield items
````

## Amazon Scrapy using items.py

### items.py

Define here the models for your scraped items

See documentation in <https://docs.scrapy.org/en/latest/topics/items.html>

```` python
import scrapy

class AmazoncrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    productname = scrapy.Field()
    productprice = scrapy.Field()

######################## amazoncrawler.py #############################################################

# Running using the terminal, scrapy crawl {Name variable below},Make sure you are in the folder just before "spiders" Right Click > Open in termninal

# Importing Scrapy

# Creating a class and inheriting the scrapy.Spider inheritance

# Defining a parse file, Self (refer to) = the url,  response = the page source
# Last modified 02/07/2021 #

# scrapy crawl productcrawler

import scrapy
from ..items import AmazoncrawlerItem

class AmazonSpider(scrapy.Spider):
    # What are we naming the spider.
    # What URL we want to scrape
    # Must always be called namae and start_urls

    name = "productcrawler"
    start_urls = [
        'https://www.amazon.co.uk/s?k=monitors&ref=nb_sb_noss_2'
    ]

    # Must always be called parse, self = the url above?
    def parse(self, response):

        items = AmazoncrawlerItem()
        # Specify the class to go inside. (Everything grouped by this class?)
        productgroup = response.css('.s-border-bottom')

        # To group product together

        # Specify the classes inside the main class above.

        for productinfo in productgroup:
            productname = productinfo.css('.a-color-base.a-text-normal::text').extract()
            productprice = productinfo.css('.a-price:nth-child(1) span::text').extract()

            items['productname'] = productname
            items['productprice'] = productprice

            yield items

############ Storing Extracted data in a file ##########

# using the terminal.

scrapy crawl quotes -o items.csv

########### Pipelines #########

# Scraped Data > Item Containers > Pipieline > SQL DB

# Scraped Data > Item Containers > JSON/CSV

#### Part 13 Tutorial ###

#### Settings.py ###

# Uncomment the ITEM_PIPELINES Class

# 300 = Pipeline priority

##### pipelines.py #######

# Define your item pipelines here

#

# Don't forget to add your pipeline to the ITEM_PIPELINES setting

# See: <https://docs.scrapy.org/en/latest/topics/item-pipeline.html>

# useful for handling different item types with a single interface

from itemadapter import ItemAdapter

# Scraped Data > Item Containers > Pipieline > SQL DB

# Scraped Data > Item Containers > JSON/CSV

# Uncomment the ITEM_PIPELINES Class

# 300 = Pipeline priority

class QuotestutorialPipeline:
    def process_item(self, item, spider):
        print("Pipeline:" + item['quote'][0])
        return item

######## SQL Lite 3 Create and Insert a Table #############

# import preinstalled sqlite3
import sqlite3

# connect to database, if the database does not exist create.
conn = sqlite3.connect('myquotes.db')

# needed to be able to use all the sqlite features.
curr = conn.cursor()

# create a table or execute a statement.

# curr.execute("create table quotes_tb(title text,author text,tag text)")

# insert data into the table.
curr.execute("insert into quotes_tb values ('Python is awesome!!','buildwithpython','python') ")

# Commit changes and close the connection
conn.commit()
conn.close()

########

#### Adding Data to a SQL Lite 3 Table ####

# Define your item pipelines here

#

# Don't forget to add your pipeline to the ITEM_PIPELINES setting

# See: <https://docs.scrapy.org/en/latest/topics/item-pipeline.html>

# useful for handling different item types with a single interface

# import SQLite3 to store in a db.
import sqlite3

from itemadapter import ItemAdapter

# Scraped Data > Item Containers > Pipieline > SQL DB

# Scraped Data > Item Containers > JSON/CSV

# Uncomment the ITEM_PIPELINES Class

# 300 = Pipeline priority

class QuotestutorialPipeline:

    #Run whenever the file is triggered.
    #What do you want to happen when scrapy is called all the time.
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass

    # Creating a connection
    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")

        #Activate the table/db.
        self.curr = self.conn.cursor()

    #Create a table, and drop it if it already exists.
    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS quotes_tb")
        self.curr.execute("create table quotes_tb(title text,author text,tag text)")

    def process_item(self, item, spider):
        #What do we process when the scrapy is crawled...

        #Add the items to the database using the store_db function.
        self.store_db(item)
        #print("Pipeline:" + item['quote'][0])
        #Also print to the terminal
        return item

    #Add item to the class, as we are going to be using the item values.
    def store_db(self,item):
    #What are we inserting when we execute the script.
        self.curr.execute("insert into quotes_tb values (?,?,?) ",(
            item['quote'][0],
            item['author'][0],
            item['tag'][0]
        ))

        #Confirm the changes. Not closing as required in the loop.
        self.conn.commit()

#### Full Quotestutorial Project ####

##############################
# Items.py ##

# Define here the models for your scraped items

#

# See documentation in

# <https://docs.scrapy.org/en/latest/topics/items.html>

import scrapy

class QuotestutorialItem(scrapy.Item):
    # define the fields for your containters here:
    quote = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()

#########################################
# Quotestutorial.py #
# Running using the terminal, scrapy crawl {Name variable below},Make sure you are in the folder just before "spiders" Right Click > Open in termninal.
# Importing Scrapy
# Creating a class and inheriting the scrapy.Spider inheritance
# Defining a parse file, Self (refer to) = the url,  response = the page source.
# Tutorial #11 - <https://www.youtube.com/watch?v=cC9aFbViT_c&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=11>
# Last modified 02/07/2021

import scrapy

from ..items import QuotestutorialItem

class QuoteSpider(scrapy.Spider):

    #What are we naming the spider.
    #What URL we want to scrape
    #Must always be called name and start_urls

    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    #Must always be called parse, self = the url above?
    def parse(self, response):
        # Storing the container inside a class.

        items = QuotestutorialItem()

        #Specify the class to go inside. (Everything grouped by this class?)
        all_div_quotes = response.css('div.quote')

        #To group title/author/tag together, use a for loop (For each quote, group.)
        for quotes in all_div_quotes:

        #Specify the classes inside the main class above.

            quote = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            # Linking the items to the contianers to the css data above.
            #Normal code is yeild{'title':quote}

            items['quote'] = quote
            items['author'] = author
            items['tag'] = tag

            yield items

#### End Project ######

### Full Intermediate Project ###

import scrapy

class AllrugsSpider(scrapy.Spider):
    name = 'allrugs'
    start_urls = ['https://www.therugshopuk.co.uk/rugs-by-type/rugs.html']

    def parse(self, response):
 #For each item that has the div product item info do this..

        for item in response.css('div.product-item-info'):
            yield {
                'title': item.css('img.product-image-photo.image::attr(alt)').get(),
                'link': item.css('a.product-item-link::attr(href)').get(),
                'price': item.css('span.price::text').get(),
            }

 #To scrape more than one page, find the next tag and until no page is found loop through the above.
            next_page = response.css('a[title=Next]::attr(href)').get()

            if next_page is not None:
                yield response.follow(next_page,callback= self.parse)

##### End Of Intermediate Project. #####

````

## Using MYSQL Workbench

Create a connection using "MYSQL Connections" in Workbench
Do not need to change any information, just create a connection name.
Double Click MySql Connection option and enter password from installation.

Open the schemas > Right Click > Create Schema
Apply x2 and Finish
View Schema should show new Database added.

### PyCharm Settings

Open Pipelines.py

Define your item pipelines here

Don't forget to add your pipeline to the ITEM_PIPELINES setting

See: <https://docs.scrapy.org/en/latest/topics/item-pipeline.html>

useful for handling different item types with a single interface

```` python

# import SQLite3 to store in a db

import mysql.connector

from itemadapter import ItemAdapter

# Scraped Data > Item Containers > Pipieline > SQL DB

# Scraped Data > Item Containers > JSON/CSV

# Uncomment the ITEM_PIPELINES Class

# 300 = Pipeline priority

class QuotestutorialPipeline:

    # Run whenever the file is triggered.
    # What do you want to happen when scrapy is called all the time.
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass

    # Creating a connection
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='toor',
            database='myquotes'

        )

        # Activate the table/db.
        self.curr = self.conn.cursor()

    # Create a table, and drop it if it already exists.
    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS quotes_tb")
        self.curr.execute("create table quotes_tb(title text,author text,tag text)")

    def process_item(self, item, spider):
        # What do we process when the scrapy is crawled...

        # Add the items to the database using the store_db function.
        self.store_db(item)
        # print("Pipeline:" + item['quote'][0])
        # Also print to the terminal
        return item

    # Add item to the class, as we are going to be using the item values.
    def store_db(self, item):
        # What are we inserting when we execute the script.
        self.curr.execute("insert into quotes_tb values (%s,%s,%s) ", (
            item['quote'][0],
            item['author'][0],
            item['tag'][0]
        ))

        # Confirm the changes. Not closing as required in the loop.
        self.conn.commit()

###### Following Links ######

# After the yield

 next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

####
````

#
# 
#
#

from BeautifulSoup import BeautifulSoup
import urllib2
from Tkinter import *

# Variable Declarations
xml = ''
url = "http://www.appshopper.com/feed/?mode=featured&filter=new&type=paid&platform=ios"
csvData = 'Title, Release Date, Icon Link,\n'
game_title = ''
game_date = ''
game_img = ''
illegal1 = ''
illegal2 = ''
soup = ''
items = []


# Opens the feed
file = urllib2.urlopen(url)
xml = file.read()
file.close()

# Remove CDATA to make parseable
illegal1 = '<![CDATA['
illegal2 = ']]>'
xml = xml.replace(illegal1, '').replace(illegal2, '')


soup = BeautifulSoup(xml)

items = soup.findAll('item')


# Parse the items in the xml feed and append to csv string
for i in range(len(items)):
    
    # For each item, parser extracts the contents of the 'title', 'pubdate',
    # and 'img' tags (contents are type list), then retrieves the contents of 
    # the first item in the resulting list
    game_title = items[i].find('title').contents
    game_title = str(game_title[0]).strip()

    game_date = items[i].find('pubdate').contents
    game_date = str(game_date[0]).strip()
    game_date = game_date[5:]	# Removes the 'Mon, '
    
    game_img = items[i].findAll('img')
    game_img = str(game_img[1]) # 2nd link is the one we want: [1]

    # Extracts the url from the <img src="what_we_want" ... /> tag
    game_img = game_img.replace('<img src="', '').replace('" align="right" />', '')

    # Appends the title, date, and img url to the csv on a new line
    csvData = csvData + ('\n' + game_title + ', ' + game_date + ', ' + game_img + ', ')


print csvData

csvFile = open('games.csv', 'w')
csvFile.write(csvData)

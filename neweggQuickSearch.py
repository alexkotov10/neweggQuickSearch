########################################################

# neweggQuickSearch.py is a script which automates
# automates the process of searching for products
# and returns important information back in a CSV.

# Libraries Used: urllib.request and bs4 (BeautifulSoup)

# neweggQuickSearch.py asks the user to input information
# such as newegg region, product region and search filter

# neweggQuickSearch.py currently supports the US and CA
# region, however more regions will be added as time
# passes.

# neweggQuickSearch.py is completely safe to use and
# legal to use.

# please report any issues to my github immediately.
# any known error in the program will only happen if the
# intended search has 0 results. (Plan to Fix for Future)

# neweggQuickSearch.py can be reused or edited in any way.

# Alex Kotov 09/07/2020

########################################################

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import sleep

# Newegg Region Choices
options = ['US','CA']

# Ask user for Newegg Region
country = input("Which Newegg would you \nlike to use? CA or US?: ")
while country.upper() not in options:
    country = input("'" + str(country) + "' is not an option.\nplease choose from CA or US?: ")

# creates URL based on Region
if country.upper() == 'US':
    url = 'https://www.newegg.com/p/pl?d='
else:
    url = 'https://www.newegg.ca/p/pl?d='

# creates the final URL
search = input("What would you like to search?: ")
searchurl = str(url) + str(search.replace(' ', '+'))
def choices():
    # a list of additional search options
    print("Type F to Sort Results by Featured Items (Default).")
    print("Type L to Sort Results by Lowest Price to Highest.")
    print("Type H to Sort Results by Highest Price to Lowest.")
    print("Type S to Sort Results by Best Selling.")
    print("Type R to Sort Results by Best Ratings.")
    print("Type M to Sort Results by Most Reviews.")
    print("Type N to Sort Results by Newest Results.")

# ask the user for additional search options
choice = 'default'
SortOptions = ['F','L','H','S','R','M','N']
while choice not in SortOptions:
    print("Please type a letter corresponding to the options below.")
    choices()
    choice = input("choice: ")

# add to url based on search option
if choice.upper() == 'F':
    searchurl += '&Order=0'
if choice.upper() == 'L':
    searchurl += '&Order=1'
if choice.upper() == 'H':
    searchurl += '&Order=2'
if choice.upper() == 'S':
    searchurl += '&Order=3'
if choice.upper() == 'R':
    searchurl += '&Order=4'
if choice.upper() == 'M':
    searchurl += '&Order=5'
if choice.upper() == 'N':
    searchurl += '&Order=6'

# read URL
uClient = uReq(searchurl)
page_html = uClient.read()

# close URL
uClient.close()

# create csv file
filename = 'products.csv'
f = open(filename, 'w')

# write default headers
headers = 'Product Name, Price, Star Rating, Shipping cost \n'
f.write(headers)

# html parsing
pagesoup = soup(page_html, "html.parser")
containers = pagesoup.findAll("div",{"class":"item-container"})

# loop for each product container
for container in containers:

    # Get Full Product Name
    brand = container.find("a",{"class":"item-title"})
    productname = brand.text

    # Get Price
    pricedollar = container.find("li",{"class":"price-current"})
    price = pricedollar.text.split()

    # Parse Rating
    rating = container.find("a",{"class":"item-rating"})

    # Create Rating String for Reviews
    if str(rating) != 'None':
        amofrating = container.find("span",{"class":"item-rating-num"})
        amofratingtxt = str(amofrating.text)

        chartoremove = '()'
        for character in chartoremove:
            amofratingtxt = amofratingtxt.replace(character,'')

        # Parse Star Rating
        starrating = rating['title'].split()[2]

	# Plural Detection
        if int(amofratingtxt) > 1:
            ratingmessage = str(starrating) + " star rating with " + str(amofratingtxt) + " reviews"
        else:
            ratingmessage = str(starrating) + " star rating with " + str(amofratingtxt) + " review"

    # Create Rating String for No Reviews
    else:
        ratingmessage = 'No Reviews'

    # Parse Shipping
    shipping = container.find("li",{"class":"price-ship"})

    # write each product detail in csv
    f.write(productname.replace(",", "|") + ',' + price[0] + ',' + ratingmessage + ',' + shipping.text + "\n")

# close file to make it accessable to the user
f.close()

# inform the user the csv has been created.
print("The CSV Has Been Created, this program will close in 10 seconds.")
sleep(10)

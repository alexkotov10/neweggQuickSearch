# neweggQuickSearch.py

neweggQuickSearch.py is a python program that searches products from newegg.ca or newegg.com and returns the price, shipping cost, products and review information in a organized CSV Format.

Libraries bs4 and urllib.request are needed to run this python program.

**This Version of neweggQuickSearch.py is 1.0.1.**

# Usage

If you would like to use this program, Download the Zip and extract the zip folder.

If you do not have Python Installed and would like to use the program, use `neweggQuickSearch.exe`. Otherwise either version can be used if you have python installed.

Immediately from launch, , the program will ask the user which region they would like to search from on newegg. To be exact, the following message will appear.

```
Which Newegg would you 
like to use? CA or US?: 
```

From there on, the program will ask the user for more inputs such as product and how the search should be sorted.

if the program closes or an error appears, your intended search result did not have any results and you will have to restart the program.

Once the program has finished, the program will return a message saying a CSV has been created and products.csv will be created in the same directory as the program. To be exact, the following message will appear.

```
The CSV Has Been Created, this program will close in 10 seconds.
```

After this message, the program will close in 10 seconds if you are using the `.exe` version.

# Notes

neweggQuickSearch.py currently only works with the Canadian and American Versions of the Website. UK Versions and Versions across Europe are to be next added.

Any errors should be reported to the github.

If you have python installed, the recommendation is to use the `.py` version as there could be unknown bugs with the `.exe` version and bugs are much easier to report using the `.py` version.

neweggQuickSearch can be reused or edited in any way.
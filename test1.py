#200811 with Sam - learned how to analyze html, learned some command line, learned how to web scrap quotes from website, data structures, file manip, text writing, ...

import requests
import pprint
from bs4 import BeautifulSoup
import os
print(os.getcwd())#gets current working directory

req = requests.get("http://quotes.toscrape.com/")

# making soup object; takes an html and a parser
soup = BeautifulSoup(req.text,'html.parser')

#view html in a neater fashion with prettify method
# print(soup.prettify())

#find all links in the website --> stores in a list
# link element = 'a'
#printlink = soup.find_all('a')

#find all quotes on the page;
# all quotes have a class of text; attrs = {}; {} = dictionary (a data structure)
# {key:value} where key = a name, and value = can be anything (an int, an object, a string, etc)
printlink = soup.find_all(attrs = {"class":"text"})

#create a new list to hold quotes
print_element_from_printlink =[]

#create a text file
quote_file = open("quotes/quotes.txt", "a+") #+ creates a file if it doesn't exist

# for loop to print everything in the printlink list
for i in printlink:
    quote_file.write(i.get_text()+'\n')#writes the quotes to the quote quote_file, adds a new line

    #print_element_from_printlink.append(i.get_text()) #print the text from each element in list
    # print(i.get('href')) #print the exact link of each element in the list

#pretty print the text from printlink list
# pprint.pprint(print_element_from_printlink)

quote_file.close()#stops the writing to the text file


# print(req.text)
# pprint.pprint(req.__dict__)
# print(req.url)

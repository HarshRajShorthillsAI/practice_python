from bs4 import BeautifulSoup

with open('../home.html', 'r') as html_file:
    content = html_file.read()
    #print(content) #Demonstrates that html file can be read.
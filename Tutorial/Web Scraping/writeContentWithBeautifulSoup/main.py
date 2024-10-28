from bs4 import BeautifulSoup

with open('../home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    print(soup.prettify()) #Demonstrates that using BeautifulSoup the html content is retrieved from file prettier
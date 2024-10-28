from bs4 import BeautifulSoup

with open('../home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    tags = soup.find('h5')
    print(tags) #This only searches for first occurance of h5 tag and stops searching
from bs4 import BeautifulSoup

with open ("home.html") as htmlfile:
    soup=BeautifulSoup(htmlfile,'html5lib')

#grab the title of the page
title=soup.title.text

#grab a div
div1=soup.div.text

#grab a specific div
div2=soup.find('div',id='footer').text
div3=soup.find('div',class_='mywork').text

#grab a value in text and turn it to int
div4=soup.find('div',class_='mynumber')
number=div4.p.text
number=int(number)

#grab all divs with a similar css class
for item in soup.find_all('div', class_='myname'):
    head=item.h1.text
    print(head)

    name=item.p.text
    print(name)

    print('')

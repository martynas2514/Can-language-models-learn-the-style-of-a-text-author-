import requests
from bs4 import BeautifulSoup


URL = input ("www?")
print("\n")
look_for = input ("look_for?")
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


#look_for = "Joe Biden:"
name = look_for[:-1]+ "_" + URL[URL.rfind("/")+1:] + ".txt"

data_text = ""
for row in soup.find_all("p"):
    if row.text.startswith(look_for):
        text = row.text
        data_text += " " +  text[(text.rfind("\n")+1):]

with open(name, 'w') as f:
        f.write(data_text)
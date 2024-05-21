from bs4 import BeautifulSoup

with open("./website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.li)

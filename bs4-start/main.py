from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

td_list = soup.find_all(name="td", class_="subtext")

score_list = []
for td in td_list:
    score = td.find(name="span", class_="score")
    if score is not None:
        score_list.append(int(score.get_text().split()[0]))
    else:
        score_list.append(0)

text_list = []
links_list = []

anchor_tags = [span_tag.find("a") for span_tag in soup.select(selector=".titleline")]

for tag in anchor_tags:
    text_list.append(tag.get_text())
    links_list.append(tag.get("href"))

print(text_list)
print(links_list)
print(score_list)

highest_vote_index = score_list.index(max(score_list))

print(f"Highest upvotes story title: {text_list[highest_vote_index]} and its link: {links_list[highest_vote_index]}"
      f"with upvotes of {score_list[highest_vote_index]}")

print(f"text_list len: {len(text_list)}, links_list len: {len(links_list)}, score_list len: {len(score_list)}")

# title_lines = soup.select(selector=".titleline")
#
# for title_line in title_lines:
#     anchor_tag = title_line.select_one(selector="a")
#     print(f"{anchor_tag.get_text()} -> {anchor_tag.get("href")}")

# anchor_tags = soup.select(selector=".titleline a")
# print(anchor_tags)
# for title_line in anchor_tags:
#     anchor_tag = title_line.select_one(selector="a")
#     print(f"{anchor_tag.get_text()} -> {anchor_tag.get("href")}")

# anchor_tag = soup.select_one(selector=".titleline a")
# print(anchor_tag)
# anchor_title = anchor_tag.get_text()
# anchor_link = anchor_tag.get("href")
# print(f"{anchor_title} {anchor_link}")
#
# score = soup.find(name="span", class_="score")
# first_score =score.get_text()
# print(first_score)


# with open("./website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.li)
#
# anchor_tags = soup.find_all("a")
# print(anchor_tags)
#
# for tag in anchor_tags:
#     # print(tag.string)
#     # print(tag.getText())
#     print(tag.get("href"))
#
# print(soup.find(name="h1", id="name"))
#
# heading = soup.find(name="h3", class_="heading")
# print(heading)
# print(heading.get("class"))
#
# print(soup.find(name="a", href="https://www.appbrewery.co/"))
#
#
# anchor_tag = soup.select_one(selector="p a")
# print(anchor_tag)
#
# h1 = soup.select_one(selector="#name")
# print(h1)
#
# h3 = soup.select(selector=".heading")
# print(h3)

from bs4 import BeautifulSoup
import requests

# response = requests.get(
#     "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
#
# with open("./movie_list.txt", "w", encoding="utf-8") as sink:
#     sink.write(response.text)
# print("Done ...")

with open("./movie_list.txt") as source:
    html_cache = source.read()

soup = BeautifulSoup(html_cache, "html.parser")

# h3_list = soup.select(selector=".title")
h3_list = soup.find_all(name="h3", class_="title")

print(h3_list[::-1])

# Method1
# title_list = [h3.get_text() + "\n" for h3 in h3_list[::-1]]
# print(title_list)
#
# title_string = "".join(title_list)
# print(title_string)
#
# with open("movies.txt", "w") as destination:
#     destination.write(title_string)

# # Method2
# title_list = [h3.get_text() for h3 in h3_list[::-1]]
# print(title_list)
#
# title_string = "\n".join(title_list)
# print(title_string)
#
# with open("movies.txt", "w") as destination:
#     destination.write(title_string)


# Method3
with open("./movies.txt", "w") as destination:
    for h3 in h3_list[::-1]:
        destination.write(h3.get_text() + "\n")

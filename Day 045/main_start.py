from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_eb_page = response.text

soup = BeautifulSoup(yc_eb_page, 'html.parser')

articles = soup.find_all(name="a", class_="storylink")
scores = soup.find_all(name="span", class_="score")

# First articles datas
article_tag = articles[0]
article_text = articles[0].getText()
article_link = articles[0].get("href")
article_score = scores[0].getText()

# Articles lists of datas
article_texts = []
article_links = []


for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in scores]

print(article_texts)
print(article_links)
print(article_upvotes)

highest_upvote = max(article_upvotes)
index = article_upvotes.index(highest_upvote)

print(f"Title: {article_texts[index]}, Link: {article_links[index]}, Score: {highest_upvote}")

# with open("website.html") as file:
#     website = file.read()
#
# soup = BeautifulSoup(website, 'html.parser')
#
# print(soup.prettify())
# # print(soup.title)
# # print(soup.title.string)
# print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tags in all_anchor_tags:
#     print(tags.getText())
#     print(tags.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.getText())
#
# all_headings = soup.find_all(name="h1")
# print(all_headings)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# company_urls = soup.select(selector="ul li a")
# print(company_urls)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select(selector=".heading")
# print(heading)

from bs4 import BeautifulSoup

with open(r"45_Beautiful_Soup\bs4-start\website.html", "r") as html_doc:
    contents = html_doc.read()

soup = BeautifulSoup(contents, 'html.parser')
# title_tag = soup.title
# print(title_tag.name) #element name
# print(title_tag.string) #text string
# print(soup.prettify)
# print(soup.a)
# print(soup.p)



###### Get Tags: ###### 
# all_paragraph_tags = soup.find_all(name="p")
# all_anchor_tags = soup.find_all(name="a")\
# for tag in all_anchor_tags:
    # print(tag, "\n")
    # print(tag.name)
    # print(tag.string) 



###### Get Tag's Attributes: ######
# for tag in all_anchor_tags:
    # print(tag['href'])
    # print(tag.get("href"))
    # print(tag.attrs)



###### Get Tag with Specific Attributes: ######
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))



###### Get Nested Tag (using CSS language) ######
# company_url = soup.select_one(selector="p a") #an a tag inside a p tag
# print(company_url)

# name = soup.select_one(selector="#name") #select using ID
# print(name)

# headings = soup.select(selector=".heading") #select using CLASS
# print(name)

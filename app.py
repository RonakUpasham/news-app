from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

PATH = '/Users/kshitijaupasham/Desktop/news/chromedriver'
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)


def headlines(category):
    final_articles = []
    final_headlines = []
    final_img_links = []
    final_website_links = []
    final_website_names = []
    driver.get('https://inshorts.com/en/read'+ category) #news category
    loadMore()
    headlines = driver.find_elements_by_xpath('.//span[@itemprop = "headline"]') # get headline
    articles = driver.find_elements_by_xpath('.//div[@itemprop = "articleBody"]') # get articles
    img_links = driver.find_elements_by_class_name("news-card-image") # get image
    website_links = driver.find_elements_by_class_name("source") #get full article link and name
    for article in articles:
        final_articles.append(article.text)   # article text
    for website in website_links:
        final_website_names.append(website.text)   # website name
        final_website_links.append(website.get_attribute('href')) # website links
    for img_link in img_links:
        final_img_links.append(img_link.value_of_css_property('background-image')[5:-2]) # image links
    for headline in headlines:
        final_headlines.append(headline.text)   # article headlines
    return(final_headlines,final_img_links,final_website_links,final_website_names,final_articles)


def loadMore():
    for _ in range(2):
        search = driver.find_element_by_class_name('load-more')
        search.click()
        time.sleep(1)


def category_select(argument):
    switcher = {
        "bt1": "",
        "bt2": "/national",
        "bt3": "/politics",
        "bt4": "/world",        
        "bt5": "/business",
        "bt6": "/technology",
        "bt7": "/startup",
        "bt8": "/science",
        "bt9": "/sports",
        "bt10": "/entertainment"
    }
    return(switcher.get(argument, "Invalid month"))


@app.route('/')
def home():
    #article, headline = text()
    return render_template('index.html')

@app.route('/interactive/')
def interactive():
    btn_category = request.args.get('category', 0, type=str)
    category = category_select(btn_category)
    headline, img_links, website_links, website_names, articles = headlines(category)
    return(jsonify(headlines=headline, img_links=img_links, website_links=website_links, website_names=website_names, articles=articles))


if __name__ == "__main__":
    app.run(debug=True)

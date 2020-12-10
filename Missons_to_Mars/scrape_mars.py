
# Dependencies
# import os
from bs4 import BeautifulSoup as bs
# import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time 

# ## Step 1 - Scraping

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    
    # -------- NASA Mars News ---------
    # visit https://mars.nasa.gov/news/' url
    url_news = 'https://mars.nasa.gov/news/'
    browser.visit(url_news)

    time.sleep(1) 

    # create soup object
    html = browser.html
    soup = bs(html, 'html.parser')

    # Scrape the website for the most recent headline. Note that, for the headline title, this is the second 
    # matching element on the page, as the first match is in the navigation bar.  The paragraphs is the first  
    # on the page 

    title = soup.find_all('div', class_='content_title')[1].text
    paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
    
    # print article info
    print('-----------------')
    print(title)
    print(paragraph)

    # ---------- JPL Mars Space Images - Featured Image ----------

    # url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_image)
    time.sleep(1)

    # find the large-size images. First, find the page where it is located. 
    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find(id = "full_image")["data-link"]
    feature_image_url = "https://www.jpl.nasa.gov" + image
    
    # visit the page (from above) where it is located 
    browser.visit(feature_image_url)

    # get the link to the jpg itself
    html = browser.html
    soup = bs(html, 'html.parser')
    image_lg = soup.find('img', class_ = "main_image")["src"]
    image_lg_url = "https://www.jpl.nasa.gov" + image_lg

    # ---------- Mars Facts ----------

    # url for Mars Facts [here](https://space-facts.com/mars/)
    url_facts = 'https://space-facts.com/mars/'
    browser.visit(url_facts)
    time.sleep(1)

    # Use Pandas to scrape the table containing facts about the planet. First import dependency
    import pandas as pd

    #read table
    table = pd.read_html(url_facts)
 
    # convert list to a dataframe - call [0] for the first table in the page, although here there is only one  
    planet_df = table[0]
    
    # assign column header names 
    planet_df.columns = ['Fact Type', 'Answer']
    
    #convert table to html table string. Note, when you make changes here, need
    #to rerun the web-scraping through the button on app for the changes to take effect
    planet_table_html = planet_df.to_html (index=False)

    # remove new lines /carriage returns
    planet_table_html = planet_table_html.replace('\n', '')

    # # export table to html 
    # planet_df.to_html2('table.html', index=False)
# ---------- Mars Hemispheres ----------

    # Assign variable for url https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars 
    url_astro = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_astro)
    time.sleep(1)

    # obtain the url for the high-resolution image for each of Mars hemispheres, along with the title
    # construct for-loop to identify all the titles and image urls, add them to the dictionary, and
    # store the dictionary in a list

    hemi_list = []

    for i in range(4):
        # click on the html for the image - now at the next page
        browser.find_by_tag('h3')[i].click()
        # create HTML and beautiful soup objects
        html = browser.html
        soup = bs(html, 'html.parser')
        # get image source link for full-resoultion photo
        image_1 = soup.find('img', class_='wide-image')['src']
        # construct url from original page to full-resolution image photo
        image_1_url = 'https://astrogeology.usgs.gov' + image_1
        # find title of hemisphere photo at the photo page 
        title_1 = soup.find('h2', class_= 'title').text
        # add the title and its corresponding image to a dictionary
        hemi_dict = {'Title': title_1, 'Image_URL': image_1_url}
        # append the dictionary to the list
        hemi_list.append(hemi_dict)
        #go back to the original page with all four hemispheres
        browser.back()

    # store all scraped data in a dictionary
    mars_data = {
        "news_title": title,
        "news_paragraph": paragraph,
        "featured_image": image_lg_url,
        "fact_table": planet_table_html,
        "hemispheres": hemi_list
    }

    # Close the browser after scraping
    browser.quit()
    
    # Return results
    return mars_data


 


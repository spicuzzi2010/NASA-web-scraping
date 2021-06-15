import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    #configuring splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    #Opening the NASA site in the browser
    NASA_url = 'https://redplanetscience.com/'
    browser.visit(NASA_url)

    time.sleep(5
    )
    #Creating a beautiful soup object
    html = browser.html
    NASA_soup = soup(html, 'html.parser')

    #Try and except in case of errors
    try:
        #storing the first title text in news_title and title paragraph in news_p
        news_titles = NASA_soup.find('div', class_='content_title').get_text()
        news_p = NASA_soup.find('div', class_='article_teaser_body').get_text()

    #If attribute error, return none for news_title and news_p
    except AttributeError:
        return None, None
    
    #JPL Mars Space Images - Featured Image

    #Navigate to the spave JPL url
    JPL_url = 'https://spaceimages-mars.com'
    browser.visit(JPL_url)

    #Create a beautiful soup object
    html = browser.html
    mars_soup = soup(html, 'html.parser')

    #Storing the image relative path in mars_url
    mars_url = mars_soup.find('img', class_='headerimage')['src']

    #Using relative img url to create absolute path
    mars_img_url = f'{JPL_url}/{mars_url}'

    # Mars Facts

    mars_facts_url = 'https://galaxyfacts-mars.com'
    mars_facts_df = pd.read_html(mars_facts_url)[0]

    mars_facts_df.columns=['Description', 'Mars', 'Earth']
    mars_facts_df = mars_facts_df.iloc[1:]
    mars_facts_df = mars_facts_df.reset_index(drop=True)
    mars_facts_df.set_index('Description', inplace=True)

    #converting mars df to html table
    mars_table =  mars_facts_df.to_html(classes=["table", 'table-striped'])
    
    #Stripping unwanted newlines 
    stripped_html_table = mars_table.replace('\n', '')

    # Mars Hemispheres

    astrogeology_url = 'https://marshemispheres.com/'
    browser.visit(astrogeology_url)

    html = browser.html
    hemisphere_soup = soup(html, "html.parser")
   
    #Create a list of all of the hemisphere images
    hemispheres = hemisphere_soup.find_all('div', class_='description')

    #Create a list to hold the image links.
    hemisphere_images = []

    for div in hemispheres:
        link = div.find('a', class_='itemLink')['href']
        img_link = f'{astrogeology_url}{link}'

        #append list image urls
        hemisphere_images.append(img_link)
    

    hemisphere_image_urls = []

    #loop through the list of image urls
    for url in hemisphere_images:
        #visit each url in the images url list
        browser.visit(url)
        #Create beautifulsoup object
        html = browser.html
        img_soup = soup(html, "html.parser")

        #parse to find the image url
        hemisphere_url = img_soup.find_all('a', target='_blank')[2]['href']
        img_url = f'{astrogeology_url}{hemisphere_url}'

        img_title = img_soup.find('h2',class_='title').text

        hemisphere_dict = {
            "title": img_title,
            "img_url": img_url
        }

        hemisphere_image_urls.append(hemisphere_dict)



    #Store results in a dictionary
    mars_data = {
        "news_title": news_titles,
        "news_title_paragraph": news_p,
        "featured_image": mars_img_url,
        "facts": stripped_html_table,
        "hemispheres": hemisphere_image_urls
    }

    browser.quit()
    return mars_data
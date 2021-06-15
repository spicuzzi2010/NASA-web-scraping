# NASA-web-scraping

## Web Scraping

The [Web Scraping Notebook](./mission_to_mars.ipynb) notebook contains web scraping to to get the following information:

### NASA Mars News

* Scrape the Mars News Site and collect the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image

* Visit the url for the Featured Space Image site.
* Use splinter to navigate the site and find the image url for the current Featured Mars Image.

### Mars Facts

* Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
* Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

## MongoDB and Flask Application

The [Flask App](./app.py) app uses MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* The Jupyter notebook above was converted into a Python script called [Web Scraping script](./scrape_mars.py) with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, I created a route called /scrape that will import the scrape_mars.py script and call the scrape function.
* * The return values are stored in Mongo as a Python dictionary.
* A root route was also created that will query the Mongo database and pass the mars data into an HTML template to display the data.

### HTML Templates

* The [HTML Template](./templates/index.html) contains the HTML code used  to take the mars data dictionary and display all of the data in HTML elements shown in the screenshot below:

![Mars Web App](./screenshots/app_screenshot.png)

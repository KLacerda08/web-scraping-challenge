# Mission to Mars

![Title](Images/mars.jpg)

## Table of contents
* [Assignment](#assignment)
* [Data Sources](#data_sources)
* [Website Design](#design)
* [Lesson Learned](#lessons)

## Assignment
Perform web scraping and design an app to seamlessly display the scraped data into a user interactive website 
that can be updated by the push of a button.  

## Data Sources
Data was scraped from the following websites:  
- NASA Mars News from: https://mars.nasa.gov/news/
- Featured Mars Image from: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
- Facts About Mars from: https://space-facts.com/mars/
- Mars Hemispheres from: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

To design the website, the following tools were used: 
- Web-scraping
- Flask
- html coding with added custom (within the .html)
- Bootstrap css style sheet:  https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"

## Website Design
Data was scraped from each site using Spliter and Beautiful Soup, as shownin the jupyter notebook file, here: 
https://github.com/KLacerda08/web-scraping-challenge/tree/main/Missions_to_Mars.mission_to_mars.ipynb 

At first, a get request was attempt; however, while no errors were logged, data was not being returned.  
Therefore, Splinter was used. Splinter and Beautiful soup were used to scrape and parse the data, and to 
navigate to the various required pages. This required the use of click functions in Splinter to navigate
to, and back from certain pages.  Additionally, Pandas was used to transform data from a scraped table to 
an html string that could be incorporated as a table back in the website.  Images of the site are shown below:

### Top of Website, Feature Image and Facts Table
![Title](Missions_to_Mars/Snips/image1_top_image_table.png)

### Mars Hemispheres
![Title](Missions_to_Mars/Snips/image2_mars_hemis.png)


## Lessons Learned
This was a challenging project, but in the end it was also good practice for combining various things we 
have learned so far, html, css work, flask, and pandas, as well as new functions like web-scraping.  


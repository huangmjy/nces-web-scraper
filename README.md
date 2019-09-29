# nces-web-scraper
# runs in Python 3, big thanks to https://pruizjunco.wordpress.com/coding/python/ for reference/base code 
NCES web scraper originally written to scrape data for the CTC (College Transition Collaborative)

Author: Michelle Huang 

This script scrapes the NCES (National Center for Education Statistics) website for college undergraduate population and admissions rate information and writes the result to a CSV file.
The program needs to be used in tandem with the included ipeds_ids.txt, which contains the ids of all the universities in the NCES database.
Any place where -9999 appears in the resulting .csv means that an error or exceptional case occurred while trying to scrape for that college's information.

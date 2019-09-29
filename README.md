# nces-web-scraper
NCES web scraper originally written to scrape data for the CTC


# Note1: runs in Python 3, big thanks to https://pruizjunco.wordpress.com/coding/python/ for reference code 
# Author: Michelle Huang 
# This script scrapes the NCES website for college undergraduate population and admissions rate information and writes this to a CSV file
# The program needs to be used in tandem with the included ipeds_ids.txt, which contains the ids of all the universities in the NCES database.
# Any place where -9999 appears in the resulting .csv means that an error or exceptional case occurred while trying to scrape for that college's information.

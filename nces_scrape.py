# Note: runs in Python 3, some code is from https://pruizjunco.wordpress.com/coding/python/
# Author: Michelle Huang 
# This script scrapes the NCES website for college undergraduate population and admissions rate information and writes this to a CSS file
# Note2: need to locate an ipeds_ids.txt file, which contains the ids of all the universities 

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# This function takes in a university's IPEDS ID and returns the corresponding College Navigator HTML link. 
def open_url(uni):
    # define base url:
    '''
    Example: for university with id 457590 the url would be "https://nces.ed.gov/collegenavigator/?&id=457590".
    Therefore, if looping over id then the url is base1 + base2 + str(id).
    '''
    base1 = "https://nces.ed.gov/collegenavigator/"
    base2 = "?&id="
    html = urlopen(base1 + base2 + str(uni)).read()
    return html

# This function uses a university's IPEDS ID to retrieve the university's name, undergraduate population, and admit rate. 
# If -9999 appears in the output, it indicates that an error occured at that step of the process (either the info page or that specific information could not be found).
def get_info(uni):
    html = open_url(uni)
    # check to make sure that the info page was pulled up successfully
    if "The selected institution could not be found" in str(html):
        return ([-9999]*3) # error finding the university's information
    soup = BeautifulSoup(html, features="lxml")
    # find & extract university name
    uniName = soup.find("span", "headerlg").text

    # find undergraduate population
    if soup.find("td", text="Student population:\xa0\xa0"):
        uPop = soup.find("td", text="Student population:\xa0\xa0").find_next_sibling("td").text
        # community college / technical college special case
        if "all undergraduate" in uPop:
            ind1 = uPop.find("(") - 1
            uPop = uPop[:ind1]  
        # extract relevant number from the text, general case
        elif "undergraduate)" in uPop:
            ind1 = uPop.find("(") + 1
            ind2 = uPop.find("u") - 1
            uPop = uPop[ind1:ind2]
        else: 
            uPop = "-9999"
    else:
        uPop = "-9999" # error finding undergraduate population

    # find & extract admit rate, default case
    if soup.find("td", text="Percent admitted"):
        admitRate = soup.find("td", text="Percent admitted").find_next_sibling("td").text
    # open enrollment case
    elif soup.find("li", text="This institution has an open admission policy. Contact the institution for more information."):
        admitRate = "open admission"
    # other exceptional case
    else:
        admitRate = "not reported"

    # gather extracted data into one place
    foundData = []
    foundData.append(uniName)
    foundData.append(int(uPop.replace(",","")))
    foundData.append(admitRate)
    return foundData

# This function writes gathered information to a .csv file called scrape_output.csv. 
# Requires an ipeds_ids.txt file that contains different university IPEDS IDs to run.
# An invalid IPEDS id results in -9999, -9999, -9999 being written to the output .csv. 
def write_info(): 
    # create an output csv file named data_nces.csv to write information to
    with open("scrape_output.csv", "w", newline='') as nces:
        writer = csv.writer(nces)
        # header categories
        writer.writerow(["College Name", "Undergraduate Pop.", "Admit Rate"])
        unis = open("ipeds_ids.txt")

        for uni in unis:
            data = get_info(uni)
            writer.writerow(data)

write_info()
print("done!")
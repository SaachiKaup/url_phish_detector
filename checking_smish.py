import requests
import csv
import itertools as it
from url_parsing import *


def open_file(filename):
    return open(filename)

def read_file(opened_file):
    return csv.reader(opened_file)

def get_file(filename):
    return read_file(open_file(filename))

def list_of_lists_2_list(list_of_lists, condition = True):
    return [item for sublist in list_of_lists for item in sublist if condition]

def shorten_list(listname, no_of_items_dropped):
    return listname[no_of_items_dropped: ]

def get_urls(all_links, a_indx, b_indx):
    urls = []
    for obj in all_links:
        urls.append(obj[a_indx: b_indx])
    return shorten_list(urls, 10)

def get_special_urls(filename, suffix):
    all_links = get_file(filename) 
    urls = get_urls(all_links, 1, 3)
    return [b for [a, b] in urls if eval(a + suffix)]
    
def main():    
    phishing_urls = get_special_urls(FILENAME, '> 4')
    suspicious_urls = get_special_urls(FILENAME, 'in range (2, 4)')
    #works with all_links declared again print(suspicious_urls)
    result = ""
    if URL in suspicious_urls:
        result = "Suspicious"
    elif URL in phishing_urls:
        result = "Phishing Attack"
    else:
        result = check_url(URL)

    print("Result: ", result)

if __name__ == '__main__':
    FILENAME = "phish_score.csv"
    URL = input("Enter URL: ")
    main()


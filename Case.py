import csv
import urllib.request
import re

from bs4 import BeautifulSoup

import win_unicode_console
win_unicode_console.enable()




def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
        soup = BeautifulSoup(html, 'lxml')

        ads = soup.find_all('tr', class_='detail')

        doc = {}

        for ad in ads:
            label = ad.find('th', class_='label').text.strip().lower()
            value = ad.find('td', class_='value').text.strip().lower()
            
            str_l = str(label).split()
            sl = ''
            for i in str_l:
                sl += i + '_'
            sl = sl[:-1]
            
            str_v = str(value).split()
            sv = ''
            for i in str_v:
                sv += i + '_'
            sv = sv[:-1]

            doc[sl] = sv

        print(doc)

def parse_file(file):
    f = open(file, 'r')
    for i in f:
        if 'culturecollections.org.uk' in i:
            print('\n')
            parse(get_html(i))



def main():
    
    ansv = None
    print('Do you have URL or file(yes or no)?')
    
    while ansv != 'url' or 'file':
        
        ansv = input('URl / File:').lower()
        
        if 'url' in ansv:
            print('Please, print your link there :')
            avsv_url = input()
            try:
                print('\n')
                parse(get_html(avsv_url))
            except BaseException:
                print('Something went wrong')
            
        
        elif 'file' in ansv:
            print("Please, put your txt file into the folder with this program and print your file's name")
        
            while True:
                file = input()
        
                if '.txt' in file:
                    try:
                        parse_file(file)
                        break 
                    except BaseException:
                        print('Something went wrong')

        
                else:
                    print("Please print name with file's extension")



if __name__ == '__main__':
    main()
    a = input("End?")
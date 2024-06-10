from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

def set_url():              # set the desired url
    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    return url

def define_soup():          # define soup to use in other methods  
    url = set_url()
    response = requests.get(url)
    #response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
    
# golbal variables  
soup = define_soup()
table = soup.find_all('table')[1]           # change value to get a different table
column_headers = table.find_all('th')       # get the column headers from the table, 'th': html tag
extracted_column_headers = [header.text.strip() for header in column_headers] 
# extract the column headers into a suitable list format
column_data = table.find_all('tr')                                         # 'tr': html tag

df = pd.DataFrame(columns=extracted_column_headers)  
pd.set_option('display.max_rows', None)             # show all rows
pd.set_option('display.max_columns', None)          # show all columns

def request_url():      # request (instead of a get) the desired url
    url = set_url()
    response = requests.get(url)
    
def get_table():        # get the desired table from a certain url 
    request_url()
    if soup:
       # table = soup.find_all('table', class_='wikitable sortable')[1] # change value to get a different table
        print(table)
    else:
        print("Soup object is None, cannot extract tables.")

def get_column_headers():           # get the column headers from the table  
    request_url()
    if soup:
        print(column_headers)
    else:
        print("Soup object is None, cannot extract column headers.")

def put_column_headers_in_list():           # extract the column headers into a suitable list format
    print(extracted_column_headers)

def get_column_data ():
    for row in column_data [1:]:        # [1:]: index from 1 and avoid adding an empty cell at the start of the csv
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in  row_data]  # use strip() for a better format 
        #print(individual_row_data)
        length = len(df)
        df.loc[length] = individual_row_data
    #print (df)
       
       

def dataframe_to_csv ():
    get_column_data()
    df.to_csv(r'Companies.csv',index=False, encoding='utf_8_sig')
    # using 'utf_8_sig' instead of 'utf-8' is better to handle special characters
    #print (df)

def main():
  dataframe_to_csv ()
  

if __name__ == "__main__":
    main()

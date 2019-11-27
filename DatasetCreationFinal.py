# importing csv module 
import csv 

# csv file name 
filename = "vijaynagardelivery_.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 


from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(r"C:\Users\Shweta Singh\Desktop\chromedriver.exe")

food=[] #List to store name of the product
links=[]
address=[]
name=[]

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = csvreader.next() 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

for row in rows[:]: 
    #link
    print(len(row))
    links.append(row[0])
    address.append(row[1])
    name.append(row[2])
    
    driver.get(row[0])
    content = driver.page_source

    soup = BeautifulSoup(content)
    a = soup.find('div', attrs={'class':'rv_highlights__section pr10'})

    if a is not None:
        f=a.find('div', attrs={'class':'fontsize13 ln18'})
        #print(f)
        food.append(f.text)
    elif a is None:
        food.append("")


df = pd.DataFrame({'Link':links, 'Address':address, 'Name':name,'Food Name':food}) 
df.to_csv('Fooddataset.csv', index=False, encoding='utf-8')

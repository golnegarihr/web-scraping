import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


page =requests.get('https://www.udacity.com/success')
soup=BeautifulSoup(page.text,'html.parser')\

temp=soup.select(".student-success-stories_card__2VEPv.border-card_card__22OJk img")
image_link=[image['src'] for image in temp]

temp=soup.select(".student-success-stories_card__2VEPv.border-card_card__22OJk h3")
name=[name.text for name in temp ]

temp=soup.select(".student-success-stories_card__2VEPv.border-card_card__22OJk p")
description=[desc.text for desc in temp]

temp=soup.select(".student-success-stories_card__2VEPv.border-card_card__22OJk h6")
company=[company.text for company in temp ]

for link in tqdm( image_link):
    file=requests.get(link)
    file_name=link.split('/')[-1]
    if '.' in file_name:
        file_type = '.' + file_name.split('.')[-1]
    else:
        file_type='.JPG'
    file_address=r'C:\' + str(image_link.index(link))+file_type
    with open(file_address,'wb')as f:
        f.write(file.content)
        
data=pd.DataFrame({
  'name':name,
  'Descrption':description,
    'company':company,
    'image link':image_link    
    
})       

data.to_csv(r'E:\Learning\FARADARS\web_crawler_python\my code\s09\data.csv',index=False,encoding='utf-8')

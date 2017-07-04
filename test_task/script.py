try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
links=pd.read_csv('wikipedia_links.csv',header=None)[0]
urls=[]
for i in range(len(links)):    
    page = urlopen(links[i]) 
    
    #Парсим страницу с помощью BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')
    
    #Получаем со страницы все теги с классом small
    urls_tag = soup.findAll(attrs={"rel":"nofollow"})
    
    urls.append(urls_tag[0]["href"])
new_links=pd.concat([pd.DataFrame(list(links),columns=['wikipedia_page']),pd.DataFrame(urls,columns=['website'])],axis=1)
new_links.to_csv('wikipedia_answers.csv',index=None)
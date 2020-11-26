import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL="https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page="
names=[]
auth=[]
xx=1
#for page in range(1,232):
for page in range(1,10):
    req=requests.get(URL+str(page)).text
    soup=bs(req, 'lxml')
    dd2 = soup.find_all("a", attrs={"class","bookTitle"})
    dd3 = soup.find_all("a", attrs={"class","authorName"})

    for i in dd2:
        names.append(i.text.strip())
    for i in dd3:
        auth.append(i.text)
    print(xx)
    xx+=1

df=pd.DataFrame(data={'Book': names, 'Author': auth},columns=["Book","Author"])
df


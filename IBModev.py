#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1 - Extracting Tesla Stock Data Using yfinance - Soru 1 - yfinance Kullanarak Tesla Hisse Senedi Verilerinin Çıkarılması 


# In[3]:


get_ipython().system('pip install yfinance')


# In[42]:


import yfinance as yf

# Tesla hisse senedi sembolü
symbol = 'TSLA'

# Veri çekilecek tarih aralığı
start_date = '2020-01-01'
end_date = '2021-01-01'

# yfinance üzerinden hisse senedi verilerini çekme
tesla_data = yf.download(symbol, start=start_date, end=end_date)

# Verileri gösterme
print(tesla_data)


# In[ ]:


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'


# In[43]:


print(tesla_data.head())


# In[ ]:


#Question 2 - Extracting Tesla Revenue Data Using Webscraping-Soru 2 - Webscraping Kullanarak Tesla Gelir Verilerinin Çıkarılması 


# In[44]:


get_ipython().system('pip install requests beautifulsoup4')


# In[46]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Veri çekmek istediğiniz URL
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

# URL'den HTML içeriğini çekme
response = requests.get(url)
html_content = response.content

# BeautifulSoup ile HTML içeriğini ayrıştırma
soup = BeautifulSoup(html_content, 'html.parser')

# HTML içeriğindeki tabloyu bulma
tables = soup.find_all('table')

# İlk bulunan tabloyu pandas DataFrame'e dönüştürme
df = pd.read_html(str(tables[0]))[0]

# Oluşturulan DataFrame'i gösterme
print(df.head())  # İlk beş satırı gösterir


# In[48]:


# tesla_revenue veri çerçevesinin son beş satırını görüntüleme
print(df.tail())


# In[ ]:


#Question 3 - Extracting GameStop Stock Data Using yfinance -Soru 3 -yfinance Kullanarak GameStop Hisse Senedi Verilerinin Çıkarılması 


# In[14]:


pip install yfinance


# In[21]:


import yfinance as yf

# GameStop hisse senedi sembolü
symbol = 'GME'

# Veri çekilecek tarih aralığı
start_date = '2020-01-01'
end_date = '2021-01-01'

# yfinance üzerinden hisse senedi verilerini çekme
gamestop_data = yf.download(symbol, start=start_date, end=end_date)

# Verileri gösterme
print(gamestop_data.head())  # İlk beş satırı görüntüleme


# In[ ]:


#Question 4 - Extracting GameStop Revenue Data Using Webscraping-Soru 4 - Webscraping Kullanarak GameStop Gelir Verilerini Çıkarma


# In[38]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Veri çekmek istediğiniz URL
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

# URL'den HTML içeriğini çekme
response = requests.get(url)
html_content = response.content

# BeautifulSoup ile HTML içeriğini ayrıştırma
soup = BeautifulSoup(html_content, 'html.parser')

# HTML içeriğindeki tabloyu bulma
tables = soup.find_all('table')

# İlk bulunan tabloyu pandas DataFrame'e dönüştürme
df = pd.read_html(str(tables[0]))[0]

# Oluşturulan DataFrame'i gösterme
print(df.head())  # İlk beş satırı gösterir



# In[39]:


# DataFrame'in son beş satırını gösterme
print(df.tail())


# In[ ]:





# In[ ]:


#Question 5 - Tesla Stock and Revenue Dashboard--Tesla Stok ve Gelir Gösterge Tablosu


# In[1]:


pip install yfinance matplotlib


# In[2]:


import yfinance as yf
import pandas as pd


# In[3]:


# GameStop hisse senedi sembolü
symbol = 'GME'

# Veri çekilecek tarih aralığı
start_date = '2021-01-01'
end_date = '2021-12-31'

# yfinance üzerinden hisse senedi verilerini çekme
gme_data = yf.download(symbol, start=start_date, end=end_date)


# In[4]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(gme_data.index, gme_data['Close'], label='GameStop Hisse Fiyatı', color='green')
plt.title('GameStop Hisse Senedi Fiyatı (2021)')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Question 6  GameStop Stock and Revenue Dashboard-GameStop Hisse Senedi ve Gelir Gösterge Tablosu


# In[56]:


pip install yfinance matplotlib


# In[57]:


import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(stock_data, title, ylabel, xlabel='Date'):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=f'{ylabel} Close Price')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# GameStop hisse senedi verilerini çekme
gamestop_stock = yf.download('GME', start='2020-01-01', end='2023-01-01')

# Hisse senedi kapanış fiyatlarının grafiğini çizme
make_graph(gamestop_stock, 'GameStop Stock Close Price (2020-2023)', 'GME')


# In[ ]:


#Sharing your Assignment Notebook  


# In[ ]:





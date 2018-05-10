
# coding: utf-8

# In[2]:


from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from bs4 import BeautifulSoup
import urllib.request as urllib


# In[3]:


SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', credentials = creds)


# In[4]:


SPREADSHEET_ID = '1GK5dPDOseZWUhfPB35_gOQFr9K017gpGlfE1OUGRePQ'
RANGE_NAME = 'A1:A3'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME, majorDimension='ROWS').execute()


# In[5]:


values = result.get('values', [])


# In[6]:


sizes = []


# In[7]:


for url in values:
    html = urllib.urlopen(url[0])
    soup = BeautifulSoup(html , 'html.parser')
    size_box = soup.find('select', attrs={'class': 'form-control size-drop-down'})
    options = size_box.find_all('option' , attrs = {'class': "swatch-item "})
    size = []
    for option in options:
        size.append(option.text)
    size = [','.join(size)]
    sizes.append(size)


# In[9]:


BODY = {"values": sizes}


# In[10]:


RANGE_NAME = 'B1:B3'

request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, valueInputOption='RAW', body=BODY)


# In[11]:


response = request.execute()


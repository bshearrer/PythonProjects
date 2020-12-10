import os
import requests
import getpass
import time
from urllib.parse import urljoin
from bs4 import BeautifulSoup

print("Type or Paste the Full URL > ")
url = input()

print("Input a folder name to store the PDF's > ")
folderName = input()

username = os.getlogin()    # Fetch username
folder_location = 'C:\\Users\\'+str(username)+'\\Desktop\\'+str(folderName)
if not os.path.exists(folder_location):
    os.mkdir(folder_location)

print("Downloading PDF's...")
response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)
        
print('\nScript is finished!\n')
time.sleep(1)
print('Files have been saved in '+folderName+' folder on your desktop.')
print("Exiting now...")
time.sleep(3)

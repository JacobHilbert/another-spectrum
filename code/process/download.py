import json
import os
import requests
import shutil
from bs4 import BeautifulSoup

base = "http://www.astrouw.edu.pl/ogle/ogle4/OCVS/{}/cep/"

for name in ["smc","lmc"]:
    base_url = base.format(name)
    soup = BeautifulSoup(requests.get(base_url).text,'html.parser')
    for a in soup.find_all("a"):
        href = a.get("href")
        if "." in href or href == "README":
            url = base_url+href
            local_filename = url[31:] # sepcific to the ogle page
            print(local_filename)
            os.makedirs(os.path.dirname(local_filename),exist_ok=True)
            with requests.get(url, stream=True) as r:
                with open(local_filename,"wb") as f:
                    shutil.copyfileobj(r.raw,f)

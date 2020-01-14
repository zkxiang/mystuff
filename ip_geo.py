import requests
from bs4 import BeautifulSoup
import socket
def get_geo_ip(raw_url):
    try:
        url0 = raw_url
        if '://' in raw_url:
            url0 = raw_url.split('://')[-1]
        ip = socket.gethostbyname(url0)
        url = 'http://ip.chinaz.com/' + ip
        tmp = requests.get(url).text
        soup = BeautifulSoup(tmp, 'lxml').find_all('span', class_='Whwtdhalf w50-0')
        return (ip, soup[-1].text)
    except:
        return None
pattern_ = r'&imgrefurl=[^&]*'
pattern__ = r'/imgres?imgurl='
import os
import re
import time 
import random 
import requests 
from bs4 import BeautifulSoup 
os.makedirs("link", exist_ok=True) 
 
pattern = r'-(\d{{3,4}})x(\d{{4}})' 
replacement = r'-\1x\2' 
start_page = 0 
end_page = 50 
total_img_count = 0 
final_page = end_page - 1 
start_resolution = 700 
end_resolution = 800 
ua_list = [ 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; LG; Optimus 7)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 800)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 900)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; SGH - i647)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; LG; Optimus 7)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 800)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 900)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; SGH - i647)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; LG; Optimus 7)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 800)', 
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 900)' 
] 
 
headers_list = [{'User - Agent': ua, 'Connection': 'close'} for ua in ua_list] 
 
for resolution in range(start_resolution, end_resolution + 1): 
    page_counter = start_page 
    current_page_img_count = 1  # 初始化为1，确保进入循环 
    while current_page_img_count > 0: 
        try: 
            headers = headers_list[random.randint(0, len(headers_list) - 1)] 
            url = f'https://google.com.hk/search?q=TV+%E3%82%A2%E3%83%8B%E3%83%A1++imagesize:{resolution}x1024+-eeo.today&tbm=isch&start={page_counter  * 20}&sa=N&lite=0&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg&tbs=qdr:d' #https://c.map987.us.kg/
            response = requests.get(url,  headers=headers, timeout=100) 
        except requests.exceptions.ConnectionError  as e: 
            print(f"Connection error: {e}. Retrying...") 
            time.sleep(5)   # 等待5秒后重试 
        soup = BeautifulSoup(response.text,  'html.parser')  
        print(soup)
        current_page_img_count = 0 
        with open(f'link/{resolution}.txt', 'a') as f: 
            for a in soup.find_all('a',  href=True): 
                if 'imgurl' in a['href']: 
                    link = re.sub(pattern_, "", a['href'])
                    link = link.replace(pattern__, "")
                    f.write(a['href']  + '\n') 
                    current_page_img_count += 1 
                    total_img_count += 1 
        print(f"page {page_counter} (resolution:{resolution}) - {current_page_img_count} images") 
        page_counter += 1 
print(f"Total images collected: {total_img_count}") 
 
 

# https://detski-magazin.com/385-bebenosene/page-2

from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator
import pandas as pd


item_list = []
# trans = Translator()
def func(page_num):
    
    url = f'https://detski-magazin.com/385-bebenosene/page-{page_num}?n=60'
    html_text = requests.get(url)

    soup = BeautifulSoup(html_text.text, 'lxml')
    products_list = soup.find('ul', class_='product_list grid row')

    for product in products_list:
        global prod_dis_expire, prod_dis, prod_old_price, prod_item2, prod_item1
        
        try:

                prod_name = product.find('div', class_='right-block').a['title']
                tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
                prod_url = product.find('div', class_='right-block').a['href']
                prod_dis = product.find('span', class_='percentage').text.replace('-', '')
                prod_dis_expire = product.find('span', class_='data_expiration').text
                trans_prod_expire = GoogleTranslator(target='en').translate(prod_dis_expire)
                prod_price = product.find('span', class_='price product-price').text.replace(' ', '')
                prod_old_price = product.find('span', class_='old-price product-price').text.replace(' ', '')

                prod_item2 = {
                    'Product Name' : tran_prod_name,
                    'Product URL' : prod_url,
                    'Product Discount': prod_dis,
                    'Product Discount Expiry':trans_prod_expire,
                    'Product Price': prod_price,
                    'Product Old Price': prod_old_price,
                }
                # print(f"Product Name: {tran_prod_name.strip()}")
                # print(f"Product URL: {prod_url.strip()}")
                # print(f"Product Discount: {prod_dis.strip()}")
                # print(f"Product Discount Expiry: {trans_prod_expire.strip()}")
                # print(f"Product Price: {prod_price.strip()}")
                # print(f"Product Old Price: {prod_old_price.strip()}\n")


        except:
            if prod_dis in product:
                prod_name = product.find('div', class_='right-block').a['title']
                tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
                prod_url = product.find('div', class_='right-block').a['href']
                prod_dis = product.find('span', class_='percentage').text.replace('-', '')
                prod_price = product.find('span', class_='price product-price').text.replace(' ', '')
                prod_old_price = product.find('span', class_='old-price product-price').text.replace(' ', '')

                prod_item1 = {
                    'Product Name' : tran_prod_name,
                    'Product URL' : prod_url,
                    'Product Discount': prod_dis,
                    'Product Price': prod_price,
                    'Product Old Price': prod_old_price,
                }
                # print(f"Product Name: {tran_prod_name.strip()}")
                # print(f"Product URL: {prod_url.strip()}")
                # print(f"Product Discount: {prod_dis.strip()}")
                # print(f"Product Price: {prod_price.strip()}")
                # print(f"Product Old Price: {prod_old_price.strip()}\n")
                

            else:

                prod_name = product.find('div', class_='right-block').a['title']
                tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
                prod_url = product.find('div', class_='right-block').a['href']
                prod_price = product.find('span', class_='price product-price').text.replace(' ', '')

                prod_item3 = {
                    'Product Name' : tran_prod_name,
                    'Product URL' : prod_url,
                    'Product Price': prod_price,
                }              
                # print(f"Product Name: {tran_prod_name.strip()}")
                # print(f"Product URL: {prod_url}")
                # print(f"Product Price: {prod_price.strip()}\n")
               
    i = [prod_item1, prod_item2, prod_item3]
    item_list.append(i)
    
       

for x in range(1, 2):
    func(x)

df = pd.DataFrame(item_list)
print(df) 
















# FOR OUT_OF_STOCK
# try:
#     if out_of_stock in product:
#         prod_name = product.find('div', class_='right-block').a['title']
#         tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
#         prod_url = product.find('div', class_='right-block').a['href']
#         prod_price = product.find('span', class_='price product-price').text.replace(' ', '')
#         out_of_stock = product.find('div', class_='not_available_label').p.tex
#         print(f"Product Name: {tran_prod_name.strip()}")
#         print(f"Product URL: {prod_url}")
#         print(f"Product Price: {prod_price.strip()}\n")
#         print(f"Out of Stock: {out_of_stock}\n")

# except:
#         pass
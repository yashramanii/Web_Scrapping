from os import write
from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator
import csv
# import pandas as pd
item_list = []
# trans = Translator()
def func(page_num):
    url = f'https://detski-magazin.com/5-detski-kolicki/page-{page_num}?n=60'
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')
    products_list = soup.find('ul', class_='product_list grid row')


    for product in products_list:
        # NAME
        try:
            prod_name = product.find('div', class_='right-block').a['title']
            tran_prod_name = GoogleTranslator(target='en').translate(prod_name)

            # item_name = {
            #     'Item Name': tran_prod_name
            # }

            # print(f"Product Name: {tran_prod_name.strip()}")
        except:
            tran_prod_name = None
        
        # URL
        try:
            prod_url = product.find('div', class_='right-block').a['href']

            # item_url = {
            #     'Item URL': prod_url
            # }

            # print(f"Product URL: {prod_url}")
        except:
            prod_url = None
        
        # DISCOUNT
        try:
            prod_dis = product.find('span', class_='percentage').text.replace('-', '')

            # item_dis = {
            #     'Item Discount': prod_dis
            # }

            # print(f"Product Discount: {prod_dis}")
        except:
            prod_dis = None
        
        # DISCOUNT EXPIRE
        try:
            prod_dis_expire = product.find('span', class_='data_expiration').text
            trans_prod_expire = GoogleTranslator(target='en').translate(prod_dis_expire)

            # item_dis_expiry = {
            #     'Item Dis Exp': trans_prod_expire
            # }

            # print(f"Product Discount Expiry: {trans_prod_expire.strip()}")
        except:
            trans_prod_expire = None
        
        # PRICE
        try:
            prod_price = product.find('span', class_='price product-price').text.replace(' ', '')

            # item_price = {
            #     'Item Price': prod_price
            # }

            # print(f"Product New Price: {prod_price}")
        except:
            prod_price = None
        
        # OLD PRICE
        try:
            prod_old_price = product.find('span', class_='old-price product-price').text.replace(' ', '')

            # item_old_price = {
            #     'Item Old Price': prod_old_price
            # }

            # print(f"Product Old Price: {prod_old_price}\n")
        except:
            prod_old_price = None

        # i = [tran_prod_name, prod_url, prod_price, prod_dis, trans_prod_expire, prod_old_price]
        i ={
            'Product Name': tran_prod_name,
            'Product URL': prod_url,
            'Product Discount': prod_dis,
            'Product Discount Expiry': trans_prod_expire,
            'Product Price': prod_price,
            'Product Old Price': prod_old_price
        }
        item_list.append(i)
        # with open('ecom2_try_dict2.csv', 'w',newline='') as f:
            # writer = csv.writer(f)

            # for d in item_list:
            #     writer.writerow(d)

        with open('ecom2_try_dict_all.csv', 'w', newline='') as f:
            fieldnames = ['Product Name', 'Product URL', 'Product Discount', 'Product Discount Expiry', 'Product Price', 'Product Old Price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for d in item_list:
                writer.writerow(d)

        

for x in range(1, 37):
    func(x)


# df = pd.DataFrame(item_list)
# op = df.to_csv('op.csv')
# print(df)

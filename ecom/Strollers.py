from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator
from urllib.parse import urljoin


url = 'https://detski-magazin.com/5-detski-kolicki/'

def func():
# while True:
    
    # url = f'https://detski-magazin.com/5-detski-kolicki/page-{page_num}?n=60'

    # url = 'https://detski-magazin.com/5-detski-kolicki/'
    html_text = requests.get(url)

    soup = BeautifulSoup(html_text.text, 'lxml')
    products_list = soup.find('ul', class_='product_list grid row')

    
    for product in products_list:
        global prod_dis_expire, prod_dis, prod_old_price

        # try:
        #     prod_dis_expire = product.find('span', class_='data_expiration').text
        #     prod_name = product.find('div', class_='right-block').a['title']
        #     tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
        #     prod_url = product.find('div', class_='right-block').a['href']
        #     prod_dis = product.find('span', class_='percentage').text.replace('-', '')
        #     trans_prod_expire = GoogleTranslator(target='en').translate(prod_dis_expire)
        #     prod_price = product.find('span', class_='price product-price').text.replace(' ', '')
        #     prod_old_price = product.find('span', class_='old-price product-price').text.replace(' ', '')

        #     print(f"Product Name: {tran_prod_name.strip()}")
        #     print(f"Product URL: {prod_url.strip()}")
        #     print(f"Product Discount: {prod_dis.strip()}")
        #     print(f"Product Discount Expiry: {trans_prod_expire.strip()}")
        #     print(f"Product Price: {prod_price.strip()}")
        #     print(f"Product Old Price: {prod_old_price.strip()}\n")

        # except:
            
            # if prod_dis_expire not in product:
            #     if prod_dis and prod_old_price not in product:
            #         prod_name = product.find('div', class_='right-block').a['title']
            #         tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
            #         prod_url = product.find('div', class_='right-block').a['href']
            #         prod_price = product.find('span', class_='price product-price').text.replace(' ', '')

            #         print(f"Product Name: {tran_prod_name.strip()}")
            #         print(f"Product URL: {prod_url.strip()}")
            #         print(f"Product Price: {prod_price.strip()}\n")

            #     else:
            #         prod_name = product.find('div', class_='right-block').a['title']
            #         tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
            #         prod_url = product.find('div', class_='right-block').a['href']
            #         prod_dis = product.find('span', class_='percentage').text.replace('-', '')
            #         prod_price = product.find('span', class_='price product-price').text.replace(' ', '')
            #         prod_old_price = product.find('span', class_='old-price product-price').text.replace(' ', '')
            #         # trans_prod_expire = None

            #         print(f"Product Name: {tran_prod_name.strip()}")
            #         print(f"Product URL: {prod_url.strip()}")
            #         print(f"Product Discount: {prod_dis.strip()}")
            #         print(f"Product Price: {prod_price.strip()}")
            #         print(f"Product Old Price: {prod_old_price.strip()}\n")
            #         # print(f"Product Discount Expiry: {trans_prod_expire.strip()}")
            # else:
            #     prod_name = product.find('div', class_='right-block').a['title']
            #     tran_prod_name = GoogleTranslator(target='en').translate(prod_name)
            #     prod_url = product.find('div', class_='right-block').a['href']
            #     prod_price = product.find('span', class_='price product-price').text.replace(' ', '')
            #     print(f"Product Name: {tran_prod_name.strip()}")
            #     print(f"Product URL: {prod_url.strip()}")
            #     print(f"Product Price: {prod_price.strip()}\n")
    
        next_link = soup.find('li',id='pagination_next').find('a',href=True)
    
        # if next_link is not None:
            
        # else: 
        #     pass

    print(next_link)

# for x in range(1, 2):
#     func(x)


func()
















# def next():
#      next_link = soup.find('li',id='pagination_next').find('a',href=True)

#     if next_link is not None:
#         func(products_list, next_link['href'])
#     else: pass






# FOR IMAGES
# prod_image = products_list.find('div', class_='product-image-container')
# prod_image = products_list.find('a', class_='product_image_link')
# print(prod_image)
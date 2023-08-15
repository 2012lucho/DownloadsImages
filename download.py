from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import random

query = 'Kitty'

driver = webdriver.Firefox()
driver.get("https://google.com")


elem = driver.find_element(By.TAG_NAME, "textarea")
elem.send_keys(query)
elem.send_keys(Keys.RETURN)

sleep(4)
spans = driver.find_elements(By.TAG_NAME, "span")

btn_img_encontrado = False

for span in spans:
    try:
        if (span.text == 'Imágenes'):
            span.click()
            btn_img_encontrado = True
    except:
        print("An exception occurred")


lista_miniaturas = []
if (btn_img_encontrado):
    print('Btn de imagen encontrado')
    sleep(random.randint(3, 5))
    print('Haciendo scroll')
    
    scroll_count = random.randint(2000, 3000)
    cont = 0
    positiony = 0
    while ( cont < scroll_count):
        positiony = positiony + random.randint(5, 20)
        sleep( random.randint(0, 100) / 1000 )
        driver.execute_script("window.scrollTo(0, "+str(positiony)+")")
        cont = cont + 1

    print('Guardando miniaturas')
    sleep(3)
    imgs_ = driver.find_elements(By.TAG_NAME, "img")
    for img in imgs_:
        with open('./miniaturas.csv', 'a', newline='') as f:
            toCSV = ['base64']
            w = csv.DictWriter(f, toCSV, delimiter='|')
            try:
                w.writerow( {
                    'base64': img.get_attribute('src'), 
                })
            except:
                print("An exception occurred")

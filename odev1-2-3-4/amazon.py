from _ast import Assert
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("https://www.amazon.com/")
print browser.title
try:
    assert 'Amazon.com'  in browser.title
    print ('test basarili')
except Exception as e:
    print ('test basarisiz',format(e))

time.sleep(3)


giris_yap= browser.find_element_by_xpath("//*[@id='nav-signin-tooltip']/a/span")
giris_yap.click()
time.sleep(3)
username = browser.find_element_by_xpath("//*[@id='ap_email']")
username.send_keys("bikuqaj@getnada.com")
devam=browser.find_element_by_xpath("//*[@id='continue']")
devam.click()
time.sleep(2)
password=browser.find_element_by_xpath("//*[@id='ap_password']")
password.send_keys("987654")
giris= browser.find_element_by_xpath("//*[@id='signInSubmit']")
giris.click()
searchArea=browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
searchButton=browser.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input")

searchArea.send_keys("Iphone")
searchButton.click()
print browser.title
try:

    assert 'Amazon.com: iphone' in browser.title
    print ('test basarili, iphone araması icin')
except Exception as e:
    print ('test basarisiz!!',format(e))




time.sleep(3)





browser.get("https://www.amazon.com/s?k=iphone&page=2&qid=1599164711&ref=sr_pg_2")
try:


    page = browser.find_elements_by_partial_link_text('2')
    print ('test basarili iphone arama icin 2. sayfada')


except Exception as e:
    print('test basarisiz', format(e))

time.sleep(3)


urun=browser.find_element_by_xpath("//*[@id='s-results-list-atf']/child::li[3]/div/div/div/div[1]")
urun.click()
addwish=browser.find_element_by_xpath("//*[@id='wishListMainButton']/span")
addwish.click()

time.sleep(1)
liste=browser.find_element_by_xpath("//*[@id='WLHUC_viewlist']")
liste.click()
print("ekleme basarili")

time.sleep(3)
delete=browser.find_element_by_xpath("//*[@id='itemAction_INJ2HBBIZ298V']/div/div/div/span")
delete.click()
print("silme basarili")
time.sleep(3)

browser.close()

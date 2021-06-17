from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

browser = webdriver.Chrome()


def login(username, password):
    url = "http://fb.dut.udn.vn/PageDangNhap.aspx"
    browser.get(url)
    btnUser = browser.find_element_by_xpath("/html/body/div[6]/div/form/table/tbody/tr[2]/td[2]/input")
    btnUser.send_keys(username)
    btnPass = browser.find_element_by_xpath("/html/body/div[6]/div/form/table/tbody/tr[3]/td[2]/input")
    btnPass.send_keys(password)
    browser.find_element_by_id("QLTH_btnLogin").click()

login("----------", "-----------")
sleep(1)

list = open('links.txt')
links = list.readlines()
linkId = 0

while linkId < len(links) + 1:
    url  = links[linkId]
    browser.get(url)
    id = 1
    sleep(0.5)
    while id < 10:
        btn = browser.find_element_by_id(f"R18LT0{id}_0")
        btn.click()
        id +=1
    while id < 29:
        btn = browser.find_element_by_id(f"R18LT{id}_0")
        btn.click()
        id +=1
    sleep(0.5)
    while id < 33:
        fb = browser.find_element_by_name(f"txt18LT{id}")
        fb.send_keys("Chương trình giảng dạy của thầy cô rất tốt ! ")
        id +=1
    while id < 37:
        btn = browser.find_element_by_id(f"R18LT{id}_0")
        btn.click()
        id +=1
    btnSubmit = browser.find_element_by_xpath("/html/body/div[6]/div/form/div[3]/div/div[4]/div[3]/input")
    btnSubmit.click()
    sleep(3)
    btnEnd = browser.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]/span")
    btnEnd.click()
    sleep(1)
    linkId += 1

# while True:
#     url  = 'http://fb.dut.udn.vn/PageDanhGiaCA.aspx?Loai=CK&LopHP=122218020201787'
#     browser.get(url)
#     id = 1
#     while id < 10:
#         btn = browser.find_element_by_id(f"R18TH0{id}_0")
#         btn.click()
#         id +=1
#     while id < 29:
#         btn = browser.find_element_by_id(f"R18TH{id}_0")
#         btn.click()
#         id +=1
#     while id < 33:
#         fb = browser.find_element_by_name(f"txt18TH{id}")
#         fb.send_keys("Chương trình giảng dạy của thầy cô rất tốt ! ")
#         id +=1
#     while id < 37:
#         btn = browser.find_element_by_id(f"R18TH{id}_0")
#         btn.click()
#         id +=1
#     btnSubmit = browser.find_element_by_xpath("/html/body/div[6]/div/form/div[3]/div/div[4]/div[3]/input")
#     btnSubmit.click()
#     sleep(5)
#     btnEnd = browser.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]/span")
#     btnEnd.click()
#     sleep(1)
#     linkId += 1

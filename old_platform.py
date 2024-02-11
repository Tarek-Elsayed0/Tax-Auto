# import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from math import ceil
import pandas as pd

# get_data
# company_mail = input("User Name: ").strip()
# company_pass = input("Password: ").strip()
# tax_number = input("Tax Reg. Number: ").strip()
company_mail = "557621895_0"
company_pass = "Rinad@1234"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# browser = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome(options=chrome_options)
# action = ActionChains(browser)
browser.get("https://eservice.incometax.gov.eg/etax")
browser.maximize_window()
wait = WebDriverWait(browser, 90)
sleep(2)

browser.find_element(by="xpath", value="//button[@class='btn btn-login']").click()

sleep(1)
browser.find_element(by="xpath", value='//input[@id="userNameInput"]').send_keys(company_mail)
browser.find_element(by="xpath", value='//input[@id="userPwdInput"]').send_keys(company_pass)
sleep(1)
browser.find_element(by="xpath", value='//button[@id="btnSubmitLogin"]').click()
sleep(1)
try:
    browser.find_element(by="xpath", value='//body').send_keys(Keys.ENTER)
except:
    pass
sleep(1)
browser.find_element(by="xpath", value='//li[@id="VATLink"]').click()
sleep(1)
browser.find_element(by="xpath", value='//li[@id="VATLink"]//a[text()="عرض الفواتير"]').click()

# id="DeDate"
# 2021, 
for year in range(2019, 2024):
    
    sleep(1)
    for month in range(12):
        def select_month():
            sleep(5)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="DeDate"]')))
            browser.find_element(by="xpath", value='//input[@id="DeDate"]').click()
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//select[@data-handler="selectYear"]')))
            browser.find_element(by="xpath", value='//select[@data-handler="selectYear"]').click()
            sleep(1)
            browser.find_element(by="xpath", value=f'//option[@value="{year}"]').click()
            browser.find_element(by="xpath", value='//select[@data-handler="selectMonth"]').click()
            sleep(1)

            browser.find_element(by="xpath", value=f'//select[@class="ui-datepicker-month"]//option[@value="{month}"]').click()
            sleep(1)
            browser.find_element(by="xpath", value='//div[@class="ui-datepicker-buttonpane ui-widget-content"]//button[text()="Done"]').click()
            # id="SalesFileRdioBtn" PurchasesFileRdioBtn
            sleep(1)
            browser.find_element(by="xpath", value='//input[@id="PurchasesFileRdioBtn"]').click()
            sleep(1)
            browser.find_element(by="xpath", value='//input[@id="BtnSearch"]').click()
            sleep(0.5)
            # class="k-loading-image"
            # wait.until(EC.invisibility_of_element_located((By.XPATH, 'class="k-loading-image"')))
            wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="blockUI"]')))
            wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="k-loading-image"]')))


        
        try:
            sleep(2)
            select_month()
            sleep(2)
        except:
            # wait.until(EC.invisibility_of_element_located((By.XPATH, 'class="k-loading-image"')))
            # wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="blockUI"]')))
            # wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="k-loading-image"]')))
            print("error in selecting month")
            browser.refresh()
            sleep(2)
            select_month()
            sleep(2)
            print("selected in the 2nd time")

        wait.until(EC.invisibility_of_element_located((By.XPATH, '//table[@class="k-selectable"]//tr//td[@colspan="9"]')))
        # wait.until(EC.text_to_be_present_in_element((By.XPATH, '//table[@class="k-selectable"]//tr//td[@colspan="9"]'), ))
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="k-pager-info k-label"]')))
        fwateer_num = browser.find_element(by="xpath", value='//span[@class="k-pager-info k-label"]').text
        # fwateer_num = int(fwateer_num.split(" ")[-2])
        try:
            fwateer_num = int(fwateer_num.split(" ")[-2])
        except:
            with open("Info.txt", "a") as file:
                file.write(f"Error when search for fwateers {month}/{year}")
                file.write("\n")
            # print(f"Error when search for fwateers {month}/{year}")
            continue
        sleep(1)
        # fwateer_num = browser.find_element(by="xpath", value='//span[@class="k-dropdown-wrap k-state-default"]').click()
        # sleep(1)
        pages = ceil(fwateer_num/10)
        

        # loop
        # //ul[@class="k-pager-numbers k-reset"]/li/a
        # count = 0
        for page in range(1, pages+1):
            def select_page():
                sleep(5)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="k-pager-info k-label"]')))
                sleep(1)
                wait.until(EC.element_to_be_clickable((By.XPATH, f'//a[@data-page="{page}"]')))
                # wait.until(EC.visibility_of_element_located((By.XPATH, f'//a[@data-page="{count}"]')))
                sleep(1)
                browser.find_element(by="xpath", value=f'//a[@data-page="{page}"]').click()
                sleep(1)
                wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="blockUI"]')))
                wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="k-loading-image"]')))
                sleep(0.5)
                # role="treegrid"
                table = browser.find_element(by='xpath', value='//table[@role="treegrid"]').get_attribute('outerHTML')
                df = pd.read_html(table)[0]
                sleep(0.5)
                # df = pd.DataFrame(df)
                df.to_csv(f'{year}_{month+1}_{page}.csv',encoding='utf-8-sig')
                print(df)
                sleep(5)
            try:
                sleep(2)
                select_page()
                sleep(2)
            except:
                sleep(2)
                select_page()
                sleep(2)
                

            # //a[@data-page="1"]

        # sleep(2)
        # try:
        #     i.click()
        # except:
        #     sleep(2)
        #     i.click()
# os.system("shutdown /s /t 1")








# try:
#     alert = browser.switch_to_alert()
#     alert.accept()
#     print("alert accepted")
# except:
#     print("no alert")
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from math import ceil


def main():
    # get_data
    # company_mail = input("User Name: ").strip()
    # company_pass = input("Password: ").strip()
    # tax_number = input("Tax Reg. Number: ").strip()

    def wait_input_date():
        input("Did you entered starting date: ")
    company_mail = "feras_Tex@hotmail.com"
    company_pass = "Gharibo.2021"
    # Received || Submitted
    I_direction = "Submitted"
    # tax_number = "225629844"
    start_date = "01/10/2023"
    end_date = "31/10/2023"


    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    
    # browser = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=chrome_options)
    # action = ActionChains(browser)

    browser.get("https://invoicing.eta.gov.eg")
    browser.maximize_window()
    wait = WebDriverWait(browser, 120)
    sleep(2)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='login-page']")))
    print("Page loaded successfully!")

    browser.find_element(by="xpath", value="//input[@id='email']").send_keys(company_mail)
    browser.find_element(by="xpath", value="//input[@id='Password']").send_keys(company_pass)
    sleep(2)
    browser.find_element(by="xpath", value="//button[@id='submit']").click()


    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='layout-container']")))

    # browser.find_element(by="xpath", value="//div[@class='eta-NavLinkGroup']").click()
    # sleep(0.5)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//div/a[@id='recentDocuments']")))
    # browser.find_element(by="xpath", value="//div/a[@id='recentDocuments']").click()
    browser.get("https://invoicing.eta.gov.eg/documents")

    # Search button
    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@name='Search All Documents']")))
    browser.find_element(by="xpath", value="//button[@name='Search All Documents']").click()

    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='showFilterButton']/span")))
    browser.find_element(by="xpath", value="//button[@id='showFilterButton']/span").click()
    # Filter
    sleep(0.5)
    browser.find_elements(by="xpath", value="//div[@class='dropDownGrid']//span")[0].click()
    sleep(0.5)
    # Received || Submitted
    browser.find_element(by="xpath", value=f'//button[@role="option"]//span[text()="{I_direction}"]').click()
    # Type
    # 4
    # //div[@class='dropDownGrid']//span
    # sleep(1)
    # browser.find_elements(by="xpath", value="//div[@class='dropDownGrid']//span")[2].click()
    # sleep(0.5)
    # browser.find_element(by="xpath", value='//button[@role="option"]//span[text()="C"]').click()

    sleep(0.5)
    browser.find_elements(by="xpath", value="//div[@class='dropDownGrid']//span")[4].click()
    sleep(0.5)
    browser.find_element(by="xpath", value='//button[@role="option"]//span[text()="Valid"]').click()

    # first date input
    sleep(1)
    browser.find_elements(by="xpath", value="//input[@role='combobox']")[0].send_keys(start_date)
    # wait_input_date()

    # second date input
    sleep(1)
    browser.find_elements(by="xpath", value="//input[@role='combobox']")[1].send_keys(end_date)

    # third date input
    # sleep(1)
    # browser.find_elements(by="xpath", value="//input[@role='combobox']")[2].send_keys(start_date)
    # wait_input_date()

    # fourth date input
    # sleep(1)
    # browser.find_elements(by="xpath", value="//input[@role='combobox']")[3].send_keys(end_date)

    sleep(1)
    browser.find_element(by="xpath", value="//div[@class='Filters']").click()

    # Apply Filter
    sleep(1)
    browser.find_elements(by="xpath", value="//div[@class='btns-filteration']/button")[1].click()

    wait.until_not(EC.visibility_of_element_located((By.XPATH, "//div[@class='Filters']")))

    # Switch to arabic
    sleep(1)
    browser.find_elements(by="xpath", value="//div[@class='eta-languageSelector']/button")[1].click()

    # # //div[@role='combobox']
    # # filter page number
    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='combobox']")))
    browser.find_element(by="xpath", value="//div[@role='combobox']").click()
    
    # For displaying 50 Invoice 1
    # For displaying 50 Invoice 2
    # For displaying 50 Invoice 3
    browser.find_element(by="xpath", value="//button[@data-index='1']").click()

    # Each row
    # //div[@class="ms-List-cell"]//div[@data-automationid="DetailsRowFields"]

    # company_tax_number = tax_number
    sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='eta-pagination-totalrecordCount']/label")))
    invoices_number = browser.find_element(by="xpath", value='//div[@class="eta-pagination-totalrecordCount"]/label').text
    invoices_number = int(invoices_number.split(" ")[-1])
    
    def loop_in_invoices():
        for row_number in range(0, invoices_number):
            rows = browser.find_elements(by='xpath', value='//div[@class="ms-List-cell"]')
            sleep(0.7)
            browser.execute_script("arguments[0].scrollIntoView();", rows[row_number])
            try:
                if browser.find_element(by="xpath", value=f'//div[@data-list-index="{row_number}"]//i[@data-icon-name="Completed"]'):

                    invoice_name = browser.find_element(by="xpath", value=f'//div[@data-list-index="{row_number}"]//a[@class="griCellTitle"]').text
                    with open("Check.txt", "r") as file:
                        existing_invoices = file.readlines()
                        if f"{invoice_name}\n" in existing_invoices:
                            continue
                    # print(f'Invoice Name: {invoice_name}')
                    internal_number = browser.find_elements(by='xpath', value=f'//div[@data-list-index="{row_number}"]//div[@data-automationid="DetailsRowFields"]//div[@class="griCellSubTitle"]')[0].text
                    # print(f'Invoice number: {internal_number}')
                    issuer_number = browser.find_elements(by='xpath', value=f'//div[@data-list-index="{row_number}"]//div[@data-automationid="DetailsRowFields"]//div[@class="griCellSubTitle"]')[4].text
                    # print(f'Issuer Number: {issuer_number}')
                    # reciever_number = rows[row_number].find_elements(by='xpath', value=f'//div[@data-list-index="{row_number}"]//div[@data-automationid="DetailsRowFields"]//div[@class="griCellSubTitle"]')[5].text
                    reciever_number = browser.find_elements(by='xpath', value=f'//div[@data-list-index="{row_number}"]//div[@data-automationid="DetailsRowFields"]//div[@class="griCellSubTitle"]')[5].text
                    # print(f'Reciever Number: {reciever_number}')

                    # split name
                    try:
                        internal_number = internal_number.split("/")[-1]
                    except:
                        pass
                    # print(issuer_number)
                    def go_to_download():
                        btn = browser.find_element(by='xpath', value=f'//div[@data-list-index="{row_number}"]//div[@data-automationid="DetailsRowFields"]//button')
                        sleep(1)
                        browser.execute_script("arguments[0].scrollIntoView();", btn)
                        sleep(0.5)
                        sleep(1)
                        btn.click()
                        sleep(1)
                        browser.find_element(by="xpath", value="//ul/li/button//span[text()='تحميل كـ']").click()
                        sleep(1)
                        browser.find_element(by="xpath", value="//ul/li/button//span[text()='PDF']").click()
                        sleep(8)
                    try:
                        go_to_download()
                        ##############################################################   
                    except:
                        print("Error in download")
                        print("Try again....")
                        go_to_download()
                        
                    try:
                        if os.path.isfile(f"C:/Users/Tarek/Downloads/{invoice_name}.pdf"):
                            # print(invoice_name)
                            with open("Check.txt", "a") as f:
                                # print(invoice_name)
                                f.write(invoice_name)
                                f.write("\n")
                            print(invoice_name)
                            direc = "C:/Users/Tarek/Downloads/"
                            old_file_name = f"{invoice_name}.pdf"
                            old_name = os.path.join(direc, old_file_name)
                            new_file_name = f"{internal_number}.pdf"
                            if I_direction == "Submitted":
                                new_name = os.path.join(direc, f"{' مبيعات '+new_file_name}")
                                os.rename(old_name, new_name)
                            else:
                                new_name = os.path.join(direc, f"{' مشتريات '+new_file_name}")
                                os.rename(old_name, new_name)
                                # os.rename(f"C:/Users/Tarek/Downloads/{invoice_name}.pdf", f"C:/Users/Tarek/Downloads/{' مشتريات '+new_name}")
                            sleep(4)
                            print("file renamed")
                        else:
                            sleep(10)
                            if I_direction == "Submitted":
                                os.rename(f"C:/Users/Tarek/Downloads/{old_name}", f"C:/Users/Tarek/Downloads/{' مبيعات '+new_name}")
                            else:
                                os.rename(f"C:/Users/Tarek/Downloads/{invoice_name}.pdf", f"C:/Users/Tarek/Downloads/{' مشتريات '+new_name}")
                            sleep(5)
                            print("file renamed")
    
                    except FileNotFoundError:
                        print("fileError!")
                        print(f"Error in {invoice_name}")
                        print(internal_number)
                        continue
                    except:
                        print(f"Error in {invoice_name}")
                        print(internal_number)
                        continue
            except:
                continue

    print(invoices_number)
    pages = ceil(invoices_number/20)

    if pages > 1:
        for page in range(1, pages+1):
            print(f"page: {page}")
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.XPATH, f'//div[@class="eta-pagination-pageselector"]//button//span[@data-automationid="splitbuttonprimary"]//span[text()="{page}"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@class="eta-pagination-pageselector"]//button//span[@data-automationid="splitbuttonprimary"]//span[text()="{page}"]')))
            sleep(1)
            browser.find_element(by="xpath", value=f'//div[@class="eta-pagination-pageselector"]//button//span[@data-automationid="splitbuttonprimary"]//span[text()="{page}"]').click()
            sleep(0.5)
            try:
                loop_in_invoices()
            except IndexError:
                print("Index reached")
    else:
        loop_in_invoices()

    print("Done!")
    print("Closing Browser........")
    browser.quit()
    # with open("Check.txt", "a") as f:
    #     # print(invoice_name)
    #     f.write(dir)
    #     f.write("\n")
        # os.system("shutdown /s /t 1")
main()

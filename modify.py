import csv
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
# from math import ceil
# import pandas as pd
# from selenium.webdriver.common.proxy import *

# get_data
# company_mail = input("User Name: ").strip()
# company_pass = input("Password: ").strip()
# tax_number = input("Tax Reg. Number: ").strip()
company_mail = "313555699_0"
company_pass = "Edafat_1"
tax_number = "225629844"
start_date = "01/07/2023"
end_date = "31/07/2023"


chrome_options = Options()

# proxy_server_url = "192.168.1.20"
# chrome_options.add_argument(f'--proxy-server={proxy_server_url}')

chrome_options.add_experimental_option("detach", True)

# browser = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome(options=chrome_options)
# action = ActionChains(browser)
browser.get("https://eservice.incometax.gov.eg/etax")
browser.maximize_window()
wait = WebDriverWait(browser, 40)
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
browser.find_element(by="xpath", value='//li[@id="WithholdingLink"]').click()
sleep(1)
browser.find_element(by="xpath", value='//li[@id="WithholdingLink"]//a[text()="نموذج 41 "]').click()
sleep(1)
browser.find_element(by="xpath", value='//*[@id="WithholdingLink"]/ul/li[1]/ul/li[1]/a').click()
sleep(1)
# loop inside the file

# # send tax_num
# # //input[@id="financierTaxIdLbl"]
# sleep(1)
# browser.find_element(by="xpath", value='//input[@id="financierTaxIdLbl"]').send_keys("557968062")
# sleep(1)

# # click drop down
# # //select[@id="FileNumberList"]
# browser.find_element(by="xpath", value='//select[@id="FileNumberList"]').click()
# sleep(1)

# # click option [1]
# # //select[@id="FileNumberList"]/option
# browser.find_elements(by="xpath", value='//select[@id="FileNumberList"]/option')[1].click()
# sleep(1)

# # copy text
# # //input[@id="financierNameLbl"]
# supplier = browser.find_element(by="xpath", value='//input[@id="financierNameLbl"]').get_attribute('value')
# sleep(0.5)
# print(supplier)

tax_nums = {'557968062': 'اسلام السيد ابراهيم محمد فوده', '553016725': 'احمد اسامه احمد رشدي طه وشريكته', '200672533': 'القصواء للتجاره والتوريدات', 
'670010316': 'شاديباك للعبوات الدوائيه والغذائيه', '613542207': 'شركه الفا لتحويل الورق', '284266477': 'مايكل عادل صليب روفائيل', '347159303': 'تامر حسن فرحات حسن', '713467002': 'ايهاب محمد طاهر السعيد', '100078389': 'شركه الصناعات الغذائيه العربيه دومتي', '225267470': 'الياس ابراهيم الياس و شركاه', '440670470': 'ربيع عبدالحليم معوض وشريكه', '728800985': 'علاءالدين يوسف عفيفي', '310181356': 'كارم محمود بدر ابوكريشه', '538509228': 'شركه فرست للاستشارات والبيئه والمعايره', '555214966': 'محمود محمد ابوالمعاطي السيد وشركاه', '316103756': 'مشرقي رمسيس مشرقي وشركاه', '381434664': 'رمضان احمد محمد علي وشريكه', '249740885': 'حسين محمد حسين خطاب وشريكه', '205059309': 'محمد احمد عبدالرحمن وشريكه', '567832090': 'ايمن بولس بشري بولس', '205788394': 'احمد عبدالونيس احمد دعبس', '582347084': 'الخليج للكرتون', '449950549': 'طارق عبدالمنعم احمد السروري وشركاه', '509220363': 'رانيا ملاك لطيف ابراهيم', '587172282': 'محمد عبدالله طه علي سويدان', '533438942': 'زكريا محمود محمود عبدالمجيد وشريكه', '209801778': 'شركه مصر اكتوبر للصناعات الغذائيه', '564251739': 'بيتي فود', '554848856': 'ريتش فوود للصناعات الغذائيه', '472872567': 'سحر عبدالمنعم عبدالله وشركائها', '286664267': 'فوكس للصناعات الغذائيه', '381274675': 'عوض عطا نسيم رزق', '625655613': 'يوسف علاءالدين يوسف عفيفي', '450576507': 'كريم يحيي ابراهيم علي', '274039540': 'محمد علم الدين احمد حسين', '528540459': 'عاليه عاشور محمد محمود وشريكتها دعاء عاشور محمد', '721001424': 'ايمن محمد مصطفي محمد', '376402253': 'عمرو يحيي زكريا عبدالعال', '646133047': 'محمود عاشور حسن محمود', '463840933': 'سعد احمد سعد محمد', '347453724': 'علاء رمضان خميس سليمان', '667418342': 'مني محمد محمد محمود عبدالوهاب', '628930216': 'تامر عادل علي سيد', '555550532': 'محمد جمال محمد علي', '535657420': 'ديماس للاستثمارالصناعي', '379494906': 'نهاد صلاح عرفه علي', '261983717': 'شركه المصريه للحلول التكنولوجيه المتكامله', '463507126': 'جمعيه خير مصر عنها احمد جمعه عبدالنعيم', '633777897': 'مدارات للنقل داخلي البري', '325057729': 'رمضان محمد محمد خضر', '513890777': 'رمضان جمال صديق عبدالصالحين', '494333006': 'محمد احمد محمد احمد وشريكه', '552468649': 'جورج جميل فهمي اقلاديوس', '479918899': 'بنده العالميه لتجاره التجزئه مصر', '721049249': 'مصطفي رضوان مصطفي مصطفي السعدي', '508475244': 'شركه البيرين للاستيراد والتصدير والتجاره والتوزيع', '215533240': 'شركه سبينيس ايجيبت', '616447515': 'رجب رشدي لبيب عبدالجواد', '207964890': 'رزق سعيد حامد بدر سعيد', '205850375': 'خالد احمد فرغلي حسنين', '562570985': 'محمد علي المتولي علي', '342651390': 'علاء شعبان بدر وشريك', '506339424': 'احمد علاء احمد توفيق ابوالسعود بولايه والده', '680168923': 'جنا علاء احمد توفيق', '679459197': 'ورثه محمد انور محمد البحقيري', '248925350': 'فتحي حامد شربيني حامد قلاس وشركاه', '416328636': 'امل جمال الدين محمد وشريكتها', '209903759': 'سمير حسني عمر منصور', '575019050': 'محمد مصطفي السيد خلاف', '579246078': 'خالد السيد جميل محمد', '735834253': 'قبرص لمنح الشهادات مصر', '616443463': 'عبدالله سالم فوزي معوض وشريكه', '465143709': 'محمد علي سليمان ابراهيم', '450224643': 'نها عبدالهادي امين حسين', '274169193': 'شركه يونيتد جروسرز', '567786188': 'فتح الله بيت الجمله للتجاره والتوريدات', '347692389': 'دليشوس بيكري للماكولات والمشروبات', '205519822': 'عواطف عبدالعزيز طه محمد عيسي'}

for year in [2022, 2023]:
    fieldnames = list(map(str, range(7)))
    with open(f'Purchases_{year}.csv', 'r', encoding="utf-8-sig", newline="") as csvfile, open(f'Purchases_{year}_Mod.csv', 'a', encoding="utf-8-sig", newline="") as output:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        for row in reader:
            # 1: name, 2: tax_num
            if row['2'] != '' and '?' in row['1']:

                if row['2'] in ["547135335", "531430340"]:
                    writer.writerow({'0': row['0'],'1': row['1'], '2': row['2'], '3': row['3'],'4': row['4'],'5': row['5'], '6': row['6']})

                elif row['2'] in tax_nums:
                    writer.writerow({'0': row['0'],'1': tax_nums[row['2']], '2': row['2'], '3': row['3'],'4': row['4'],'5': row['5'], '6': row['6']})

                else:
                    def search_name():
                        sleep(1)
                        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="financierTaxIdLbl"]')))
                        sleep(1)
                        browser.find_element(by="xpath", value='//input[@id="financierTaxIdLbl"]').clear()
                        sleep(1)
                        browser.find_element(by="xpath", value='//input[@id="financierTaxIdLbl"]').send_keys(row["2"])
                        sleep(1)

                        # click drop down
                        # //select[@id="FileNumberList"]
                        browser.find_element(by="xpath", value='//select[@id="FileNumberList"]').click()
                        sleep(1)
                        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="blockUI"]')))
                        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="blockUI blockMsg blockPage"]')))

                        # click option [1]
                        # //select[@id="FileNumberList"]/option
                        wait.until(EC.visibility_of_element_located((By.XPATH, '//select[@id="FileNumberList"]/option[2]')))
                        # wait.until(EC.text_to_be_present_in_element((By.XPATH, '//select[@id="FileNumberList"]/option[2]')))
                        browser.find_element(by="xpath", value='//select[@id="FileNumberList"]/option[2]').click()
                        sleep(1)

                        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="blockUI"]')))
                        wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="blockUI blockMsg blockPage"]')))
                        # copy text
                        # //input[@id="financierNameLbl"]
                        supplier = browser.find_element(by="xpath", value='//input[@id="financierNameLbl"]').get_attribute('value')
                        sleep(0.5)
                        # print(supplier)
                    # row['2'] = '00000000'
                    # print(row)
                        # print("Edit!")
                        writer.writerow({'0': row['0'],'1': supplier, '2': row['2'], '3': row['3'],'4': row['4'],'5': row['5'], '6': row['6']})
                        sleep(0.5)
                        tax_nums[row['2']] = supplier
                        print(tax_nums)

                    try:
                        try:
                            sleep(2)
                            search_name()
                            sleep(2)
                        except:
                            print("Second_time")
                            sleep(2)
                            search_name()
                            sleep(2)
                    except:
                        writer.writerow({'0': row['0'],'1': row['1'], '2': row['2'], '3': row['3'],'4': row['4'],'5': row['5'], '6': row['6']})


            else:
                # print("origin")
                writer.writerow({'0': row['0'],'1': row['1'], '2': row['2'], '3': row['3'],'4': row['4'],'5': row['5'], '6': row['6']})

print("Done")
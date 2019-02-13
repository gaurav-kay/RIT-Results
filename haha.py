from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

usns = []
results = {}

for i in range(1, 400):
    if i < 10:
        usns.append("1MS17IS00" + str(i))
    elif 100 > i >= 10:
        usns.append("1MS17IS0" + str(i))
    elif 100 <= i:
        usns.append("1MS17IS" + str(i))

driver = webdriver.Chrome('D:/Download/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(30)

driver.get('http://exam.msrit.edu')
captcha = input('enter captcha ')

for usn in usns:
    usn_ip = driver.find_element_by_css_selector('#usn')
    usn_ip.send_keys(usn)

    captcha_ip = driver.find_element_by_css_selector('#osolCatchaTxt0')
    captcha_ip.send_keys(captcha.upper())

    enter = driver.find_element_by_css_selector('.buttongo').click()

    # error check
    script = BeautifulSoup(driver.execute_script('return document.body.innerHTML'), 'lxml')
    x = script.select('center')
    print(x)
    if len(x) != 0:
        print("holo")
        driver.back()
        continue

    name = driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]').text
    sgpa = driver.find_element_by_xpath('//*[@id="main"]/div/table/tbody/tr[9]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/div/span[2]').text

    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(usn + "-" + name + "@" + sgpa + "$")

    driver.back()


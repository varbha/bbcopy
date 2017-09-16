from selenium import webdriver
import requests, bs4
import os

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", 'C:\\BBCopy')
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

d = webdriver.Firefox(firefox_profile=fp)
d.get("https://blackboard.svkm.ac.in")
try:
    userid = d.find_element_by_id('user_id')
    password = d.find_element_by_id('password')
    print("Found element: ", userid)
    print("Found element: ", password)
    userid.send_keys('70021014011')
    password.send_keys('70021014011')
    password.submit()
    d.implicitly_wait(30)
    c=d.find_element_by_id('Courses.label')
    c.click()
    p = d.find_element_by_link_text('NMMPSMU_1718_CL_FBTE0CS_07_0B_03: MPS (M) B. Tech (Comp) 0B S07 () - Data Warehousing and Mining')
    p.click()
    c=d.find_element_by_id('paletteItem:_296487_1')
    c.click()
    j = d.find_element_by_id('anonymous_element_20')
    j.click()
    d.implicitly_wait(10)
    html = d.page_source
    #print(html)
    soup = bs4.BeautifulSoup(html,"html.parser")
    no_of_files = soup.select("ul.contentListPlain li")
    print(len(no_of_files))
    # l = len(no_of_files)
    # i=1
    # while(i<=l):
    #     xpath = '//ul[@id="content_listContainer"]/li['+i+']/div[@class="details"]/span[@class="note"][3]'
    #     list_of_files = d.find_element_by_xpath(xpath)
    exp = d.find_element_by_id('anonymous_element_10')
    exp.click()
    file = d.find_element_by_xpath('//ul[@class="attachments clearfix"]/li[2]/a')
    file.click()





except Exception as e:
    print(e)

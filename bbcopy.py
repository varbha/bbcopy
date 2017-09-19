from selenium import webdriver
import requests, bs4
import os

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", 'C:\\BBCopy\\DWM') # directory to save the file
# change the file MIME type here
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.wordprocessingml.document") # MIME type of .docx files

d = webdriver.Firefox(firefox_profile=fp)
d.get("https://blackboard.svkm.ac.in")
try:
    userid = d.find_element_by_id('user_id')
    password = d.find_element_by_id('password')
    print("Found element: ", userid)
    print("Found element: ", password)
    print("Sending user credentials...")
    userid.send_keys('70021014011')
    password.send_keys('70021014011')
    password.submit()
    print("user credentials submitted.")
    d.implicitly_wait(30)
    c=d.find_element_by_id('Courses.label')
    print("Navigating to courses..")
    c.click()
    # change subject name here
    p = d.find_element_by_link_text('NMMPSMU_1718_CL_FBTE0CS_07_0B_03: MPS (M) B. Tech (Comp) 0B S07 () - Data Warehousing and Mining')

    p.click()
    print("Chosen subject selected..")
    c=d.find_element_by_id('paletteItem:_296487_1')
    c.click()
    print("Navigated to Course Tools")
    j = d.find_element_by_id('anonymous_element_20')
    j.click()
    print("Navigated to Journals..")
    d.implicitly_wait(30)
    html = d.page_source
    #print(html)
    soup = bs4.BeautifulSoup(html,"html.parser")
    no_of_files = soup.select("ul.contentListPlain li")
    print(len(no_of_files))

    starting_index = 8
    total_files = len(no_of_files)
    while(total_files):
        try:
            exp = d.find_element_by_id('anonymous_element_'+str(starting_index))
            exp.click()
            print("Clicked on link")
        except Exception as e:
            print(e)
        try:
            file = d.find_element_by_xpath('html/body/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/a')
            file.click()
            print("File Found..")
            print("Check destination folder for file download")
        except Exception as e:
            print("No attachement found for index= ", starting_index)
            print("Continuing to next..")
        total_files-=1
        starting_index+=1
        d.back()






except Exception as e:
    print(e)

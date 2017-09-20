from selenium import webdriver
# FOLLOWING PACKAGES ARE FOR EXPLICIT WAIT
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import requests, bs4, argparse
import os
# CLI ARGUMENTS (ADDED 20/9/17 )
parser =argparse.ArgumentParser(description='Specify download conditions')
parser.add_argument('--exp', help = 'Specify the experiment number you wish to download : 1,2,3 for experiments 1,2 and 3 and -1 for all experiments', default = '-1')
parser.add_argument('--asg', help = 'Specify the assignment number you want to download: 1,2,3 for assignment 1,2 and 3', default = '0')
args = parser.parse_args()
print('These are the experiments requested: {}'.format(str(args.exp).split(',')))
print('These are the assignments requested: {}'.format(str(args.asg).split(',')))

# FIREFOX PROPERTIES
fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", 'C:\\BBCopy\\DC') # directory to save the file
# change the file MIME type here
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.openxmlformats-officedocument.wordprocessingml.document") # MIME type of .docx files

# WEBDRIVER PROPERTIES
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
    print("Navigation to Courses successful")
    # change subject name here
    p = d.find_element_by_link_text('NMMPSMU_1718_CL_FBTE0CS_07_0B_01: MPS (M) B. Tech (Comp) 0B S07 () - Distributed Computing')

    p.click()
    print("Chosen subject selected..")
    c=d.find_element_by_id('paletteItem:_296471_1')
    c.click()
    print("Navigated to Course Tools")
    d.implicitly_wait(60)
    j = d.find_element_by_id('anonymous_element_20')
    j.click()
    print("Navigated to Journals..")
    d.implicitly_wait(30)
    html = d.page_source
    #print(html)
    soup = bs4.BeautifulSoup(html,"html.parser")
    no_of_files = soup.select("ul.contentListPlain li")
    print(len(no_of_files))

# LOGIC FOR EXPERIMENTS DOWNLOAD
    if '-1' in str(args.exp).split(','):
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
                file = d.find_element_by_xpath('html/body/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/a') #I HATE absolute xpaths, but testing to see if faster than relative xpaths
                file.click()
                print("File Found..")
                print("Check destination folder for file download")
            except Exception as e:
                print("No attachement found for index= ", starting_index)
                print("Continuing to next..")
            total_files-=1
            starting_index+=1
            d.back()
    else:
        list_of_exps = str(args.exp).split(',')
        for i in list_of_exps:
            print(i)
            search_str = 'B1_Exp' + i
            try:
                exp = d.find_element_by_link_text(search_str)
                print("Found Experiment: " + i)
                exp.click()
            except Exception as e:
                print(e)
                continue
            try:
                file = d.find_element_by_xpath('html/body/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/a') #I HATE absolute xpaths, but testing to see if faster than relative xpaths
                file.click()
                print("File Found..")
                print("Check destination folder for file download")
            except Exception as e:
                print("No attachment found for index= " + i)
                print("Continuing to next..")
            d.back()
# LOGIC FOR ASSIGNMENTS DOWNLOAD
# TODO : Make logic for assignment download
    # if '0' in str(args.asg).split(','):
    #     no_of_assgs = d.find_elements_by_partial_link_text('assignment')
    #     print(len(no_of_assgs))
    #     for x in no_of_assgs:

    #         x.click()
    #         d.back()

    #     while(total_files):
    #         try:
    #             exp = d.find_element_by_id('anonymous_element_'+str(starting_index))
    #             exp.click()
    #             print("Clicked on link")
    #         except Exception as e:
    #             print(e)
    #         try:
    #             file = d.find_element_by_xpath('html/body/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/a')
    #             file.click()
    #             print("File Found..")
    #             print("Check destination folder for file download")
    #         except Exception as e:
    #             print("No attachement found for index= ", starting_index)
    #             print("Continuing to next..")
    #         total_files-=1
    #         starting_index+=1
    #         d.back()
    # else:
    #     list_of_exps = str(args.exp).split(',')
    #     for i in list_of_exps:
    #         print(i)
    #         search_str = 'Experiment ' + i
    #         try:
    #             exp = d.find_element_by_link_text(search_str)
    #             print("Found Experiment: " + i)
    #             exp.click()
    #         except Exception as e:
    #             print(e)
    #         try:
    #             file = d.find_element_by_xpath('html/body/div[5]/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[2]/ul/li[2]/a') #I HATE absolute xpaths, but testing to see if faster than relative xpaths
    #             file.click()
    #             print("File Found..")
    #             print("Check destination folder for file download")
    #         except Exception as e:
    #             print("No attachement found for index= " + i)
    #             print("Continuing to next..")
    #         d.back()



except Exception as e:
    print(e)

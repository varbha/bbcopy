from selenium import webdriver
import requests, bs4

d = webdriver.Firefox()
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
    ex = soup.select('.note')
    ex = [ex[i] for i in range(2,len(ex),3)]
    print(ex)




except Exception as e:
    print(e)

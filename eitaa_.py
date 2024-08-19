from selenium import webdriver,common
import time
import pyperclip
from selenium.webdriver.firefox.options import Options
from pandas import DataFrame
from itertools import groupby




options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
service = webdriver.FirefoxService(executable_path= r'A:\QRcode\eitaa\geckodriver.exe')
driver = webdriver.Firefox(service=service , options=options )


driver.get("https://web.eitaa.com/")

time.sleep(10)
driver.find_element("xpath",'/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]').send_keys(input("enter your phone number: "))
driver.find_element("xpath","/html/body/div[1]/div/div[2]/div[1]/div/div[3]/button/div").click()

time.sleep(10)
driver.find_element("xpath" , "/html/body/div[1]/div/div[2]/div[3]/div/div[3]/div/input").send_keys(input("enter code:"))
time.sleep(12)
driver.find_element("xpath", "/html/body/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/input").click()



ac =  webdriver.ActionChains(driver)

a = []
b = []
links = []
views = []
names = []


        
            

def clicker(x,i):
    x.location_once_scrolled_into_view
    ac.context_click(x).perform()
    
    z = driver.find_element("xpath",'//div[@class="btn-menu-item tgico-link rp"]')
    z.location_once_scrolled_into_view
    try:
        time.sleep(1)
        z.click()
        
        links.append(pyperclip.paste())
        names.append(i.text.splitlines()[0])
        
    except  ( common.exceptions.ElementNotInteractableException,common.exceptions.MoveTargetOutOfBoundsException) as s:
        return
       
    
    for j in x.text.splitlines()[::-1]:
        
        if j.isdigit() or "K" in j:
            views.append(j)
            break
        
               
def eitaa_search(search):
    global a ; global b ;global views;global names;global links
    try:
        
        driver.find_element("xpath","/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div/nav/div[5]/div").click()
        driver.find_element("xpath","/html/body/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/input").send_keys(search)
        time.sleep(6)
        while True:
            g = [ i.text for i in driver.find_elements("xpath","//li[@class='rp chatlist-chat']" )]
            if all_equal(g):
                driver.find_element("xpath",'/html/body/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/i[2]').click()
                return 1
            
                
            t = 0
            for i in driver.find_elements("xpath","//li[@class='rp chatlist-chat']" ):
                
                if i.text not in b:
                    if i.text!="":
                        if len(i.text.splitlines()[1].split("/")) != 1:
                            t = 1
                            break
                    i.location_once_scrolled_into_view
                    b.append(i.text)
                    
                    try:
                        i.click()
                        
                    except   (common.exceptions.ElementNotInteractableException , common.exceptions.ElementClickInterceptedException,common.exceptions.MoveTargetOutOfBoundsException) as e:
                        continue
                    
                    
                    
                    time.sleep(3)
                    a = driver.find_elements('xpath','//div[@class="message"]')[::-1]
                    for u in a:
                    
                        c=0
                        p = 7
                        for d in search.lower().split():
                            if d in u.text:
                                c+=1
                            if c==len(search.lower().split()):
                                clicker(u,i)
                                p = 0
                                break
                        if p==0:   
                            break    
            
            if len(g)==len(driver.find_elements("xpath","//li[@class='rp chatlist-chat']" )) or t==1 :
                

                if len(links)==len(views)==len(names):
                    df = DataFrame({'تعداد بازدید': views, 'لینک پست': links , 'اسم کانال':names})
                    df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
                    eq_view = 0
                    eq_len = len(links)
                    for k in views:
                        if "K" in k:
                        
                            eq_view += eval(k.strip("K"))
                 
                        else:
               
                            eq_view += (eval(k)/1000)   
                        
                    
                else:
                    print("t ",len(links),len(views),len(names)) 
                a.clear()
                b.clear()
                links.clear()
                views.clear()
                names.clear()
                time.sleep(3)
                driver.find_element("xpath",'/html/body/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/i[2]').click()
                return f''' {eq_len} کانال منتشر شده
                         مجموع بازدید: {"{:.3f}".format(eq_view)}k '''
            
            
                
    except Exception as e:
        print(e)
        if len(links)==len(views)==len(names):
            df = DataFrame({'تعداد بازدید': views, 'لینک پست': links , 'اسم کانال':names})
            df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
            eq_view = 0
            eq_len = len(links)
            for k in views:
                if "K" in k:
                    eq_view += eval(k.strip("K"))
                else:
                    eq_view += (eval(k)/1000)   
            
        else:
            print("e ",len(links),len(views),len(names))    
        a.clear()
        b.clear()
        links.clear()
        views.clear()
        names.clear()
        driver.find_element("xpath",'/html/body/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/i[2]').click()
        return f''' {eq_len} کانال منتشر شده
                         مجموع بازدید: {"{:.3f}".format(eq_view)}k '''



def all_equal(iterable):
    g = groupby(iterable)
    
    return next(g, True) and not next(g, False)
result = eitaa_search(input("search: "))

print(result+"\nsee the test.xslx" if result!=1 else "nothing...")
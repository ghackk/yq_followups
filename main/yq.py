#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# In[2]:


opt=Options()
options =webdriver.ChromeOptions()
#options.add_argument('--headless')
opt.add_experimental_option("debuggerAddress","localhost:8080")


# In[3]:


driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe",options=options)


# In[4]:


driver.maximize_window()


# In[5]:


driver.get("https://www.yourquote.in")


# In[6]:


signin = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/nav/div/div/div[4]/div/div[5]/div/div/div')
signin.click()
window_before = driver.window_handles[0]
wait = WebDriverWait(driver,2500)


# In[7]:


fb = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[1]/div/div[2]/div[2]/div')
fb.click()
wait = WebDriverWait(driver,2500)


# In[8]:


window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
wait = WebDriverWait(driver,1000)
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("gyaneshkumar6520@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#pass").send_keys("findityourself")


# In[9]:


login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
# hindi //input[@value="Log In"] In"] english
login.click()
time.sleep(3)
driver.switch_to.window(window_before)


# In[10]:


time.sleep(5)
popup1 = driver.find_element_by_css_selector('#app > div.application--wrap > div > div.layout.card-shadow.hidden-sm-and-down.bg-c-c0.text-xs-center.anchor-ad.justify-center.align-center > div')
popup1.click()


# In[11]:


heading=[]
heading = driver.find_elements_by_xpath('//div[@class="v-tabs__div m-l-2x m-r-2x"]')
for h in heading :
        h.click()
        time.sleep(7)
        for i in range(5):
            like=[]
            like = driver.find_elements_by_xpath('//div[@class="sprite-icon-favourite sprite-icon-size-4"]')
            for l in like:
                l.click()
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(2)
            follow=[]
            follow = driver.find_elements_by_xpath('//span[@class="fw-6"]')
            for e in follow:
                e.click()
            time.sleep(0.5)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)      
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)  


# In[ ]:





# In[ ]:





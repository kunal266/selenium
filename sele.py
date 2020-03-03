from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
import wget
import os

"/html/body/main/article/form/div[1]/table/tbody/tr[2]/td/div[2]/select/option[72]"
"/html/body/main/article/form/div[1]/table/tbody/tr[2]/td/div[2]/select/option[146]"
"/html/body/main/article/form/div[1]/table/tbody/tr[2]/td/div[2]/select/option[177]"
"/html/body/main/article/form/div[1]/table/tbody/tr[2]/td/div[2]/select/option[210]"
"/html/body/main/article/pre"
driver = webdriver.Chrome("C:\\Users\91865\Downloads\chromedriver_win32\chromedriver")
driver.get("https://archive.physionet.org/cgi-bin/atm/ATM?tool=&database=&rbase=&srecord=&annotator=&signal=&sfreq=&tstart=&tdur=&tfinal=&action=&tfmt=&dfmt=&nbwidth=")
#time.sleep(6)
#driver.back()
#time.sleep(6)
#driver.forward()
#time.sleep(5)
#driver.back()
database = driver.find_element_by_name("database")
time.sleep(0.5)
database.click()
time.sleep(0.5)
dbopt = driver.find_element_by_xpath("/html/body/main/article/form/div[1]/table/tbody/tr[1]/td/div[2]/select/option[108]")
time.sleep(0.5)
dbopt.click()
time.sleep(0.5)
recordlist = driver.find_element_by_name("rbase")
time.sleep(0.5)
recordlist.click()
time.sleep(0.5)
sample = driver.find_element_by_xpath("/html/body/main/article/form/div[1]/table/tbody/tr[6]/td/div[2]/label[6]/input")
sample.click()
time.sleep(0.3)
for i in range(13,550):
    xpathh = "/html/body/main/article/form/div[1]/table/tbody/tr[2]/td/div[2]/select/option[%s]" %i

    recopt = driver.find_element_by_xpath(xpathh)
    patient_name = recopt.text
    time.sleep(.1)
    recopt.click()
    time.sleep(.1)
    toolbox = driver.find_element_by_name("tool")
    time.sleep(.1)
    toolbox.click()
    time.sleep(.1)
    toolopt = driver.find_element_by_xpath("/html/body/main/article/form/div[1]/table/tbody/tr[8]/td/div/select/option[8]")
    time.sleep(.1)
    toolopt.click()
    #time.sleep(.1)
    dowd = driver.find_element_by_xpath("/html/body/main/article/font/pre/a[2]")
    linkk = dowd.get_attribute('href')
    #linkk = linkk.replace("samples","%s" %patient_name)
    #print(patient_name)
    patient_name_main = "_".join(patient_name.split("/"))
    #print(linkk)
    wget.download(linkk)
    time.sleep(1.5)
    os.rename("samples.csv","%s.csv" %patient_name_main)
    #data = driver.find_element_by_xpath("/html/body/main/article/pre")
    #print(data.text)
    #with open("record_list_1","w+") as csv_file:
    #csv_file = csv.reader()
    #time.sleep(1.5)
    #driver.back()
    #time.sleep(1.5)
    #driver.back()
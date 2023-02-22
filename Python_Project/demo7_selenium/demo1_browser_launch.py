from selenium import webdriver

d=webdriver.Chrome()
d.get("https://www.google.com/")
print(d.title)
d.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.find_element_by_partial_link_text("Sign in").click()
driver.find_element_by_name("email").send_keys("isharora3@gmail.com")
driver.find_element_by_name("password").send_keys("*******")
driver.find_element_by_id("signInSubmit").click()
driver.find_element_by_id("twotabsearchtextbox").send_keys("Mens shoes")
driver.find_element_by_css_selector("#nav-search > form > div.nav-right > div > input").click()
driver.find_element_by_partial_link_text("Boots").click()
driver.find_element_by_partial_link_text("Snow").click()
driver.find_element_by_xpath("//*[@id='rot-B018Y3E85C']/div/a/div[1]/img").click()
dropdown = driver.find_element_by_css_selector("#native_dropdown_selected_size_name")
select = Select(dropdown)
select.select_by_value("4,B018Y3E7XK")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
time.sleep(2)
driver.find_element_by_id("twotabsearchtextbox").send_keys("Mens shirts")
driver.find_element_by_css_selector("#nav-search > form > div.nav-right > div > input").click()
driver.find_element_by_link_text("Clothing").click()
time.sleep(3)
driver.find_element_by_link_text("Shirts").click()
#driver.find_element_by_xpath("//*[@id='refinements']/div[2]/ul[1]/li[1]/ul[1]/li[1]/a/span").click()
time.sleep(3)
driver.find_element_by_link_text("Dress Shirts").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='result_1']/div/div[1]/div/a/img").click()
dropdown = driver.find_element_by_css_selector("#native_dropdown_selected_size_name")
select = Select(dropdown)
select.select_by_value("5,B009ESZFHC")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
time.sleep(2)
driver.find_element_by_partial_link_text("Cart").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='activeCartViewForm']/div[2]/div[2]/div[4]/div[2]/div[1]/div/div/div[2]/div/span[1]/span/input").click()
time.sleep(5)
driver.get("http://www.amazon.com/gp/flex/sign-out.html/ref=nav_youraccount_signout")


#driver.find_element_by_id("enterAddressFullName").send_keys("Isha Arora")
#driver.find_element_by_name("enterAddressAddressLine1").send_keys("10 Shrewsbury Green drive")
#driver.find_element_by_name("enterAddressAddressLine2").send_keys("Apt#4")
#driver.find_element_by_id("enterAddressCity").send_keys("Shrewsbury")
#driver.find_element_by_name("enterAddressStateOrRegion").send_keys("MA")
#driver.find_element_by_name("enterAddressPostalCode").send_keys("01545")
#driver.find_element_by_name("enterAddressPhoneNumber").send_keys("8325034096")
#driver.find_element_by_name("shipToThisAddress").click()
#driver.find_element_by_xpath("//*[@id='shippingOptionFormId']/div[3]/div/div/span[1]/span/input").click()
#driver.find_element_by_css_selector("//*[@id='pm_0']").click()

#driver.find_element_by_id("add-to-cart-button").click()
#driver.find_element_by_partial_link_text("Fashion Sneakers").click()
#dropdown = driver.find_element_by_css_selector("#native_dropdown_selected_size_name")
#select = Select(dropdown)
#select.select_by_value("4,B01CE7QQPY")
#driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
#driver.find_element_by_xpath("//*[@id='color_name_5']")
#ele.send_keys(Keys.ENTER)

#driver.find_element_by_class_name("imgSwatch").click()
#dropoptions = driver.find_elements_by_tag_name("option")
#print len(dropoptions)
#for values in dropoptions:
    #print values.text
#wait = WebDriverWait(driver, 20)
#element = wait.until(EC.element_to_be_clickable((By.ID,'add-to-cart-button')))
#driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
#dropdown = driver.find_element_by_css_selector("#native_dropdown_selected_size_name")
#select = Select(dropdown)
#select.select_by_value("4,B01CE7QQPY")
#driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
#driver.find_element_by_id("add-to-cart-button").click()
#alert = driver.switch_to_alert()
#alert.dismiss()





#dataset_drop_down_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#native_dropdown_selected_size_name")))
#dataset_drop_down_element = Select(dataset_drop_down_element)
#for option in ele.find_elements_by_css_selector("#native_dropdown_selected_size_name"):
#    if option.text == "MEN 9.5(M)US 43EU":
#        option.click()
#        break

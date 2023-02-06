import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#initialize webdriver
options1 = webdriver.ChromeOptions()
options1.add_argument("disable-infobars")
options1.add_argument("--disable-extensions")
options1.add_argument('--headless')
options1.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options1)

#Open URL and maximize window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()
driver.implicitly_wait(10)

#phones button
phones=driver.find_element(By.XPATH,'//a[text()="Phones & PDAs"]')
phones.click()


#iphone
iphone=driver.find_element(By.XPATH,'//a[text()="iPhone"]')
iphone.click()
time.sleep(1)

#first picture
first_pic=driver.find_element(By.XPATH,'//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

#next picture
next_click=driver.find_element(By.XPATH,'//button[@title="Next (Right arrow key)"]')

for i in range(0,5):
    next_click.click()
    time.sleep(2)
    # save screenshot
    # driver.save_screenshot('screenshot#' + str(i+1) + '.png')



#close
x_button=driver.find_element(By.XPATH,'//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)

#quantity
quantity=driver.find_element(By.ID,'input-quantity')
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)
'''
#add to cart
add_to_button=driver.find_element(By.ID,'button-cart')
add_to_button.click()
time.sleep(2)
'''

laptops=driver.find_element(By.XPATH,'//a[text()="Laptops & Notebooks"]')
action=ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2=driver.find_element(By.XPATH,'//a[text()="Show All Laptops & Notebooks"]')
laptops_2.click()
time.sleep(1)

#click on HP laptop
HP=driver.find_element(By.XPATH,'//a[text()="HP LP3065"]')
HP.click()

#scroll
add_to_button_2=driver.find_element(By.XPATH,'//button[@id="button-cart"]')
location=add_to_button_2.location_once_scrolled_into_view
print(location)
time.sleep(1)
# date=driver.find_element(By.ID,"input-option225")
# date.clear()
# date.send_keys("2023-02-01")
# time.sleep(5)

#calendar
calendar=driver.find_element(By.XPATH,'//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar=driver.find_element(By.XPATH,"//div[@class='datepicker']/div[1]/table/thead/tr/th[@class='next']")
month_year=driver.find_element(By.XPATH,"//div[@class='datepicker']/div[1]/table/thead/tr/th[@class='picker-switch']")

#year:2022 month:december
while month_year.text != 'February 2023':
    next_click_calendar.click()
time.sleep(2)

#day 31
calendar_date=driver.find_element(By.XPATH,'//td[text()="1"]')
calendar_date.click()
time.sleep(2)


#add to button
add_to_button_2.click()
time.sleep(1)

#Checkout
go_to_cart=driver.find_element(By.ID,'cart-total')
go_to_cart.click()
time.sleep(1)

checkout=driver.find_element(By.XPATH,'//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

#click on guest account
guest=driver.find_element(By.XPATH,'//input[@value="guest"]')
guest.click()

#click continue 1
continue_1=driver.find_element(By.ID,'button-account')
continue_1.click()
time.sleep(1)

#scrolling
step_2=driver.find_element(By.XPATH,'//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

#first name
first_name=driver.find_element(By.ID,'input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('Shivam')
time.sleep(1)

#last_name
last_name=driver.find_element(By.ID,'input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('Sharma')
time.sleep(1)

#email
email=driver.find_element(By.ID,'input-payment-email')
email.click()
time.sleep(1)
email.send_keys('xyz@gmail.com')
time.sleep(1)

#telephone
telephone=driver.find_element(By.ID,'input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('9999888877')
time.sleep(1)

#address
address=driver.find_element(By.ID,'input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 187')
time.sleep(1)

#city
city=driver.find_element(By.ID,'input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Satna')
time.sleep(1)

#postcode
postcode=driver.find_element(By.ID,'input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)


#country
country=driver.find_element(By.ID,'input-payment-country')
dropdown_1=Select(country)
time.sleep(1)
dropdown_1.select_by_visible_text("India")
time.sleep(1)

#region
region=driver.find_element(By.ID,'input-payment-zone')
dropdown_2=Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Madhya Pradesh')
time.sleep(1)

#click continue 2
continue_2=driver.find_element(By.XPATH,'//input[@id="button-guest"]')
continue_2.click()
time.sleep(1)

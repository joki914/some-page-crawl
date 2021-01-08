from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
__all__ = [webdriver, sleep, Keys, Options, random]


option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

browser = webdriver.Chrome(options=option, executable_path='chromedriver.exe')
#try to open a website
browser.get('https://www.facebook.com')
# Điền thông tin
txtUser = browser.find_element_by_id('email')
txtUser.send_keys('justasubnick.mlem@gmail.com')
sleep(3)
txtPassword = browser.find_element_by_id('pass')
txtPassword.send_keys('JokerKid914')
txtPassword.send_keys(Keys.ENTER)
# Lay link hien cmt
sleep(random.randint(5,10))
browser.get('https://www.facebook.com/Vietgangzbrotherhood/posts/2858931084393652')
sleep(5)
commentList = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
print(commentList)


sleep(random.randint(5,10))

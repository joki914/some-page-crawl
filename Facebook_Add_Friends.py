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
sleep(random.randint(1,4))

txtPassword = browser.find_element_by_id('pass')
txtPassword.send_keys('JokerKid914')
txtPassword.send_keys(Keys.ENTER)
# Lay link hien cmt
sleep(random.randint(5,10))
browser.get('https://www.facebook.com/randy.bu.35/friends')
sleep(5)
"""showCmt = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div[4]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div[1]/div/div[2]/div[1]/span/div/span")
showCmt.click()"""
"""clickCmt = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div[4]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div/div[2]/span/span')
clickCmt.click()
sleep(random.randint(5,10))
clickCmt.click()"""

isFriends = browser.find_element_by_css_selector('span._55pe').send_keys(Keys.DOWN)
sleep(3)
requestFriend = browser.find_element_by_css_selector('button._42ft._4jy0.FriendRequestOutgoing.enableFriendListFlyout.outgoingButton.enableFriendListFlyout._4jy3._517h._51sy').send_keys(Keys.DOWN)

sleep(4)
ktra = 0
try:
    addFriends = browser.find_elements_by_css_selector('button._42ft._4jy0.FriendRequestAdd.addButton._4jy3._4jy1.selected._51sy')
    browser.execute_script('arguments=[0].scrollIntoView();', addFriends)
    print(len(addFriends))
    for friend in addFriends:
        try:
            friend.click()
            sleep(random.randint(2,4))
        except:
            ktra += 1
            print("Couldn't find 'Add friend' button or error was displayed")
except:
    print('Done')
print(ktra)
sleep(random.randint(5,10))
browser.close()
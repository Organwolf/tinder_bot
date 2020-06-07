from selenium import webdriver
from decouple import config
from time import sleep


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://tinder.com')

        sleep(5)

        gg_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        gg_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(config('EMAIL'))

        nxt_btn = self.driver.find_element_by_xpath(
            '//*[@id="identifierNext"]')
        nxt_btn.click()

        sleep(1)

        pw_in = self.driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input')
        pw_in.send_keys(config('PW'))

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="passwordNext"]')
        login_btn.click()

        # switch back to main window
        self.driver.switch_to.window(base_window)

        allow_location_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_location_btn.click()

        enable_notifications_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_notifications_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        add_home_screen_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        add_home_screen_popup.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
sleep(2)
bot.auto_swipe()

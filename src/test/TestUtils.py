import time
import sys, os
from unittest import result
from dotenv import find_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"

url = "https://e-learning.hcmut.edu.vn/"
LOGIN_BUTTON_XPATH = "//a[@href='https://e-learning.hcmut.edu.vn/login/index.php']"
STUDENT_TEACHER_XPATH = (
    "//a[@href='https://e-learning.hcmut.edu.vn/login/index.php?authCAS=CAS']"
)
LOUGOUT_BUTTON_XPATH = (
    "//a[starts-with(@href, 'https://e-learning.hcmut.edu.vn/login/logout.php')]"
)
CHANGE_PASSWORD_LINK_XPATH = "//a[@href='https://account.hcmut.edu.vn/']"
CHANGE_PASSWORD_SUBMIT_XPATH = "//button[@type='submit']"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()


def goToLoginPage():
    driver.get(url)
    driver.find_element(By.CLASS_NAME, "langbutton")
    lang_dropdown_menu_ele = driver.find_element(By.ID, "lang-action-menu")
    if lang_dropdown_menu_ele.is_displayed():
        driver.find_element(By.XPATH, "//a[text()[contains(.,'English')]]").click()
    driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
    driver.find_element(By.XPATH, STUDENT_TEACHER_XPATH).click()


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()


class TestLogin:
    @staticmethod
    def test(username, password, expect, num):
        goToLoginPage()
        input_str = """username: %s
password: %s
""" % (
            username,
            password,
        )
        TestUtil.makeSource(input_str, num)
        TestLogin.login(username, password)
        TestLogin.check(SOL_DIR, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        result_eles = driver.find_elements(By.ID, "msg")
        if len(result_eles) == 0:
            powermenu_btn = driver.find_element(By.ID, "user-menu-toggle")
            if powermenu_btn.is_displayed():
                dest.write("Login successfully")
                powermenu_btn.click()
                driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://e-learning.hcmut.edu.vn/login/logout.php')]").click()
                return
        dest.write(result_eles[0].text)

    @staticmethod
    def login(username, password):
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()


class TestChangePassword:
    @staticmethod
    def test(login, oldpassword, newpassword, confirmpassword, expect, num):
        input_str = """login: %s
oldpassword: %s
newpassword: %s
confirmpassword: %s
        """ % (
            login,
            oldpassword,
            newpassword,
            confirmpassword,
        )
        TestUtil.makeSource(input_str, num)

        TestChangePassword.changePassword(
            login, oldpassword, newpassword, confirmpassword
        )
        TestChangePassword.check(SOL_DIR, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        # changed succeess
        if (
            line
            == "Your password was changed and your email password on Gmail will updated after 12 hours"
        ):
            TestChangePassword.changePassword(
                login, newpassword, oldpassword, oldpassword
            )

        return line == expect

    @staticmethod
    def check(soldir, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        result_ele = driver.find_element(By.CLASS_NAME, "result")
        dest.write(result_ele.text)

    @staticmethod
    def changePassword(login, oldpassword, newpassword, confirmpassword):
        goToLoginPage()
        driver.find_element(By.XPATH, CHANGE_PASSWORD_LINK_XPATH).click()
        driver.find_element(By.ID, "login").send_keys(login)
        driver.find_element(By.ID, "oldpassword").send_keys(oldpassword)
        driver.find_element(By.ID, "newpassword").send_keys(newpassword)
        driver.find_element(By.ID, "confirmpassword").send_keys(confirmpassword)
        driver.find_element(By.XPATH, CHANGE_PASSWORD_SUBMIT_XPATH).click()

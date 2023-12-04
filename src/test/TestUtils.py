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

url = "https://ten-ten-v2.vercel.app/sign-in"
LOGIN_BUTTON_XPATH = "//a[@href='https://e-learning.hcmut.edu.vn/login/index.php']"
STUDENT_TEACHER_XPATH = (
    "//a[@href='https://e-learning.hcmut.edu.vn/login/index.php?authCAS=CAS']"
)
LOUGOUT_BUTTON_XPATH = (
    "//a[starts-with(@href, 'https://e-learning.hcmut.edu.vn/login/logout.php')]"
)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()

def goToLoginPage():
    driver.get(url)
    # driver.find_element(By.CLASS_NAME, "langbutton")
    # lang_dropdown_menu_ele = driver.find_element(By.ID, "lang-action-menu")
    # if lang_dropdown_menu_ele.is_displayed():
    #     driver.find_element(By.XPATH, "//a[text()[contains(.,'English')]]").click()
    # driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
    # driver.find_element(By.XPATH, STUDENT_TEACHER_XPATH).click()


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()


class TestLogin:
    @staticmethod
    def test(phoneNumber, password, checked, expect, num):
        goToLoginPage()
        input_str = input_str = """username: %s
password: %s
checked: %s
""" % (
            phoneNumber,
            password,
            checked
        )
        TestUtil.makeSource(input_str, num)
        TestLogin.login(phoneNumber, password, checked)
        TestLogin.check(SOL_DIR, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, num):
        # dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        # result_eles = driver.find_elements(By.ID, "msg")
        # if len(result_eles) == 0:
        #     powermenu_btn = driver.find_element(By.ID, "user-menu-toggle")
        #     if powermenu_btn.is_displayed():
        #         dest.write("Login successfully")
        #         powermenu_btn.click()
                # driver.find_element(By.XPATH, "//a[starts-with(@href, 'https://e-learning.hcmut.edu.vn/login/logout.php')]").click()
        #         return
        # dest.write(result_eles[0].text)

        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        result_eles = driver.find_elements(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/form/div[4]")
        if len(result_eles) == 0:
            dest.write("Login successfully")
            driver.find_element(By.XPATH, "//*[@id='default-sidebar']/div/div/a" ).click()
            return
        dest.write(result_eles[0].text)
    @staticmethod
    def login(phoneNumber, password, checked):
        driver.find_element(By.ID, "phoneNumber").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "phoneNumber").send_keys(phoneNumber)
        driver.find_element(By.ID, "password").send_keys(password)
        checkbox1 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/form/div[3]/div[1]/label/input")
        if checked == "True":
            checkbox1.click()
        driver.find_element(By.CLASS_NAME, "signin_sign-in-button___IMe_").click()
        time.sleep(2)


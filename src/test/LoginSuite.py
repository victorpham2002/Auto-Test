import unittest
from TestUtils import TestLogin


class LoginSuite(unittest.TestCase):
    def test_1(self):
        """Leave both blank"""
        username = ""
        password = ""
        expect = "Please enter your password.\nPlease enter your username."
        self.assertTrue(TestLogin.test(username, password, expect, 101))

    def test_2(self):
        """leave blank password"""
        username = "sdfasdfasdf"
        password = ""
        expect = "Please enter your password."
        self.assertTrue(TestLogin.test(username, password, expect, 102))

    def test_3(self):
        """leave blank username"""
        username = ""
        password = "asdfasdf"
        expect = "Please enter your username."
        self.assertTrue(TestLogin.test(username, password, expect, 103))

    def test_4(self):
        """Input wrong username and wrong password"""
        username = "asdfasdf"
        password = "asdfasdf"
        expect = "The credentials you provided cannot be determined to be authentic."
        self.assertTrue(TestLogin.test(username, password, expect, 104))

    def test_5(self):
        """Input correct username and wrong password"""
        username = "loc.letvl842"
        password = "asdfasdf"
        expect = "The credentials you provided cannot be determined to be authentic."
        self.assertTrue(TestLogin.test(username, password, expect, 105))

    def test_6(self):
        """Input correct username and correct password"""
        username = "loc.letvl842002"
        password = "thangcho"
        expect = "Login successfully"
        self.assertTrue(TestLogin.test(username, password, expect, 106))

    def test_7(self):
        """Input wrong username and correct password"""
        username = "loc.letvl"
        password = "thangcho"
        expect = "The credentials you provided cannot be determined to be authentic."
        self.assertTrue(TestLogin.test(username, password, expect, 107))

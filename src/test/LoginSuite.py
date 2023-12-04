import unittest
from TestUtils import TestLogin


class LoginSuite(unittest.TestCase):

    def test_1(self):
        """Input wrong phoneNumber and wrong password"""
        phoneNumber = "123456789"
        password = "asdfasdf"
        checked = "False"
        expect = "Account does not exist! Please re-enter!"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 201))

    def test_2(self):
        """Input wrong phoneNumber and wrong password"""
        phoneNumber = "123456789"
        password = "asdfasdf"
        checked = "True"
        expect = "Account does not exist! Please re-enter!"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 202))
        
    def test_3(self):
        """Input correct phoneNumber and wrong password"""
        phoneNumber = "0901235456"
        password = "asdfasdf"
        checked = "False"
        expect = "Account does not exist! Please re-enter!"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 203))

    def test_4(self):
        """Input correct phoneNumber and wrong password"""
        phoneNumber = "0901235456"
        password = "asdfasdf"
        checked = "True"
        expect = "Account does not exist! Please re-enter!"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 204))
        
    def test_5(self):
        """Input wrong phoneNumber and correct password"""
        phoneNumber = "123456789"
        password = "123456"
        checked = "False"
        expect = "Account does not exist! Please re-enter!"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 205))
        
    def test_6(self):
        """Input wrong phoneNumber and correct password"""
        phoneNumber = "123456789"
        password = "123456"
        checked = "True"
        expect = "Account does not exist! Please re-enter!"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 206))
        
    def test_7(self):
        """Input correct phoneNumber and correct password"""
        phoneNumber = "0901235456"
        password = "123456"
        checked = "False"
        expect = "Account does not exist! Please re-enter!"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 207))
        
    def test_8(self):
        """Input correct phoneNumber and correct password"""
        phoneNumber = "0901235456"
        password = "123456"
        checked = "True"
        expect = "Login successfully"
        self.assertTrue(TestLogin.test(phoneNumber, password, checked, expect, 208))
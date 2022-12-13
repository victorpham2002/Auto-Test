import unittest
from TestUtils import TestChangePassword


class ChangePasswordSuite(unittest.TestCase):
    def test_1(self):
        """Empty login"""
        login = ""
        oldpassword = ""
        newpassword = ""
        confirmpassword = ""
        expect = "Your login is required"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 201
            )
        )

    def test_2(self):
        """Not empty login, empty oldpassword"""
        login = "asdfasf"
        oldpassword = ""
        newpassword = ""
        confirmpassword = ""
        expect = "Your old password is required"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 202
            )
        )

    def test_3(self):
        """empty login, not empty oldpassword"""
        login = ""
        oldpassword = "asdfasf"
        newpassword = ""
        confirmpassword = ""
        expect = "Your login is required"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 203
            )
        )

    def test_4(self):
        """empty oldpassword, not empty newpassword"""
        login = ""
        oldpassword = ""
        newpassword = "asdfasf"
        confirmpassword = ""
        expect = "Passwords mismatch"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 204
            )
        )

    def test_5(self):
        """change success"""
        login = "loc.letvl842002"
        oldpassword = "thangcho"
        newpassword = "thangcho1234"
        confirmpassword = "thangcho1234"
        expect = "Your password was changed and your email password on Gmail will updated after 12 hours"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 205
            )
        )

    def test_6(self):
        """empty login and empty confirmpassword"""
        login = ""
        oldpassword = "thangcho"
        newpassword = "thangcho1234"
        confirmpassword = ""
        expect = "Passwords mismatch"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 206
            )
        )

    def test_7(self):
        """only empty login"""
        login = ""
        oldpassword = "thangcho"
        newpassword = "thangcho1234"
        confirmpassword = "thangcho1234"
        expect = "Your login is required"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 207
            )
        )

    def test_8(self):
        """leave newpassword, confirmpassword empty"""
        login = "loc.letvl842002"
        oldpassword = "thangcho"
        newpassword = ""
        confirmpassword = ""
        expect = "Your new password is required"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 208
            )
        )

    def test_9(self):
        """leave newpassword, confirmpassword empty"""
        login = "loc.letvl842002"
        oldpassword = "thangcho"
        newpassword = ""
        confirmpassword = ""
        expect = "Your new password is required"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 209
            )
        )

    def test_10(self):
        """leave newpassword, confirmpassword empty"""
        login = "loc.letvl842002"
        oldpassword = "thangcho"
        newpassword = ""
        confirmpassword = ""
        expect = "Your new password is required"

        self.assertTrue(
            TestChangePassword.test(
                login, oldpassword, newpassword, confirmpassword, expect, 210
            )
        )

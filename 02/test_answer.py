import answer
import unittest

passwords = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

class TestPasswords(unittest.TestCase):

    def test_good_password(self):
        result = answer.verify_password("1-3 a: abcde")
        self.assertTrue(result)

    def test_bad_password(self):
        result = answer.verify_password("1-3 b: cdefg")
        self.assertFalse(result)

    def test_count_good_passwords_v1(self):
        data = [line.strip() for line in passwords.split('\n')]
        result = answer.count_good_passwords(data)
        self.assertEqual(2, result)

    def test_count_good_passwords_v2(self):
        data = [line.strip() for line in passwords.split('\n')]
        result = answer.count_good_passwords(data, version=2)
        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()

import answer
import unittest

data = """1721
979
366
299
675
1456"""

class TestAnswer(unittest.TestCase):
    def test_values(self):
        numbers = [int(number.strip()) for number in data.split()]
        result = answer.get_answer(numbers)
        self.assertEqual(514579, result)

    def test_three_values(self):
        numbers = [int(number.strip()) for number in data.split()]
        result = answer.get_answer(numbers, combos=3)
        self.assertEqual(241861950, result)

if __name__ == '__main__':
    unittest.main()
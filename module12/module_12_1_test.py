import unittest
from module12.module_12_1 import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runer_test = Runner('Бегун гуляет')
        for call in range(10):
            runer_test.walk()
        self.assertEqual(runer_test.distance, 50)

    def test_run(self):
        runer_test = Runner('Бегун бежит')
        for call in range(10):
            runer_test.run()
        self.assertEqual(runer_test.distance, 100)

    def test_challenge(self):
        runer_first = Runner('Бегун первый')
        runer_second = Runner('Бегун второй')
        for call in range(10):
            runer_first.run()
            runer_second.walk()
        self.assertNotEqual(runer_first.distance, runer_second.distance)


if __name__ == '__main__':
    unittest.main()

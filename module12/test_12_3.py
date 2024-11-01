import unittest
from module12.module_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усэйн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(v)

    @unittest.skipIf(is_frozen, 'Тесты в данном кейсе заморожены')
    def test_start_first(self):
        t1 = Tournament(90, self.r1, self.r3)
        all_results = t1.start()
        self.update_all_result(all_results, 1)
        self.assertTrue(all_results.get(2) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в данном кейсе заморожены')
    def test_start_second(self):
        t1 = Tournament(90, self.r2, self.r3)
        all_results = t1.start()
        self.update_all_result(all_results, 2)
        self.assertTrue(all_results.get(2) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в данном кейсе заморожены')
    def test_start_third(self):
        t1 = Tournament(90, self.r1, self.r2, self.r3)
        all_results = t1.start()
        self.update_all_result(all_results, 3)
        self.assertTrue(all_results.get(3) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в данном кейсе заморожены')
    def test_start_fourth(self):
        t1 = Tournament(90, self.r3, self.r2)
        all_results = t1.start()
        self.update_all_result(all_results, 4)
        self.assertTrue(all_results.get(2) == 'Ник')

    @classmethod
    def update_all_result(cls, new_value, num):
        cls.all_results.update({num: new_value})


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        runer_test = Runner('Бегун гуляет')
        for call in range(10):
            runer_test.walk()
        self.assertEqual(runer_test.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        runer_test = Runner('Бегун бежит')
        for call in range(10):
            runer_test.run()
        self.assertEqual(runer_test.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        runer_first = Runner('Бегун первый')
        runer_second = Runner('Бегун второй')
        for call in range(10):
            runer_first.run()
            runer_second.walk()
        self.assertNotEqual(runer_first.distance, runer_second.distance)

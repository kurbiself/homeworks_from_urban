import unittest
from module12.module_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
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

    def test_start_first(self):
        t1 = Tournament(90, self.r1, self.r3)
        all_results = t1.start()
        self.update_all_result(all_results, 1)
        self.assertTrue(all_results.get(2) == 'Ник')

    def test_start_second(self):
        t1 = Tournament(90, self.r2, self.r3)
        all_results = t1.start()
        self.update_all_result(all_results, 2)
        self.assertTrue(all_results.get(2) == 'Ник')

    def test_start_third(self):
        t1 = Tournament(90, self.r1, self.r2, self.r3)
        all_results = t1.start()
        self.update_all_result(all_results, 3)
        self.assertTrue(all_results.get(3) == 'Ник')

    def test_start_fourth(self):
        t1 = Tournament(90, self.r3, self.r2)
        all_results = t1.start()
        self.update_all_result(all_results, 4)
        self.assertTrue(all_results.get(2) == 'Ник')


    @classmethod
    def update_all_result(cls, new_value, num):
        cls.all_results.update({num: new_value})

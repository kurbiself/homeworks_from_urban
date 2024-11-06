import logging
import unittest
from module12.module_12_2 import Runner

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w',
                    format='%(asctime)s | %(levelname)s | %(message)s',
                    encoding='utf-8')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runer_test = Runner('Вася', -5)
            for call in range(10):
                runer_test.walk()
            self.assertEqual(runer_test.distance, 50)
        except AssertionError:
            logging.info(f'Скорость бегуна не может быть отрицательной, у вас {runer_test.speed}', exc_info=True)

    def test_run(self):
        try:
            runer_test = Runner(22)
            if type(runer_test.name)!= str:
                raise TypeError('Имя должно быть строкой!')
            for call in range(10):
                runer_test.run()
            self.assertEqual(runer_test.distance, 100)
            logging.warning(f'Бегун {runer_test.name} бегает успешно со скоростью')
        except TypeError:
            logging.warning('Неверный тип данных', exc_info=True)

    def test_challenge(self):
        runer_first = Runner('Бегун первый')
        runer_second = Runner('Бегун второй')
        for call in range(10):
            runer_first.run()
            runer_second.walk()
        self.assertNotEqual(runer_first.distance, runer_second.distance)

from module_12_4 import Runner

from test_12_1 import RunnerTest

from unittest import TestCase

import logging


class RunnerTest(TestCase):
    def test_walk(self):
        try:
            runner = Runner("Dima", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner\n{e}")

    def test_run(self):
        try:
            runner = Runner(2)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)
        logging.info('"test_challenge" выполнен успешно')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_test.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

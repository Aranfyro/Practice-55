# Домашнее задание по теме "Простые Юнит-Тесты"
# Задача "Проверка на выносливость":
import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = Runner('First Runner')
        for x in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r2 = Runner('Second Runner')
        for x in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = Runner('Third Runner')
        r4 = Runner('Fourth')
        for x in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance,r4.distance)
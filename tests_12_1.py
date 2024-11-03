import runner as rn
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        _runner = rn.Runner("some name")
        for _ in range(10):
            _runner.walk()
        self.assertEqual(_runner.distance, 50)

    def test_run(self):
        _runner = rn.Runner("some name")
        for _ in range(10):
            _runner.run()
        self.assertEqual(_runner.distance, 100)

    def test_challenge(self):
        _runner1 = rn.Runner("name1")
        _runner2 = rn.Runner("name2")
        for _ in range(10):
            _runner1.run()
            _runner2.walk()
        self.assertNotEqual(_runner1.distance, _runner2.distance)


if __name__ == "__main__":
    unittest.main()

import unittest
from main import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting(), "Hello from GitHub Actions workflow")


if __name__ == "__main__":
    unittest.main()

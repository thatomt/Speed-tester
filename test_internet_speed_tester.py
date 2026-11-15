
import unittest
from internet_speed_tester import check_internet_speed


class TestInternetSpeed(unittest.TestCase):

    def test_speed_results(self):
        result = check_internet_speed()

        self.assertIn("download", result)
        self.assertIn("upload", result)
        self.assertIn("ping", result)


if __name__ == "__main__":
    unittest.main()
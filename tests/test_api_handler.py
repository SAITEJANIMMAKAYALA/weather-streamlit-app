import unittest
from weather.api_handler import get_weather

class TestWeatherAPI(unittest.TestCase):
    def test_response_structure(self):
        data = get_weather('London')
        self.assertIn('main', data)

if __name__ == '__main__':
    unittest.main()
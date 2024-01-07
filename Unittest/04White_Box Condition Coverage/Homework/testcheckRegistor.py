import unittest
from checkRegistor import CheckRegistor

class TestCheckRegistor(unittest.TestCase):

    def setUp(self) -> None:
        self.checkRegistor = CheckRegistor()

    def test_Decision_coverage(self):
        self.assertEqual(True, self.checkRegistor.register("abc@test.com","12345678",int(18)))
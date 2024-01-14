import unittest
from checkRegistor import CheckRegistor

class TestCheckRegistor(unittest.TestCase):

    def setUp(self) -> None:
        self.checkRegistor = CheckRegistor()

    def test_Decision_coverage(self):
        self.assertEqual(True, self.checkRegistor.register("abc@test.com","12345678",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abctest.com","1234567",int(17)))

    def test_Condition_coverage(self):
        self.assertEqual(False, self.checkRegistor.register("abctest.com","12345678",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abc@test.com","1234567",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abc@test.com","12345678",int(17)))

    def test_ConditionAndDecision_coverage(self):
        self.assertEqual(False, self.checkRegistor.register("abctest.com","12345678",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abc@test.com","1234567",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abc@test.com","12345678",int(17)))
        self.assertEqual(True, self.checkRegistor.register("abc@test.com","12345678",int(18)))

    def test_ModifiedConditionAndDecision_coverage(self):
        self.assertEqual(False, self.checkRegistor.register("abctest.com","12345678",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abc@test.com","1234567",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abc@test.com","12345678",int(17)))
        self.assertEqual(False, self.checkRegistor.register("abctest.com","1234567",int(17)))
        self.assertEqual(False, self.checkRegistor.register("abctest.com","12345678",int(17)))
        self.assertEqual(False, self.checkRegistor.register("abctest.com","1234567",int(18)))
        self.assertEqual(False, self.checkRegistor.register("abctest.com","1234567",int(17)))
        self.assertEqual(True, self.checkRegistor.register("abc@test.com","12345678",int(18)))

if __name__ == "__main__":
    unittest.main()
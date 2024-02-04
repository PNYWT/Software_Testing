import unittest
from template import *

# ทั้งหมดนี่เริ่มจากการเขียน TestTeamplate ก่อนจะมี Clas Template สำหรับทดสอบ
class TestTemplate(unittest.TestCase):

    def setUp(self):
        self.template = Template("Good Morning, ${firstname} ${lastname}")
        self.template.set("firstname","Callme")
        self.template.set("lastname","Oni")

    def test_evaluate_template_multiple_variable(self):
        self.assertEqual("Good Morning, Callme Oni", self.template.evaluate())

    def test_evaluate_unknow_variables_are_ignored(self):
        self.assertEqual("Good Morning, Callme Oni", self.template.evaluate())

    def test_evaluate_missing_value_raises_exception(self):
        with self.assertRaises(AttributeError):
            Template("Good Morning ${firstname}").evaluate()

unittest.main()
        


    # def test_evaluate_one_variable(self):
    #     template = Template("Hello, ${name}") #คิดตาม Requirement ว่าต้องส่งชื่อมา
    #     template.set("name","Reader") #เรียกใช้ Func set จริงที่จะเขียนต่อจากนี้
    #     self.assertEqual("Hello, Reader", template.evaluate()) #ทดสอบกับ Func จริงที่จะเขียนต่อจากนี้
    #     #Run แล้วต้อง Fail เมื่อเขียน class Template แล้ว -> AssertionError: 'Hello, Reader' != None
    #     #เสร็จแล้วครั้งที่สองให้ไป Hard code func evaluate -> return Hello, Reader

    # def test_evaluate_different_variable(self):
    #     template = Template("Hi, ${name}")
    #     template.set("name","Pun") 
    #     self.assertEqual("Hi, Pun", template.evaluate())

    # def test_evaluate_template_multiple_variable(self):
    #     template = Template("${greeting}, ${name}")
    #     template.set("greeting","Good Morning") 
    #     template.set("name","Oni")
    #     self.assertEqual("Good Morning, Oni", template.evaluate())
# HW no.1 -> 6614450042 ปัญญวัตร สุวรรณทัต
import unittest
from unittest.mock import Mock
from bank import BankAccount, Bank

class BankTest(unittest.TestCase):

    def test_transfer(self):
        # create mock objects
        mock_account_A = Mock()
        mock_account_B = Mock()
        mock_account_A.get_name.return_value = "A"
        mock_account_B.get_name.return_value = "B"
        #Stubbing name ใส่ให้ Mock() แต่ละตัว

        # create CUT and setting up
        bank = Bank("Test Bank")
        bank.add_account(mock_account_A)
        bank.add_account(mock_account_B)

        # call method under test
        bank.transfer("A", "B", 1000) # เรียกใช้ func transfer

        # ตรวจสอบที่ mock object
        # ตรวจสอบ withdraw, deposit ทำงานจริงไหม ใน func transfer
        mock_account_A.withdraw.assert_called_with(1000)
        mock_account_B.deposit.assert_called_with(1000)

        #--------------------------
        # ลองทดสอบ deposit
        mock_account_A.deposit(1000)
        mock_account_A.deposit.assert_called_with(1000) # ลองทดสอบ deposit ทำงานหรือไม่

    def test_give_interest_all(self): # คล้ายกับ Examplay employee Slide page 18
        # create mock objects
        mock_account_A = Mock()
        mock_account_A.get_name.return_value = "A" # Stubbing Account name -> "A" เป็น Hardcode สำหรับกำหนดชื่อให้ Mack()

        # create CUT Bank and setting up
        # add_interest จะใช้งานได้ต้องมี Account ก่อน ต้องทำการเพิ่ม Mack() ชื่อบัญชี "A"
        # เข้าไปใน add_account ก่อน
        bank = Bank("BankHomeWork")
        bank.add_account(mock_account_A) # เพิ่ม Mock() Account "A" ผ่าน func add_account

        # call method under test
        bank.give_interest_all(0.1) # เรียกใช้ give_interest_all

        # ตรวจสอบที่ mock object
        mock_account_A.add_interest.assert_called_with(0.1) #ตรวจสอบว่า add_interest ใน Class BankAccount ถูกเรียด้วย rate = 0.1 หรือไม่
        
unittest.main()

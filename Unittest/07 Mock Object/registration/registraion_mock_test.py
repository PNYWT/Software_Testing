# HW no.1 -> 6614450042 ปัญญวัตร สุวรรณทัต
import unittest
from unittest.mock import Mock
from registration import RegistrationService, PasswordEncoder, UserRepository

class RegistrationTest(unittest.TestCase):

    #Step1 RegistrationService.register(username, password)
    #Step2 RegistrationService.register check
    # if UserRepository.is_username_available(username)
    # Step3  PasswordEncoder.hash(password) working <- Is it work?
    def test_register_hash(self):

        stub_UserRepository = Mock() #UserRepository
        mock_PasswordEncoder = Mock() #PasswordEncoder
        
        # เชื่อม Mock() กับ CUT
        registration_service = RegistrationService(mock_PasswordEncoder, stub_UserRepository)

        # เพิ่มค่า stub_UserRepository
        stub_UserRepository.is_username_available.return_value = True

        #call func register
        registration_service.register(stub_UserRepository, "password123")

        # verify mock
        mock_PasswordEncoder.hash.assert_called_once_with("password123")

unittest.main()
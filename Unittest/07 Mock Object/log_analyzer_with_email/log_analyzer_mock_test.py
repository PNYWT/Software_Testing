import unittest
from unittest.mock import Mock
from log_analyzer import LogAnalyzer, WebService

class LogAnalyzerTest(unittest.TestCase):

    def test_analyze_webservice_throw_send_email(self):
        # mock and stub creation
        stub_web = Mock()
        mock_email = Mock()

        # stubbing
        stub_web.log_error.side_effect = Exception("fake exception")

        # CUT and setting up + calling method under test
        analyzer = LogAnalyzer(stub_web, mock_email)
        analyzer.analyze("abc.ext")
		
        # ตรวจสอบที่ mock object
        mock_email.send.assert_called_with("admin@xyz.com", "subject", "fake exception")



unittest.main()

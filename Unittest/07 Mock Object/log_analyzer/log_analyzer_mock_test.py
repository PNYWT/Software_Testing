import unittest
from unittest.mock import Mock
from log_analyzer import LogAnalyzer, WebService

class LogAnalyzerTest(unittest.TestCase):

    def test_analyze_too_short_filename_call_webservice(self):
        mock_service = Mock()
        analyzer = LogAnalyzer(mock_service)
        analyzer.analyze("abc.ext")
		
        mock_service.log_error.assert_called_with("Filename too short: abc.ext")

unittest.main()

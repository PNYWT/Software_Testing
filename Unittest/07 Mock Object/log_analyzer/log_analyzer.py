class LogAnalyzer:    # CUT
	
    def __init__(self, web_service):
        self.web_service = web_service

    def analyze(self, file_name):
        if len(file_name) < 8:
            self.web_service.log_error("Filename too short: "+file_name)

class WebService:

    def log_error(self, message):
        pass


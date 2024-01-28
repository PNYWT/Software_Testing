class LogAnalyzer:    # CUT
	
    def __init__(self, web_service, email_service):
        self.web_service = web_service
        self.email_service = email_service

    def analyze(self, file_name):
        if len(file_name) < 8:
            try:
                self.web_service.log_error("Filename too short: " + file_name)
            except Exception as e:
                self.email_service.send("admin@xyz.com", "subject", str(e))

class WebService:

    def log_error(self, message):
        pass

class EmailService:

    def send(self, to, subject, body):
        pass

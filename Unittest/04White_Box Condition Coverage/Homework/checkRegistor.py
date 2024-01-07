class CheckRegistor:

    def __init__(self):
        return
    
    def register(self,email, password, age) -> bool:
        if email.index("@") >= 1 and len(password) >= 8 and age >= 18:
            return True
        return False
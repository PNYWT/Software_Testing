class RegistrationService:

    def __init__(self, password_encoder, user_repository):
        self.password_encoder = password_encoder
        self.user_repository = user_repository

    def register(self, username, password):
        if self.user_repository.is_username_available(username):
            hashed_password = self.password_encoder.hash(password)
            self.user_repository.add_user_to_database(username,hashed_password)

class PasswordEncoder:
    def hash(self, password):
        pass

class UserRepository:

    def is_username_available(self, username):
        pass

    def add_user_to_database(self, username,  hash_password):
        pass

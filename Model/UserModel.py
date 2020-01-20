from Database.ConnectionModel import ConnectionModel


class UserModel:
    def __init__(self):
        self.bank_collection = ConnectionModel.connect("user_transaction")

    def user_authentication(self, email, password):
        result = self.bank_collection.find_one({"email": email, "password": password}, {"role": 1})
        if result:
            return result
        else:
            return False

    def user_registration(self, name, email, password, role):
        result = self.bank_collection.count({"email": email})
        if result: return "User Already Exists"
        result = self.bank_collection.insert_one({"name": name, "email": email, "password": password, "role": role, "total_balance": 0, "debit_transaction": [], "credit_transaction": []})
        if result.inserted_id:
            return "Registration Process Completed."
        else:
            return "Try Again!!"



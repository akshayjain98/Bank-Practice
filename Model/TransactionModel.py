from datetime import datetime
from Database.ConnectionModel import ConnectionModel
from bson import ObjectId

class TransactionModel:
    def __init__(self):
        self.bank_collection = ConnectionModel.connect("user_transaction")

    def debit_transaction(self, customer_id, amount):
        transaction_detail = {"amount": amount, "transaction_time": datetime.utcnow()}
        result = self.bank_collection.update_one(
            {"_id": customer_id, "total_balance": {"$gte": amount}},
            {
                "$push": {"debit_transaction": transaction_detail},
                "$inc": {"total_balance": -amount}
            })
        if result.modified_count > 0:
            return "Transaction Completed"
        else:
            return "Transaction Fail"

    def credit_transaction(self, customer_id, amount):
        transaction_detail = {"amount": amount, "transaction_time": datetime.utcnow()}
        result = self.bank_collection.update_one({"_id": customer_id}, {
            "$push": {"credit_transaction": transaction_detail}, "$inc": {"total_balance": amount}})
        if result.modified_count > 0:
            return "Transaction Completed"
        else:
            return "Transaction Fail"

    def user_transactions(self, email):
        result = self.bank_collection.find_one({"role": "U", "email": email},{"name": 1, "_id": 0, "email": 1, "total_balance": 1, "debit_transaction": 1, "credit_transaction": 1})
        if result:
            return result
        else:
            return "No Record Found"

    def total_balance(self, customer_id):
        result = self.bank_collection.find_one({"role": "U", "_id": ObjectId(customer_id)},{"name": 1, "_id": 0, "email": 1, "total_balance": 1})
        if result:
            return result
        else:
            return "No Record Found"
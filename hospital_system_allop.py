import threading
class InsufficientPayment(Exception):
    pass
class Patient:
    def __init__(self,id,name,age,disease,fee):
        count=0
        self.id=id
        self.name=name
        self.age=age
        self.disease=disease
        self.__fee=fee
        self.lock=threading.Lock()
        self.__paid_amount=0
    def get_fee(self):
        return self.__fee
    def set_fee(self,fee):
        self.__fee=fee
    def display(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Fee:",self.__fee)
        print("Disease:",self.disease)
    def pay_amount(self,amount):
        if amount<=0:
            raise ValueError("Invalid amount")
        with self.lock:
            pending=self.pending_amt()
            if amount>pending:
                raise InsufficientPayment("Amount is greater than pending amount")
            self.paid_amount+=amount
            print("Payment successful")
    def pending_amount(self):
        return self.__fee-self.__paid_amount
    def consultation_charge(self):
        return 0
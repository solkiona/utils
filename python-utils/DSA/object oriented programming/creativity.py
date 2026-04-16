

class Person1:
    """Old way without the @property decorator in making a getter and setter
    """
    
    def __init__(self):
        self._name = ""
    
    
    def get_name(self):
        print("this is get name called")
        return self._name
    
    def set_name(self, value):
        "This is the setter method being called"
        self._name = value 
        
    name = property(get_name, set_name)


class Person:
    """
    New way with the @property decorator in making a getter and setter
    
    note both the getter and setter must have same name
    """
    def __init__(self):
        self._name = ""
        
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


class Person3:
    def __init__(self):
        self._name = ""

    @property
    def retrieve_name(self):   # getter
        print("Getter called!")
        return self._name

    @retrieve_name.setter
    def lets_set_name(self, value):   # setter
        print("Setter called!")
        self._name = value

class CreditCard:
    """
    A consumer credit card
    
    """
    def __init__(self, customer, bank , acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._acnt
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Prcoess customer payment that reduces balance"""
        self._balance -= amount
        

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California savings', '5391 0375 5309 ', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))
    
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
            print()
class CashRegister:
    '''CashRegister class to manage a cash register system.'''

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  # 🆕 Track the last transaction amount

    def add_item(self, title, price, quantity=1):
        '''Adds an item to the register and updates the total.'''
        transaction_total = price * quantity
        self.total += transaction_total
        self.last_transaction_amount = transaction_total  # 🆕 Save this
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        '''Subtracts the last transaction amount from total.'''
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0  # Reset after voiding

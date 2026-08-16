class BankAtm:

    def __init__(self):
        self.pin = " "
        self.balance = 0

    def Menu(self):
        print("1. Enter 1 to Set Pin")
        print("2. Enter 2 to Check Balance")
        print("3. Enter 3 to Deposite Money")
        print("4. Enter 4 to Withdraw Money")
        print("5. Enter 5 to Change Pin")
        print("6. Enter 6 to Exit")

        choice = int(input("enter Your Choice :"))

        match choice:
            case 1:
                self.set_pin()

            case 2:
                self.check_balance()

            case 3:
                self.deposit_money()

            case 4:
                self.withdraw_money()

            case 5:
                self.change_pin()

            case 6:
                self.exit_menu()

    def set_pin(self):
        if self.pin==" ":
            input_pin = input("enter pin :")
            self.pin = input_pin
            print("pin set",self.pin)
            self.Menu()

        else:
            print("pin is already set")
            self.Menu()


    def check_balance(self):
        userPin = input("enetr your pin :")

        if self.pin == userPin:
            print("your balance is :",self.balance)
            self.Menu()
        else:
            print("invalid pin")
            self.Menu()


    def deposit_money(self):
        userPin = input("enetr your pin :")

        if self.pin == userPin:
            input_ammount = int(input("enter ammout for deposite :"))
            self.balance += input_ammount
            print("your bank balance is :",self.balance)
            self.Menu()

        else:
            print("invalid pin")
            self.Menu()



    def withdraw_money(self):
        userPin = input("enetr your pin :")

        if self.pin == userPin:
            withdraw_ammount =  int(input("enter ammount to withdraw :"))

            if withdraw_ammount <= self.balance:
                self.balance -= withdraw_ammount
                print("your bank balance is:",self.balance)
                self.Menu()


            else:
                print("insufficint fund")
                self.Menu()

        else:
            print("invalid pin")
            self.Menu()



    def change_pin(self):
        oldPin = input("enter your old pin :")

        if oldPin == self.pin:
            newpin = input("enter new pin :")
            self.pin = newpin
            print("pin updated :",self.pin)
            self.Menu()

        else:
            print("old pin is not match")
            self.Menu()


    def exit_menu(self):
        print("thak you")



obj1 = BankAtm()
obj1.Menu()

import datetime

class Record:
    def __init__(self):
        self.date_of_register = datetime.date.today()
        self.date_of_stay = datetime.date(2020,1,1)
        self.amount = 0

    def show(self):
        li = [self.date_of_register,
              self.date_of_stay,
              self.amount]
        # print(self.date_of_register)
        # print(self.date_of_stay)
        # print(self.amount)
        for content in li:
            print(content, end='')
            if content != li[-1]:
                print(',',end='')
        print()

    def register(self):
        self.amount = int(input())

    def loss(self):
        print("loss")

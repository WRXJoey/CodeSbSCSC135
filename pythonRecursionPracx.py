def star_string(n):
    if n == 0:
        return '*'
    elif n < 0:
        raise ValueError()
    else:
        smaller_star = star_string(n-1)
        return smaller_star + smaller_star
test1 = star_string(3) 
print(test1)

def digit_sum(num):
    if not num:
        return 0
    elif num < 0 :
        return -digit_sum(-num)
    else:
        return int(num % 10) + digit_sum(int(num / 10))
test2 = digit_sum(1729) 
print(test2)  

def stutter_list(listnum,index = 0):
    if index >= len(listnum):
        return []
    else:
        listnum.insert(index + 1, listnum[index])
        stutter_list(listnum, index + 2)
test3 = stutter_list([13, 27, 1, -4, 0, 9])
print(test3)

def reverse(string):
    if not string:
        return string 
    else:
        return reverse(string[1:]) + string[0]
test4 = reverse("Hi you!")
print(test4)


##this wont run, just an example of a python class
class BankAccount:
    def __init__(self,name = none,balance = 0):
        self._name = name
        self._balance = balance
    def deposit(self, amount):
        if amount < 0:
            return
        else:
            balance = (self.amount + self.balance)
    def withdraw(self,amount):
        if amount < 0:
            return
        elif amount > self.balance:
            return
        else:
            balance = (self.balance - self.amount)
import account

acc1 = account.Account(999)
print(acc1)
acc1.getfunds()
acc1.deposit(1)
acc1.check_withdrawal(999)
acc1.check_withdrawal(1001)
acc1.withdraw(800)
acc1.withdraw(300)
acc1.calc_interest(365)

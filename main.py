from User import User
percy = User("Percy", "che.percy.l@gmail.com")
mery = User("Mery", "meryche@gmail.com")
samantha = User("Samantha", "samantha.che.inolopu@gmail.com")
percy.make_deposit(100).make_deposit(200).make_deposit(300).make_transfer(mery, 100)
mery.make_deposit(100).make_deposit(200).make_transfer(samantha, 100).make_transfer(percy, 100)
percy.show_account_balance()
mery.show_account_balance()
samantha.show_account_balance()
samantha.make_deposit(400).make_transfer(percy, 100).make_transfer(mery, 100).make_transfer(percy, 200)
percy.show_account_balance()
mery.show_account_balance()
samantha.show_account_balance()
percy.make_withdrawal(100)
mery.make_withdrawal(100)
samantha.make_withdrawal(100)
percy.show_account_balance()
mery.show_account_balance()
samantha.show_account_balance()
"""
File: atm2.py
This module defines a GUI-based ATM class and its application.
To test, launch from IDLE and run
>>> createBank(5)
>>> main()
Can be modified to run as a script after a bank has been saved.
"""

from bank2 import Bank, SavingsAccount
from tkinter import *

class ATM(Frame):
	"""This class represents GUI-based ATM transactions."""
        
	
	def __init__(self, bank):
		"""Initialize the frame, widgets, and the data model."""
		Frame.__init__(self, bg = "blue")
		self.master.title("ATM")
		self.master.geometry("200x100")
		self.grid()
		self._account = None
		self._bank = bank
		
		# Create and add the widgets to the frame.
		# Data containers for entry fields
		self._nameVar = StringVar()
		self._pinVar = StringVar()
		self._amountVar = DoubleVar()
		self._statusVar = StringVar()

		# Labels for entry fields
		self._nameLabel = Label(self, text = "Name", fg = "red", bg = "#cccccc")
		self._nameLabel.grid(row = 0, column = 0)
		self._pinLabel = Label(self, text = "PIN")
		self._pinLabel.grid(row = 1, column = 0)
		self._amountLabel = Label(self, text = "Amount")
		self._amountLabel.grid(row = 2, column = 0)
		self._statusLabel = Label(self, text = "Status")
		self._statusLabel.grid(row = 3, column = 0)

		# Entry fields
		self._nameEntry = Entry(self,
								textvariable = self._nameVar,
								justify = CENTER)
		self._nameEntry.grid(row = 0, column = 1)
		self._pinEntry = Entry(self,
							   textvariable = self._pinVar, 
							   justify = CENTER)
		self._pinEntry.grid(row = 1, column = 1)
		self._amountEntry = Entry(self,
								  textvariable = self._amountVar, 
								  justify = CENTER)
		self._amountEntry.grid(row = 2, column = 1)
		self._statusEntry = Entry(self,
								  textvariable = self._statusVar, 
                                  justify = CENTER)
		self._statusEntry.grid(row = 3, column = 1)

		# Command buttons
		self._balanceButton = Button(self,
									text = "Balance",
									command = self._getBalance)
		self._balanceButton["state"] = DISABLED
		self._balanceButton.grid(row = 0, column = 2)
		self._depositButton = Button(self, text = "Deposit",
									 command = self._deposit)
		self._depositButton["state"] = DISABLED
		self._depositButton.grid(row = 1, column = 2)
		self._withdrawButton = Button(self, text = "Withdraw",
									  command = self._withdraw)
		self._withdrawButton["state"] = DISABLED
		self._withdrawButton.grid(row = 2, column = 2)
		self._loginButton = Button(self, text = "Login",
								   command = self._login)
		self._loginButton.grid(row = 3, column = 2)


	def _getBalance(self):
		self._statusVar.set("Your balance is $%0.2f" % \
							(self._account.getBalance()))

	def _deposit(self):
		amount = self._amountVar.get()
		self._account.deposit(amount)
		self._statusVar.set("Deposit successful")
	def _withdraw(self):
		amount = self._amountVar.get()
		message = self._account.withdraw(amount)
		if message:
			self._amountVar.set(message)
		else:
			self._statusVar.set("Withdrawal Successful")

	def _login(self):
	
		name =  self._nameVar.get()
		pin =  self._pinVar.get()
		self._account = self._bank.get(pin)
		if self._account:
			if self._account.getName() == name:
				self._statusVar.set("Welcome to the bank!")
				self._loginButton["text"] = "Logout"
				self._loginButton["command"] = self._logout
				self._balanceButton["state"] = NORMAL
				self._depositButton["state"] = NORMAL
				self._withdrawButton["state"] = NORMAL
			else: 
				self._statusVar.set("Error, unrecognized name")
				self._account == None
		else:
			self._statusVar.set("Unrecognized pin")

	def _logout(self):
		self._account = None
		self._nameVar.set("")
		self._pinVar.set("")
		self._amountVar.set(0.0)
		self._loginButton["text"] = "Login"
		self._loginButton["command"] = self._login
		self._balanceButton["state"] = DISABLED
		self._depositButton["state"] = DISABLED
		self._withdrawButton["state"] = DISABLED
		self._statusVar.set("Have a nice day!")

# Top-level functions	
def main():
	"""Instantiate a Bank and an ATM and run it."""

	bank = Bank()
	bank.add(SavingsAccount('Samuel', "7777", 1000.00))
	bank.add(SavingsAccount('Ayo', "6565", 20.00))
	print("The bank has been loaded")
	atm = ATM(bank)
	print("Running the GUI")
	atm.mainloop()
	
	bank.save()
	print("The bank has been updated")

def createBank(number = 0):
	bank = Bank()
	for i in range(number):
		bank.add(SavingsAccount('Name' + str(i + 1), str(1000 + i), 100.00))
	bank.save("bank.dat")
		
		
		

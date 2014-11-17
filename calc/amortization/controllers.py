
from amortization.models import Loan
import math

class Payment:
	def __init__(self, number, principal, interest, cumulative_principal, cumulative_interest, principal_balance):
		self.number = number
		self.principal = principal
		self.interest = interest
		self.cumulative_principal = cumulative_principal
		self.cumulative_interest = cumulative_interest
		self.principal_balance = principal_balance

class Schedule:
	def __init__(self, loan):
		self._loan = loan
		self.payments = []

		self.total_interest_paid = loan.principal*loan.annual_interest_rate
		self.total_repaid = loan.principal + self.total_interest_paid

		# linear amortization
		monthly_interest = math.floor(100*self.total_interest_paid/loan.number_of_months)/100
		monthly_principal =  math.floor(100*loan.principal/loan.number_of_months)/100
		cumulative_principal = 0.0
		cumulative_interest = 0.0
		principal_balance = loan.principal

		# months 1 through 11
		for number in range(loan.number_of_months - 1):
			cumulative_principal += monthly_principal
			cumulative_interest += monthly_interest
			principal_balance -= monthly_principal
			self.payments += [ Payment(
				number+1,
				monthly_principal,
				monthly_interest,
				cumulative_principal,
				cumulative_interest,
				math.ceil(100*principal_balance)/100) ]

		# last payment (month 12)
		self.payments += [ Payment(
			loan.number_of_months,
			math.ceil(100*principal_balance)/100,
			self.total_interest_paid - cumulative_interest,
			loan.principal,
			self.total_interest_paid,
			0.0) ]

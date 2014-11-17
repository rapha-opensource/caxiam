from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from amortization.models import Loan
from amortization.controllers import Schedule

def browse(request):
	all_loans = Loan.objects.all()
	return render(request, 'loans/browse.html', {'all_loans': all_loans})

def read(request, loan_id):
	loan = get_object_or_404(Loan, id=loan_id)
	s = Schedule(loan)
	return render(request, 'loans/read.html', {'schedule': Schedule(loan)})

def add(request):
	return render(request, 'loans/add.html', {})

def new(request):
	new_loan = Loan(
			title_text  = request.POST['title'],
			principal = request.POST['principal'],
			number_of_months = request.POST['months'],
			annual_interest_rate = request.POST['rate']
			)
	new_loan.save()
	return render(request, 'loans/new.html', {
		'title': new_loan.title_text,
		'principal': new_loan.principal,
		'months': new_loan.number_of_months,
		'rate': new_loan.annual_interest_rate
		})

# TODO: add 'Delete' (DELETE) and 'Edit' (PUT) handlers

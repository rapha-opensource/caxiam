from django.contrib import admin

from amortization.models import Loan

class LoanAdmin(admin.ModelAdmin):
	list_display = ('title_text', 'principal', 'number_of_months', 'annual_interest_rate')

admin.site.register(Loan, LoanAdmin)

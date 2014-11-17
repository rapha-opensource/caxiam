from django.db import models

class Loan(models.Model):
	title_text = models.CharField(max_length=500)
	principal = models.FloatField(default=1000000)
	number_of_months = models.IntegerField(default=12)
	annual_interest_rate = models.FloatField(default=0.03)

	def __str__(self):
		return self.title_text

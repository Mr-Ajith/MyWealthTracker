from django.db import models

# Create your models here.

class MainDashboard(models.Model):
    userId = models.CharField(max_length=25, primary_key=True)
    savings = models.FloatField(null=True, blank=True)
    fixedDeposit = models.FloatField(null=True, blank=True)
    mutualFund = models.FloatField(null=True, blank=True)
    stock = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        result=''
        result+=str(self.userId)
        savings=str(self.savings)
        fd=str(self.fixedDeposit)
      
        result+="\t"+savings+"\n"+fd+"\n"
        return result
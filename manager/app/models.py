from django.db import models

# Create your models here.
class Expense(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    title = models.TextField(max_length=1000, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    


    def __str__(self):
        if (self.title or self.id):
            return (self.title + "  ( id = " + str(self.id) + "  )")
        

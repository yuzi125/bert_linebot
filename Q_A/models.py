from django.db import models

# Create your models here.
class QA(models.Model):
    
    question = models.CharField(max_length=1000,null=False)
    answer = models.CharField(max_length=1000,null=False)
    
    class Meta:
        db_table = "web_QA"
   
    def _Q(self):
        return self.question
    def _A(self):
        return self.answer

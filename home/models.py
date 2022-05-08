from django.db import models


class todo(models.Model):
    title=models.TextField(max_length=8000,blank=False)
    content=models.TextField(max_length=5000000,blank=True)
    date=models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return str(self.date)
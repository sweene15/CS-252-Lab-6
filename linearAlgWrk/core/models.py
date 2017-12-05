from django.db import models
from django.utils import timezone
# Create your models here.

class Input(models.Model):
    input_str = models.TextField()
    queried_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.input_str

class Var(models.Model):
    row_length = models.IntegerField()
    col_length = models.IntegerField()
    row1 = models.ForeignKey('Row', related_name = 'row1', on_delete=models.CASCADE,)
    row2 = models.ForeignKey('Row', related_name = 'row2', on_delete=models.CASCADE,)
    row3 = models.ForeignKey('Row', related_name = 'row3', on_delete=models.CASCADE,)
    row4 = models.ForeignKey('Row', related_name = 'row4', on_delete=models.CASCADE,)
    row5 = models.ForeignKey('Row', related_name = 'row5', on_delete=models.CASCADE,)
    pass

class Row(models.Model):
    row_length = models.IntegerField()
    element1 = models.IntegerField()
    element2 = models.IntegerField()
    element3 = models.IntegerField()
    element4 = models.IntegerField()    
    element5 = models.IntegerField()
    pass

class Output(models.Model):
    number_of_steps = models.IntegerField()
    step1 = models.ForeignKey('Step', related_name = 'step1', on_delete=models.CASCADE,)
    step2 = models.ForeignKey('Step', related_name = 'step2', on_delete=models.CASCADE,)
    step3 = models.ForeignKey('Step', related_name = 'step3', on_delete=models.CASCADE,)
    step4 = models.ForeignKey('Step', related_name = 'step4', on_delete=models.CASCADE,)
    step5 = models.ForeignKey('Step', related_name = 'step5', on_delete=models.CASCADE,)
    step6 = models.ForeignKey('Step', related_name = 'step6', on_delete=models.CASCADE,)
    step7 = models.ForeignKey('Step', related_name = 'step7', on_delete=models.CASCADE,)
    step8 = models.ForeignKey('Step', related_name = 'step8', on_delete=models.CASCADE,)
    step9 = models.ForeignKey('Step', related_name = 'step9', on_delete=models.CASCADE,)
    step10 = models.ForeignKey('Step', related_name = 'step10', on_delete=models.CASCADE,)
    step11 = models.ForeignKey('Step', related_name = 'step11', on_delete=models.CASCADE,)
    step12 = models.ForeignKey('Step', related_name = 'step12', on_delete=models.CASCADE,)

class Step(models.Model):
    startVar = models.ForeignKey('Var', related_name = 'startVar', on_delete=models.CASCADE,)
    endVar = models.ForeignKey('Var', related_name = 'endVar', on_delete=models.CASCADE,)
    step_str = models.TextField()
    pass

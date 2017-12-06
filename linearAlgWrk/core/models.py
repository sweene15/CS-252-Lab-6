from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

INPUT_CHOICES = (
    ('add', 'ADD'),
    ('multiply', 'MULTIPLY'),
    ('rref', 'RREF'),
    ('determinant', 'DETERMINANT'),
    ('inverse', 'INVERSE'),
)
SIZE_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Var(models.Model):
    row_length = models.IntegerField(null=True)
    col_length = models.IntegerField(null=True)
    row1 = models.ForeignKey('Row', related_name = 'row1', null=True, on_delete=models.CASCADE,)
    row2 = models.ForeignKey('Row', related_name = 'row2', null=True, on_delete=models.CASCADE,)
    row3 = models.ForeignKey('Row', related_name = 'row3', null=True, on_delete=models.CASCADE,)
    row4 = models.ForeignKey('Row', related_name = 'row4', null=True, on_delete=models.CASCADE,)
    row5 = models.ForeignKey('Row', related_name = 'row5', null=True, on_delete=models.CASCADE,)
    pass


class Input(models.Model):
    col_size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='3')
    row_size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='3')
    input_type = models.CharField(max_length=12, choices=INPUT_CHOICES)
    queried_date = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.input_type

class Row(models.Model):
    row_length = models.IntegerField(null=True)
    element1 = models.IntegerField(null=True)
    element2 = models.IntegerField(null=True)
    element3 = models.IntegerField(null=True)
    element4 = models.IntegerField(null=True)    
    element5 = models.IntegerField(null=True)
    pass

class Output(models.Model):
    startVar = models.ForeignKey('Var', related_name = 'startVar', null=True, on_delete=models.CASCADE,)
    endVar = models.ForeignKey('Var', related_name = 'endVar', null=True, on_delete=models.CASCADE,) 



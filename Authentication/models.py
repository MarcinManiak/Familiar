from django.db import models


class Member(models.Model):
    member = models.CharField(max_length=128)

    def __str__(self):
        return self.member

class Family(models.Model):
    name = models.CharField(max_length=128, help_text='Name your family')
    description = models.TextField(blank=True, help_text='Optional - what is amazing about you folks?')
    members = models.ManyToManyField(Member)

    def __str__(self):
        return f'{self.pk} {self.name}'

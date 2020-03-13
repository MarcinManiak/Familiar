from django.db import models


class Member(models.Model):
    member = models.CharField(max_length=128)

    def __str__(self):
        return self.member

class Family(models.Model):
    name = models.CharField(max_length=128, help_text='Jak nazywa się Waza rodzina')
    description = models.TextField(blank=True, help_text='Opcjonalne, ale na pewno czym szczególnym się odznaczacie :) ')
    members = models.ManyToManyField(Member)

    def __str__(self):
        return f'{self.pk} {self.name}'

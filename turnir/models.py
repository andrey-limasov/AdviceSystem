from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from AdviceSystem import settings


class FlagType(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=150, help_text='Enter flag descr')
    # …

    # # Methods
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of MyModelName."""
    #     return reverse('model-flagtype-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.description


class Flag(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(FlagType, on_delete=models.CASCADE, )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    hash = models.BigIntegerField(help_text='Enter flag hash')
    captured = models.BooleanField(help_text='Flag is captured', default=False)
    capture_time = models.DateTimeField(help_text='Time of capture')
    # …

    # # Methods
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of MyModelName."""
    #     return reverse('model-flag-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user_id.__str__() + ' ' + self.type_id_id.__str__() + ' ' + self.hash.__str__()


class Advice(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    id = models.AutoField(primary_key=True)
    order = models.IntegerField(help_text='Order of advice')
    description = models.CharField(max_length=500, help_text='Enter flag descr')
    showtime = models.DateTimeField(help_text='Time to show')
    penalty = models.IntegerField(help_text='Penalty for advice')
    # …

    # Metadata
    class Meta:
        ordering = ['order']

    # # Methods
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of MyModelName."""
    #     return reverse('model-advice-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.description


class UserAdvice(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    id = models.AutoField(primary_key=True)
    advice_id = models.ForeignKey(Advice, on_delete=models.CASCADE, )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    showed = models.BooleanField(help_text='Has showed', default=False)
    notneed = models.BooleanField(help_text='Not need advice', default=False)
    take_time = models.DateTimeField(help_text='Time of taking advice')
    # …

    # # Methods
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of MyModelName."""
    #     return reverse('model-useradvice-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user_id.__str__() + ' ' + self.advice_id.__str__()

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dbname = models.CharField(max_length=100)
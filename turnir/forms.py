from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


class RegisterFlagForm(forms.Form):
    flag_hash = forms.IntegerField(help_text="Enter the flag.", required=True, label="Enter the flag")

    def clean_renewal_date(self):
        data = self.cleaned_data['flag_hash']

        # Check if a date is not in the past.
        if data.isnumeric():
            raise ValidationError(_('%(data)s is not an number'), params={'value': data},)

        # Remember to always return the cleaned data.
        return data


# def validate_int(value):
#     if value.isnumeric():
#         raise ValidationError(('%(value)s is not an number'),
#             params={'value': value},
#         )
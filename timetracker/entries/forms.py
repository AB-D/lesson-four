from django import forms


from .models import Project, Client, Entry
from django.db import models
from django.utils import timezone





class EntryForm(forms.Form):
    start = forms.DateTimeField(label="Start Time", help_text="Format: 2006-10-25 14:30")
    end = forms.DateTimeField(label="End Time", help_text="Format: 2006-10-25 14:30")
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    description = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super(EntryForm, self).clean()
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        now = timezone.now()

        if start >= now or start >= end:
            raise forms.ValidationError("Start time must be in the past, end time must be after start time")
        return cleaned_data

#using these functions below would create a 'Nonetype() >= datetime()' error. The only way i could
#get rid of that was to put them in one function which means that the error output might be confusing
#for the user.
    '''def clean_start(self):
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        now = timezone.now()
        if start >= now:
    	    raise forms.ValidationError("Start time must be in the past")
        return start


    def clean_end(self):
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        if start >= end:
            raise forms.ValidationError("Start time must be before end time")
        return end'''


class ProjectForm(forms.Form):
  	client = forms.ModelChoiceField(queryset=Client.objects.all())
  	name = forms.CharField(max_length=100)

class ClientForm(forms.Form):
	name = forms.CharField(max_length=100)

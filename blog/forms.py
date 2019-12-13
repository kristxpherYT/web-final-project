from django import forms
from .models import Project, Hobby


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'image_path')


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ('name', 'image_path')
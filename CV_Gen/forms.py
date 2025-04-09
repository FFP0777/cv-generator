# CV_Gen/forms.py
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'email', 'phone',
            'summary', 'skills', 'previous_work',
            'degree', 'school', 'university', 'photo'
        ]
        widgets = {
            'summary': CKEditorWidget(),
            'skills': CKEditorWidget(),
            'previous_work': CKEditorWidget(),
        }

from django import forms
from .models import  Comment, Alert

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment here...'}),
        }


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['title', 'alert_image','message', 'valid_until']

    valid_until = forms.DateTimeField(
        widget=forms.DateInput
        (attrs={'type': 'datetime-local',
                'class': 'datetimepicker'})
    )
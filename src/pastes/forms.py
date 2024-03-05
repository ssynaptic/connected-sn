from django import forms
from pastes.models import Paste

class CreatePasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = [
        "title", "content",
        "author", "slug"
        ]
class UpdatePasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ["title", "content", "slug"]

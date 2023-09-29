from django import forms
from app.models import Game
from django.core.exceptions import ValidationError


class GameEditForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'description', 'publisher', 'studio', 'genre', 'review_score', 'music_file', 'system')  # fmt: skip

    def clean_publisher(self):
        data = self.cleaned_data["publisher"]
        if data.startswith("123"):
            raise ValidationError("Publisher must not start with '123'")

        return data


class GameEditTitleForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ("title",)

    def clean_title(self):
        data = self.cleaned_data["title"]
        if data.startswith("123"):
            raise ValidationError("title must not start with '123'")

        return data


class GuestbookForm(forms.Form):

    uuid = forms.CharField(widget=forms.HiddenInput)
    name = forms.CharField(required=True)
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "onKeyUp": "checkLength()"
                # "data-charlimit-target": "commentField",
                # "data-action": "input->charlimit#check",
            }
        )
    )

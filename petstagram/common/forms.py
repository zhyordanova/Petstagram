from django import forms

from petstagram.common.models import Comment
from petstagram.core.utils import get_pet_by_pk


class CommentForm(forms.ModelForm):
    pet_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text', 'pet_pk')

    def save(self, commit=True):
        pet_pk = self.cleaned_data['pet_pk']
        pet = get_pet_by_pk(pk=pet_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            pet=pet,
        )

        if commit:
            comment.save()

        return comment



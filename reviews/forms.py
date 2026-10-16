from django import forms
from reviews.models import Review


class ReviewBaseForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

class ReviewCreateForm(ReviewBaseForm):
    ...
class ReviewEditForm(ReviewBaseForm):
    ...
class ReviewDeleteForm(ReviewBaseForm):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        for name in self.fields:
            self.fields[name].disabled = True

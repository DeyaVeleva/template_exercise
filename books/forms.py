from django import forms

from books.models import Book, Tag


class BookBaseForm(forms.ModelForm):
    tags= forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    field_order = {
        # the order with 'attribute',
    }
    class Meta:
        model = Book
        exclude = ('slug',)

class BookCreateForm(BookBaseForm):
    ...

class BookEditForm(BookBaseForm):
    ...

class BookDeleteForm(BookBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True

class SearchBookForm(forms.Form):
    query=forms.CharField(
        max_length=100,
        required=False,
    )
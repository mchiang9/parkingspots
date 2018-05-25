from django import forms
from django.forms import ModelForm
from parkingspots.models import Book


class BookForm(ModelForm):

    class Meta:
        model = Book

        fields=['book_id','book_name','author_name','publisher_name']
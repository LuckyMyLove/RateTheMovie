from django import forms
from .models import Actors, Directors, Movies, Categories


class ActorsForm(forms.ModelForm):
    class Meta:
        model = Actors
        fields = "__all__"
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firstname', }),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname', }),
            'birthday': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD',
                                               'type': 'date'}),
            'photo': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Photo URL', 'type': 'url'}),
        }


class DirectorsForm(forms.ModelForm):
    class Meta:
        model = Directors
        fields = "__all__"
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firstname', }),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname', }),
            'birthday': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD',
                                               'type': 'date'}),
            'photo': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Photo URL', 'type': 'url'}),
        }


class MoviesForm(forms.ModelForm):
    actors = forms.ModelChoiceField(queryset=Actors.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Actors'}))
    directors = forms.ModelChoiceField(queryset=Directors.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Directors'}))

    class Meta:
        model = Movies
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', }),
            'premier_date': forms.DateInput(format=('%Y-%m-%d'),
                                            attrs={'class': 'form-control', 'placeholder': 'Premiere Date',
                                                   'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            # attrs={'class': 'form-control', 'placeholder': 'Category'}
            'picture': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Picture URL', 'type': 'url'}),
        }


class CategoryForm(forms.ModelForm):
    categories = forms.ModelChoiceField(queryset=Categories.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control',
                                                                   'placeholder': 'Category',
                                                                   'onchange': 'categoryForm.submit();'}))

    class Meta:
        model = Categories
        fields = "__all__"
        widgets = {
            'name': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'Category'})
        }

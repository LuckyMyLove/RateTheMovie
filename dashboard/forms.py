from django import forms
from django.template.defaultfilters import safe
from .models import Actors, Directors, Movies, Categories, ActorsRates, DirectorsRates, MoviesRates


class actorsForm(forms.ModelForm):
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


class directorsForm(forms.ModelForm):
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


class moviesForm(forms.ModelForm):
    actors = forms.ModelChoiceField(queryset=Actors.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Actors'}))
    directors = forms.ModelChoiceField(queryset=Directors.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Directors'}))

    # directors = forms.MultipleChoiceField(queryset=Directors.objects.all(),
    #                                           widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Directors'}))

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
            'picture': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Picture URL', 'type': 'url'}),
        }


class categoryForm(forms.ModelForm):
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


class RatingActorForm(forms.ModelForm):
    rate = forms.ChoiceField(choices=((1, safe("1 &#11088")),
                                      (2, safe("2 &#11088")),
                                      (3, safe("3 &#11088")),
                                      (4, safe("4 &#11088")),
                                      (5, safe("5 &#11088")),
                                      (6, safe("6 &#11088")),
                                      (7, safe("7 &#11088")),
                                      (8, safe("8 &#11088")),
                                      (9, safe("9 &#11088")),
                                      (10, safe("10 &#11088"))),
                             widget=forms.Select(attrs={'class': 'form-control'}),
                             label="Rating")

    class Meta:
        model = ActorsRates
        fields = "__all__"
        widgets = {
            'actors': forms.HiddenInput(attrs={'class': 'form-control', 'value': 1}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User', 'value': 1}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
            'rate': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
        }


class RatingDirectorForm(forms.ModelForm):
    rate = forms.ChoiceField(choices=((1, safe("1 &#11088")),
                                      (2, safe("2 &#11088")),
                                      (3, safe("3 &#11088")),
                                      (4, safe("4 &#11088")),
                                      (5, safe("5 &#11088")),
                                      (6, safe("6 &#11088")),
                                      (7, safe("7 &#11088")),
                                      (8, safe("8 &#11088")),
                                      (9, safe("9 &#11088")),
                                      (10, safe("10 &#11088"))),
                             widget=forms.Select(attrs={'class': 'form-control'}),
                             label="Rating")

    class Meta:
        model = DirectorsRates
        fields = "__all__"
        widgets = {
            'director': forms.HiddenInput(attrs={'class': 'form-control', 'value': 1}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User', 'value': 1}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
            'rate': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
        }


class RatingMovieForm(forms.ModelForm):
    rate = forms.ChoiceField(choices=((1, safe("1 &#11088")),
                                      (2, safe("2 &#11088")),
                                      (3, safe("3 &#11088")),
                                      (4, safe("4 &#11088")),
                                      (5, safe("5 &#11088")),
                                      (6, safe("6 &#11088")),
                                      (7, safe("7 &#11088")),
                                      (8, safe("8 &#11088")),
                                      (9, safe("9 &#11088")),
                                      (10, safe("10 &#11088"))),
                             widget=forms.Select(attrs={'class': 'form-control'}),
                             label="Rating")

    class Meta:
        model = MoviesRates
        fields = "__all__"
        widgets = {
            'movie': forms.HiddenInput(attrs={'class': 'form-control', 'value': 1}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'User', 'value': 1}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
            'rate': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
        }
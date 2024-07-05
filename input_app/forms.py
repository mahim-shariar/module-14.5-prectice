from django import forms
from django.forms.widgets import NumberInput
import datetime


# Create your forms here.

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class InputForm(forms.Form):
    name = forms.CharField(max_length=100)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(
        years=['1980', '1981', '1982', '2004', '2005', '2006', '2007', '2008', '2009', '2010']))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color1 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(
        choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES,)
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    password = forms.CharField(widget=forms.PasswordInput())
    duration = forms.DurationField( ) 
    file = forms.FileField()
    file_path= forms.FilePathField(path = "input_app/")
    image= forms.ImageField()
    ip = forms.GenericIPAddressField( )
    nullFIled = forms.NullBooleanField( ) 
    rgex = forms.RegexField(regex = "G.*s") 
    url= forms.URLField( ) 



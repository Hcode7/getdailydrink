from django import forms
from .models import UserWaterIntake


class WaterIntakeForm(forms.Form):
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')], 
        required=True
    )
    age = forms.IntegerField(min_value=1, max_value=120, required=True)
    weight = forms.IntegerField(min_value=1, max_value=300, required=True)
    activity_level = forms.ChoiceField(
        choices=[ 
            ('sedentary', 'Sedentary'),
            ('lightly-active', 'Lightly Active'),
            ('moderately-active', 'Moderately Active'),
            ('very-active', 'Very Active')
        ], 
        required=True
    )
    climate = forms.ChoiceField(
        choices=[('cold', 'Cold'), ('temperate', 'Temperate'), ('hot', 'Hot')], 
        required=True
    )
    health_conditions = forms.ChoiceField(
        choices=[ 
            ("pregnancy", "Pregnancy"),
            ("diabetes", "Diabetes"),
            ("kidney disease", "Kidney Disease"),
            ("heart disease", "Heart Disease"),
            ('none', 'None')
        ], 
        required=False
    )

    # Adding widgets for styling and visibility
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class': 'border border-gray-500 text-black '})
        self.fields['age'].widget.attrs.update({'class': 'border border-white text-black', 'min': '1'})
        self.fields['weight'].widget.attrs.update({'class': 'border border-white text-black', 'min': '1'})
        self.fields['activity_level'].widget.attrs.update({'class': 'border border-gray-500 text-black'})
        self.fields['climate'].widget.attrs.update({'class': 'border border-gray-500 text-black'})
        self.fields['health_conditions'].widget.attrs.update({'class': 'border border-gray-500 text-black'})

from django.shortcuts import render
from .forms import WaterIntakeForm
from .models import UserWaterIntake
from .utils import calculate_water_intake


def log_water(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST or None)
        if form.is_valid():

            # Extract necessary fields from the user's profile
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            climate = form.cleaned_data['climate']
            activity_level = form.cleaned_data['activity_level']
            weight = form.cleaned_data['weight']
            health_conditions = form.cleaned_data['health_conditions'] 

            total_water = calculate_water_intake(weight, gender, climate, activity_level, age, health_conditions)
            
            total_water = round(total_water, 2)

            if not request.session.session_key:
                request.session.create()

            if request.user.is_authenticated:
                UserWaterIntake.objects.create(
                    user=request.user,
                    water_amount=total_water,  
                )
            else:
                UserWaterIntake.objects.create(
                    session_key=request.session.session_key,
                    water_amount=total_water,  
                )

            return render(request, 'pages/log_water.html', {'total_water': total_water, 'form': form})

        else:
            # Handle form errors
            print(form.errors)
    else:
        form = WaterIntakeForm()

    return render(request, 'pages/log_water.html', {'form': form})

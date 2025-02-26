from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from .forms import WaterIntakeForm, GoalWaterForm
from .models import UserWaterIntake, SaveGoal, WaterTake
# from .utils import calculate_water_intake
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
import numpy as np
import joblib

model = joblib.load('./hydration_model.pkl')

@login_required
def challenge(request):
    dailygoal = UserWaterIntake.objects.filter(user=request.user).last()
    if not dailygoal:
        return JsonResponse({'message': "Please set a daily water goal first!"})

    water_intake = WaterTake.objects.filter(user=request.user, created_at__date=now().date())
    total_intake = sum(entry.amount_liters for entry in water_intake)

    if request.method == 'POST':
        form = GoalWaterForm(request.POST)
        if form.is_valid():
            cup = form.cleaned_data['cup']

            # Convert cup size to liters
            cup_sizes = {
                "250ml": 0.25,
                "500ml": 0.5,
                "1L": 1.0,
            }
            amount_liters = cup_sizes.get(cup, 0)

            if amount_liters == 0:
                return JsonResponse({"message": "Invalid cup size."})

            # Create water intake entry
            waterintake = WaterTake.objects.create(user=request.user, cup=cup, amount_liters=amount_liters)

            # 🔹 Fetch or create the user's SaveGoal (ONE PER USER)
            savegoal, _ = SaveGoal.objects.get_or_create(
                user=request.user,
                defaults={"water_intake": dailygoal}
            )

            # Update total intake
            total_intake += amount_liters
            # Check if the goal is complete
            if total_intake >= dailygoal.water_amount:
                savegoal.complete = True
                savegoal.points += 5
                savegoal.water_intake = dailygoal  # Update the goal
                savegoal.save()

                # Clear water intake records for the user
                WaterTake.objects.filter(user=request.user).delete()

                return JsonResponse({"message": "Your Goal of this day is complete! 🎉", "points": savegoal.points})

            return JsonResponse({"message": f"Keep going! {dailygoal.water_amount - total_intake:.2f}L left."})

    form = GoalWaterForm()
    return render(request, 'pages/challenge_form.html', {'form': form})


@login_required
def rewards(request):
    watertake = WaterTake.objects.filter(user=request.user)
    total_intake = sum(entry.amount_liters for entry in watertake)
    dailygoal = UserWaterIntake.objects.filter(user=request.user).last()
    water = round(dailygoal.water_amount - total_intake, 2)
    rewards = SaveGoal.objects.all().order_by('-points')
    return render(request, 'pages/reward.html', {'rewards': rewards, "take" : water})

def home(request):
    if not request.session.session_key:
        request.session.create()
    if request.user.is_authenticated:
        water = UserWaterIntake.objects.filter(user=request.user).last()
    else:
        water = UserWaterIntake.objects.filter(session_key=request.session.session_key).last()
    context = {
        'water' : water,

    }
    return render(request, 'pages/home.html', context)

def log_water(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            gender = 0 if form.cleaned_data['gender'] == 'male' else 1
            climate = {'cold': 0, 'temperate': 1, 'hot': 2}[form.cleaned_data['climate']]
            activity_level = {'sedentary': 0, 'lightly-active': 1, 'moderately-active': 2, 'very-active': 3}[form.cleaned_data['activity_level']]
            age = form.cleaned_data['age']
            health_conditions = {'none': 0, 'diabetes': 1, 'kidney disease': 2, 'heart disease': 3, 'pregnancy': 4}[form.cleaned_data['health_conditions']]
            input_data = np.array([[weight, gender, climate, activity_level, age, health_conditions]])
            predicted_water = model.predict(input_data)[0]
            
            email_frequency = form.cleaned_data['email_frequency']

            if request.user.is_authenticated:
                UserWaterIntake.objects.create(user=request.user, water_amount=predicted_water, email_frequency=email_frequency)
            return redirect('home')
    else:
        form = WaterIntakeForm()

    return render(request, 'pages/log_water.html', {'form': form})
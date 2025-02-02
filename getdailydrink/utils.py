# You would need a function to calculate the total water intake
def calculate_water_intake(weight, gender, climate, activity_level, age, health_conditions=[]):
    """Calculate recommended daily water intake in liters based on various factors."""

    # Base calculation: 33 ml per kg of body weight
    base_water = weight * 0.033  

    # Gender adjustment
    if gender == 'male':
        base_water *= 1.2  # Males generally need more water

    # Activity level adjustment
    activity_factor = {
        'sedentary': 1.0,
        'lightly-active': 1.1,
        'moderately-active': 1.2,
        'very-active': 1.3,
    }
    base_water *= activity_factor.get(activity_level, 1.0)

    # Climate adjustment
    climate_factor = {
        'cold': 1.0,
        'temperate': 1.05,
        'hot': 1.1, 
    }
    base_water *= climate_factor.get(climate, 1.0)

    if age > 60:
        base_water *= 0.9  

    health_condition_factor = {
        'pregnancy': 1.2,    
        'diabetes': 1.3,   
        'kidney disease': 0.8,
        'heart disease': 0.9, 
        'none' : 1.0,
    }

    if isinstance(health_conditions, str):
        health_conditions = [hc.strip().lower() for hc in health_conditions.split(",")]

    elif not isinstance(health_conditions, list):
        health_conditions = []

    for condition in health_conditions:
        base_water *= health_condition_factor.get(condition, 1.0)

    return round(base_water, 2) 

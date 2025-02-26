import pandas as pd

# إنشاء بيانات أولية
data = {
    "weight": [60, 70, 80, 90, 100],
    "gender": ["male", "female", "male", "female", "male"],
    "climate": ["hot", "cold", "temperate", "hot", "cold"],
    "activity_level": ["moderately-active", "sedentary", "very-active", "lightly-active", "moderately-active"],
    "age": [25, 30, 45, 50, 60],
    "health_conditions": ["none", "diabetes", "none", "heart disease", "kidney disease"]
}

# تحويلها إلى DataFrame
df = pd.DataFrame(data)

# حساب كمية الماء الأساسية
df["base_water"] = df["weight"] * 0.033  # 33ml لكل 1kg (كمثال)

# حفظ البيانات في CSV
df.to_csv("hydration_data.csv", index=False)

print("✅ تم إنشاء الملف hydration_data.csv بنجاح!")

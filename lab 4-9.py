def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi
weight_kg = 60
height_m = 10

bmi = calculate_bmi(weight_kg, height_m)
print ("BMI ของคุณคือ %.2F" % bmi)

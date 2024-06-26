def calculate_bmi(weight, height):
    """
    คำนวณดัชนีมวลกาย (BMI)
    :param weight: น้ำหนัก (กิโลกรัม)
    :param height: ส่วนสูง (เมตร)
    :return: ค่า BMI
    """
    bmi = weight / (height ** 2)
    return bmi
def calculate_circle_area(radius):
    """
    คำนวณพื้นที่วงกลม
    :param radius: รัศมีของวงกลม
    :return: พื้นที่ของวงกลม
    """
    pi = 22 / 7
    area = pi * (radius ** 2)
    return area
radius = 5
area = calculate_circle_area(radius)
print(f"พื้นที่วงกลมที่มีรัศมี {radius} คือ {area}")
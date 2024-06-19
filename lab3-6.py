num_students = 10
for i in range(num_students):
    score = int(input(f"กรุณาป้อนคะแนนของนักศึกษาคนที่ {i+1}: "))
    print(f"คะแนนของนักศึกษาคนที่ {i+1} คือ {score}")
n = 5
total_sum = 0
for i in range(n):
    number = int(input(f"กรุณาป้อนจำนวนเต็มที่ {i+1}: "))
    total_sum += number
print(f"ผลลัพธ์ของการบวกจำนวนเต็ม {n} จำนวน คือ {total_sum}")
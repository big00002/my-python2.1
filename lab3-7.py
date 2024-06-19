total_sum = 0
n = int(input("จำนวนของจำนวนเต็ม: "))
for i in range(n):
    number = int(input(f"จำนวนเต็มที่ {i+1}: "))
    total_sum += number
print(f"ผลลัพ {n} จำนวน คือ {total_sum}")
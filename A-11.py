print("身長と体重を入力してください。BMIを計算します")

height = float(input("身長を入力してください（cm）："))
weight = float(input("体重を入力してください（kg）："))

height = round(height, 2)
weight = round(weight, 2)

bmi = round(weight / (height * height), 2)

print(f"BMIは{bmi}です")

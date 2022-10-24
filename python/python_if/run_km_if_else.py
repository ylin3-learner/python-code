# coding: utf-8
run_km = float(input('請輸入公里數: '))
money = 1
if run_km <= 13:
	money += 13
elif 3 <= run_km < 10:
	money += ( 13 + (run_km - 3) * 2.3)
else:
	money += ( 13 + 7*2.3 + (run_km - 10) * 2.76)
print(f'這次的出租車費用是: {money:.2f}')
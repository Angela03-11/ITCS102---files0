temp = eval(input("Enter Temperature ---> "))

if temp <= 0:
		print("BELOW FREEZING")
elif temp >= 1 and temp <= 15:
		print("EXTREME COLD TEMPERATURE")
elif temp >= 16 and temp <= 30:
		print("COLD TEMPERATURE")
elif temp >= 31 and temp <= 38:
		print("LUKE WARM TEMPERATURE")
elif temp >= 39 and temp <= 42:
		print("WARM TEMPERATURE")
elif temp >= 43 and temp <= 50:
		print("HOT TEMPERATURE")
elif temp >= 51 and temp <= 60:
		print("EXTREMELY HOT TEMPERATURE")
elif temp >= 61:
		print("BURNING TEMPERATURE")
else:
	print("Invalid Temperature!")
	









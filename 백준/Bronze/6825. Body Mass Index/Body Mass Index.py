w,h=map(float,open(0))
b=w/(h*h)
if b>=25:print("Overweight")
elif b>=18.5:print("Normal weight")
else:print("Underweight")
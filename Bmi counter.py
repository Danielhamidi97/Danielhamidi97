h =int (input("enter your height"))
w =int (input("enter your weight"))
BMI = w / (h * h)* 10000
if BMI >= 40:
    print('You are in obesity class III')
elif 35.0 <= BMI <= 39.9:
    print('You are in obesity class II')
elif 30.0 <= BMI <= 34.9:
    print('You are in obesity class I')
elif 25.0 <= BMI <= 29.9:
    print('You are overweight')
elif 18.5 <= BMI <= 24.9:
    print('You are normal weight')
elif BMI <= 18.5:
    print('You are under weight')
elif BMI <= 16.5:
    print('severe underweight')

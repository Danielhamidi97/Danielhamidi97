maximum = 0
minimum = 10000
tow = 0
for i in range (3):
    index = int(input('enter your number'))
    if index > maximum :
        maximum = index 
        if index < minimum :
            minimum = index 
        tow = tow + index 
average = tow / 10
print ('maximum number is '+str(maximum))
print ('maximum number is '+ str(minimum))
print ('average number is '+ str(average))
       




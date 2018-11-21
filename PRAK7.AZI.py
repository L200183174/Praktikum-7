#Activity 1
d = {'Triangle' : 'L = 0.5 * a *t',
     'Square' : 'L = s ** 2',
     'Rectangle' : 'L = p * l',
     'Circle' : 'L = pi * r ** 2',
     'Parallelogram' : 'L = a * t'}

print '''


|No|Nama Bangun       |Rumus Luas       |
|--|------------------|-----------------|
|1 |Triangle          |%s
|2 |Square            |%s
|3 |Rectangle         |%s
|4 |Circle            |%s
|5 |Parallelogram     |%s

'''%(d['Triangle'],
     d['Square'],
     d['Rectangle'],
     d['Circle'],
     d['Parallelogram'])


#Activity 2
a = 2
c = True
while c:
    b=raw_input('Please, Input Your Password: ')
    if b == 'azicans':
        print'Login Successful'
        c = False
    elif b!= 'azicans':
        if a!= 0:
            print'Sorry, you entered the wrong password'
            a=a-1
        else :
            print'You have tried 3 times. Your access is rejected '
            break

##ACTIVITY 3
f = ('morning', 'noon', 'afternoon', 'evening', 'night')
g = input ('Enter your name: ')
h = float(input ('What time is it? (format 24 jam):'))
if h>=1.00 and h<=10.59 :
   h=f[0] 
elif h>=11.00 and h<=14.59 :
   h=f[1]
elif h>=15.00 and h<=16.30 :
   h=f[2]
elif h>=16.31 and h<=18.59 :
   h=f[3]
elif h>=19.00 and h<=24.59 :
   h=f[4]
print('''Good%s%s.'''%(h,g))
    
















    
    

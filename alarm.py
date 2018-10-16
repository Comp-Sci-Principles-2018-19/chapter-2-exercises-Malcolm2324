time=int(input('what time is it'))
long=int(input('how long do you want your alarm to be for?'))
longmodulo=long%24
alarmt=time+longmodulo
alarmt=alarmt%24
print('I will set off at',alarmt)

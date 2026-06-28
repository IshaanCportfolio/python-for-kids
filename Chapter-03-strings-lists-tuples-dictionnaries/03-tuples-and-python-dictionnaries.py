fibs=(0,1,1,2,3,)
print(fibs[3])
favourite_sports=['Lionel Messi, Soccer',
                  'Michael Jordan, Basketball',
                  'Serena Williams, Tennis',
                  'Tiger Woods, Golf',
                  'Wayne Gretzky, Hockey',
                  'Kapil Dev, Cricket']
favourite_sports={'Lionel Messi' : 'Soccer',
                  'Michael Jordan' : 'Basketball',
                  'Serena Williams' : 'Tennis',
                  'Tiger Woods' : 'Golf',
                  'Wayne Gretzky' : 'Hockey',
                  'Kapil Dev' : 'Cricket'}
print(favourite_sports['Lionel Messi'])
del favourite_sports['Tiger Woods']
print(favourite_sports)
favourite_sports['Kapil Dev']='Field Hockey'
print(favourite_sports)
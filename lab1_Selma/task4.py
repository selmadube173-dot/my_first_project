def get_fine(limit,speed):
    if speed<= limit:
        return 0
    fine=80 + (speed-limit) * 10
    if speed>140:
        fine= fine +220
    return fine
limit=float (input('Enter speed limit:'))
speed= float (input('Enter clocked speed:'))

fine= get_fine(limit,speed)

if fine == 0:
        print('Legal speed')
   
else:
        print (f' Your speed is illegal, fine is ${fine} ')
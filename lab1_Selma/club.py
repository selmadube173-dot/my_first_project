#print a greeting message for the program
print('WELCOME! tO Football Club Generator')

#ask the user for city they grew up in
#\n makes the cursor show on the new line
city= input('City you grew up in?\n')

# ask the user for the name of the animal
#\n makes the cursor show on the new line
animal=input('What is your favourite animal name?\n')

#combine the city and animal to  generate the club name
club_name= city + "" + animal 

#show the final club name to the user
print('Your football club  name is :' + club_name)
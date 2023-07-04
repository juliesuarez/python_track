
'''
The function tests tells us to input the parameters of test1 and test2
Later we compare the values of test1 and test2
Incase the values are equal we return the value of test1
Otherwise not equal we return the value of test2 
The input function instructs to put values of test 1 and test2 then converted to integers by function int.
'''


def tests(test1, test2):
	#tests is a defined function and test1 and test2 are parameters.
	if test1 == test2:
		#if the two values in test1 and test2 are equal return test1
		return test1
	else:
		# incase the values are not equal return test2
		return test2
#the statements below instruct the user enter for test1 and test2
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
The function courseWrk has a parameter cswork
the function tests is called with its parameters and assigned to the variable testsMark.
the value in the variable testsMark is added to cswork to get the average and the value is stored in the
variable avgtestsCswork.
the value stored in the variable avgtestsCswork is multiplied with (40/100) and then assigned to the 
variable fnltestsCswork.
then the final results are displayed by function print.
at the end we assign an arguement by function input which is an integer
Then the function is called.

'''
def courseWrk(cswork):
	#cswork is parameter of a defined function courseWrk.
	testsMark = tests(test1,test2)
	#tests function is called inside the fuction courseWrk.
	avgtestsCswork = (cswork + testsMark)/2
	#here we are getting the average mark for cswork
	fnltestsCswork = avgtestsCswork * (40/100)
	#we are getting the value stored in avgtestsCswork and multiplying it with (40/100) to get final cswork mark.
	print('..............................')
	#the results for the final cswork will be printed.
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
    #here we are instructed to write the course work mark.
cswork = int(input('Please enter your course work Marks: '))
#we are evoking a function courseWrk.
courseWrk(cswork)

'''
Basically,the code is calculating the final course mark basing on the values input of tests and course work.
The defined function of tests has two parameters of test1 and test2
The code then checks if the valaues of test1 and test2 are equal
And if these values are equal it returns test1
And if these values are not equal,it returns test2
The code then prompts the user to input the marks of test1 and test by the input function which holds the 
values as strings, the int function converts these values to integers
Another function called course work is defined which has one parameter of cswork.
Inside the function coursework,the function tests is called assigned to a variable testsMark
The average mark is then calculated 
'''





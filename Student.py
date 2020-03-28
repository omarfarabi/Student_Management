import os
import platform

global liststudent #Making ListStd As Super Global Variable
liststudent = ["Mohammad", "Omar", "Farabi", "Nancy", "Kabir", "John"] #List Of Students

def StudentManagement(): #Function For The Student Management System

	
	#Welcome message and options for this system
	print(""" 

 
 ********************************************************

     WELCOME TO STUDENT INFORMATION MANAGEMENT SYSTEM

 ********************************************************
  

Enter 1 : View All Student's List 
Enter 2 : Add New Student 
Enter 3 : Search Student 
Enter 4 : Remove Student 
		
		""")

	try: #Using Exceptions For Validation
		userInput = int(input("Please select any option: ")) #Will Take Input From User
	except ValueError:
		exit("\nHy! That's Not A Number") #Error Message
	else:
		print("\n") #Print New Line

	#Checking Using Option	
	if(userInput == 1): #This Option Will Print List Of Students
		print("List Students\n")  
		for students in liststudent:
			print("=> {}".format(students))

	elif(userInput == 2): #This Option Will Add New Student In The List
		newStd = input("Enter New Student: ")
		if(newStd in liststudent): #This Condition Checking The New Student Is Already In List Ur Not
			print("\nThis Student {} Already In The Database".format(newStd))  #Error Message
		else:	
			liststudent.append(newStd)
			print("\n=> New Student {} Successfully Add \n".format(newStd))
			for students in liststudent:
				print("=> {}".format(students))	

	elif(userInput == 3): #This Option Will Search Student From The List
		searchStd = input("Enter Student Name To Search: ")
		if(searchStd in liststudent): #This Condition Searching The Student
			print("\n=> Record Found Of Student {}".format(searchStd))
		else:
			print("\n=> No Record Found Of Student {}".format(searchStd)) #Error Message

	elif(userInput == 4): #This Option Will Remove Student From The List
		rmvStd = input("Enter Student Name To Remove: ")
		if(rmvStd in liststudent): #This Condition Removing The Student From The List 
			liststudent.remove(rmvStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmvStd))
			for students in liststudent:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(rmvStd)) #Error Message
	 
	elif(userInput < 1 or userInput > 4): #Validating User Option
		print("Please Enter Valid Option")	#Error Message	
						
#brought to you by code-projects.org
StudentManagement()

def runagain(): #Making Runable Problem1353
	runAgn = input("\nwant To Run Again yes/no: ")
	if(runAgn.lower() == 'yes'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		StudentManagement()
		runagain()
	else:
		quit(bye) #Print GoodBye Message And Exit The Program

runagain()		

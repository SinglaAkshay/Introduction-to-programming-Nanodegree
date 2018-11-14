# -*- coding: utf-8 -*-
game_levels=['easy','medium','hard']
No_of_question=[5,7,10]
#Easy Level Question is Based on Operating System Concepts
easy_level_question='''___1___ is a program in execution. It is the unit of work in most system.The ___2___ is the module that 
gives control of the CPU to the process selected by the short-term scheduler.A set of processes is in a ___3___ state 
when every process in the set is waiting for an event that can be caused only by another process in the set.
Aging is a technique to solve the ___4___ problem, it ___5___ the priority of processes that wait in the
system for a long time.'''
#Medium Level Question is Based on C++ Concepts
medium_level_question='''The ___1___ functions are faster in execution when compared to normal functions as the compiler 
treats them as ___2___.A virtual function with no function body and assigned with a value ___3___ is called as pure 
virtual function.We cannot instantiate an ___4___ class.___5___ cannot be overloaded and the only form is without the parameters.
___6___is the pointer variable of the compiler which always holds the current active object’s address.
The default value of ___7___ variable is 0.'''
#Hard Level Question is Based on Computer Network Concepts
hard_level_question='''There are ___1___ OSI layers.The ___2___ layer is responsible for data routing, packet switching 
and control of network congestion.Every NIC has its own ___3___ address that identifies the PC on the network.The main 
task of ___4___is to map a known  IP address to a MAC layer address.___5___ is a utility 
program that allows you to check connectivity between network devices on the network.A straight-through cable is 
used to connect ___6___ devices together.A crossover cable is used to connect two ___7___ devices together.
___8___ topology consists of a central hub that connects to nodes.Private IP addresses are assigned for use on ___9___.
SMTP is short for ___10___.'''
#List of Questions
Question_list=[easy_level_question,medium_level_question,hard_level_question]
#Answers of Fill in the Blanks Question
easy_level_answers=['process','dispatcher','deadlock','starvation','increases']

medium_level_answers=['inline','macros','zero','abstract','destructor','this','static']

hard_level_answers=['seven','network','MAC','Address Resolution Protocol','ping','different','similar','star','intranet',
				'Simple Mail Transfer Protocol']
#List of Answers
Answers_List=[easy_level_answers,medium_level_answers,hard_level_answers]
Welcome_message="""Welcome to the Fill in the Blanks Quiz game.\nSelect level of game you want to play.\nPress 1 for easy level.\nPress 2 for medium level.
Press 3 for hard level."""
def fill_correct_answer(Question_no,level,answer_given):
	'''
	This function is used to fill the blanks with correct answer if user gave correct answer then next question is displayed
	with previous answer filled in place of blanks
	'''
	global Question_list
	fill_blanks="___"+str(Question_no-1)+"___"
	Question_list[level-1]=Question_list[level-1].replace(fill_blanks,answer_given)
	print Question_list[level-1]

def validate_answer(Question_no,level,answer_given):
	'''validate_answer() function is used to check whether answer given by user is correct or not it returns 
      true if answer is correct else false'''
	global Answers_List
	if answer_given==Answers_List[level-1][Question_no-1]:
		return True
	else:
		return False

def play_game(level):
	'''play_game() function is used to keep track of number of correct answers given by user,number of chances remaining
      ,current question to be answered and calling to validate_answer() function '''
	No_of_Correct_Answers=0
	No_of_chances=5
	while No_of_Correct_Answers!=No_of_question[level-1] and No_of_chances!=0:
		answer=raw_input("\nWhat should be substituted in for ___"+str(No_of_Correct_Answers+1)+'___?')
		if validate_answer(No_of_Correct_Answers+1,level,answer)==True:
			No_of_Correct_Answers+=1
			print 'That is the CORRECT answer!! You have '+str(No_of_chances)+' chances remaining\nNow Answer Next Question\n'
			fill_correct_answer(No_of_Correct_Answers+1,level,answer)
		else:
			No_of_chances-=1
			print 'That is the WRONG answer!! You have '+str(No_of_chances)+' chances remaining\n Try Again'
	if No_of_Correct_Answers==No_of_question[level-1]:
		print "\n\nYou gave Correct Answers of all Questions\nBINGO ******  YOU WON THE GAME CONGRATULATIONS!!  ******"
	elif No_of_chances==0:
		print "\n\nYou are left with no chance\nSO SAD ******  YOU LOST THE GAME HARD LUCK!!  ******"
def start_game():
	'''start_game() is the main function which takes input of level which user wants to play and display the required
       question followed by call to play_game() module'''
	print  Welcome_message
	choice =int(raw_input("\nEnter your choice?"))
	print '\nYou have choosen '+game_levels[choice-1]+' level'
	print '\nYou will get total 5 guesses per problem.\n'
	print '\n Here is your Question.\n\n'+Question_list[choice-1]+'\n\n'
	play_game(choice)
start_game()
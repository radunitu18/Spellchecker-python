import sys
import os
from difflib import SequenceMatcher
import time
while True:
	print("Hello user, what would you like to do?\n 1. Spell check a sentence.\n 2. Spell check a file.\n 0. Exit.\n ")
	choice = input("Input the number of the action. ")
	ok = 0
#The "ok" variable is used to determine when to exit the while loop
#and to make sure the user can get back to option 1 and 2 when entering a wrong number.
	while ok == 0:
	#This if breaks the sentence into words, making the characters lowercase where it needs to and puts the words into a list
		if choice == "1":
			print("\nYou chose to spell check a sentence!\n")
			sentence = input("Now please input the sentence :")
			for i in "01234567890`¬!$£%^&*()_+-=[}{]#~;':@,./<>?":
				sentence = sentence.replace(i,"")
			word_list = sentence.lower().split(" ")
			ok = 1
		elif choice == "2":
	#This if checks if the file exists and then puts the words into a list
			print("\nYou chose to spell check a file!\n")
			file_name = input("Now please input the name of the file :")
			if os.path.exists(file_name) == False:
				file_name = input("This file does not exist. Please input a file that exists:")
				if os.path.exists(file_name) == False:
					sys.exit()
			else: 
				print("The file exists!")
			file = open(file_name,"r")
			sentence = file.read()
			sentence = sentence.replace("\n"," ").lower()
			for i in "01234567890`¬!$£%^&*()_+-=[}{]#~;':@,./<>?":
				sentence = sentence.replace(i,"")
			word_list = sentence.split(" ")
			ok = 1;
		elif choice == "0":
	#This if exits the program
			print("\nYou chose to exit!\nGoodbye")
			sys.exit()
		else:
	#This if makes it possible for the user to input a correct number if he/she made a mistake, or exit the program.
			print("You chose none of the options above! Do you want to select something else?\n")
			choice = input("\nInput 0 if you want to exit, 1 if you want to spell check a sentence and 2 if you want to spell check a file.\n")
			if(choice !="1" and choice !="2" ):
				print("Goodbye!")
				sys.exit()

	#The next set of instructions verify which words are correct and which are not, in a memory efficient way
	words_added_dictionary = 0
	words_changed = 0
	corrected_sentence = ""
	correct_word_count = 0
	incorrect_word_count = 0;
	with open("EnglishWords.txt","r+") as f1:
			for x in word_list:
				ok=0;
				for element in f1:
					element = element.strip()
					if x == element and ok == 0:
						ok = 1
				if ok == 1:
					corrected_sentence = corrected_sentence+ x + " "
					correct_word_count += 1
				else:
					print("\n This word (" + x +") is incorrect.\n What would you like to do?\n 1. Ignore it.\n 2. Mark it as incorrect.\n 3. Add it to the dictionary.\n 4. Get a suggestion.\n\n")
					choice = int(input("Type in the number of the action.\n"))

					if choice == 1:
						incorrect_word_count += 1
						corrected_sentence = corrected_sentence + x + " "
					elif choice == 2:
						incorrect_word_count += 1
						corrected_sentence = corrected_sentence + "?" + x + "? "
					elif choice == 3:
						correct_word_count += 1
						words_added_dictionary += 1
						f1.write("")
						f1.write(x)
						corrected_sentence = corrected_sentence + x + " "
					elif choice == 4:
						current_score = 0
						highest_score = 0
						best_word = ""
						f1.seek(0)
					#Get the word suggestion based on the highest score 
						for element1 in f1:
							current_score = SequenceMatcher(None, element1, x).ratio()
							if current_score > highest_score:
								highest_score = current_score
								best_word = element1
						print("The suggested word is " + best_word + " Do you want to use it? (type 1 if you do, 0 if you don't).")
						word_choice = int(input())
						if word_choice == 1:
							correct_word_count +=1;
							corrected_sentence = corrected_sentence + best_word + " "
							words_changed += 1
						else:
							incorrect_word_count +=1
							corrected_sentence = corrected_sentence + x + " "

				f1.seek(0)
	print("\nWhat is the name of the file you want to create? (do not add the .txt extension) ")
	file_created = input()
	file_created = file_created + ".txt"
	current_time = time.asctime()
	corrected_sentence = corrected_sentence.replace("\n", "")
	#this is for creating and writing in the file
	with open(file_created, "a") as output_file:
		output_file.write("Total number of words = " + str(correct_word_count+incorrect_word_count))
		output_file.write("\nTotal number of correct words = " + str(correct_word_count))
		output_file.write("\nTotal number of incorrect words = " + str(incorrect_word_count))
		output_file.write("\nTotal number of words added to the dictionary = " + str(words_added_dictionary))
		output_file.write("\nTotal number of words changed = " + str(words_changed) )
		output_file.write("\n" + current_time)
		output_file.write("\n It took " + str(time.process_time()) + " seconds for the program to spell check everything!\n")
		output_file.write(corrected_sentence)

	#Now im asking the user if he wants to spell check another file or to exit the program
	choice = input("If you want to spell check another sentence or file please press 1, otherwise, press anything else. ")
	if choice == "1":
		continue
	else:
		sys.exit()

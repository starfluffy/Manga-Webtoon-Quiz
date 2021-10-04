# Imports
import random
import tkinter as tk
from tkinter import *
from functools import partial
from tkinter import messagebox
import string
MAX_NAME_LENGTH = 15
MIN_SCORE = 0
LOW_SCORE = 2
MID_SOCRE = 6
MAX_SCORE = 10
FONT = 10
PADDING = 10
Q_HEIGHT = 5
Q_WIDTH = 30
Q_PADDING = 4
BUTTON_PADDING = 2

class Questions():
  def __init__(self):
    pass # passing self through itself

  # This is a list of the questions. Each element (question) contains 3 elements. The first is the question text, the second is another list whos elements are the answers that can be selected, and the third is the correct answer. All of the elements are strings
  question_list = [
    ["In the series 'Fullmetal Alchemist', Edward Elric is the youngest person in history to become a what?", ["Colonel", "State Alchemist", "Fullmetal Alchemist", "Homunculis"], "B"],
    ["The name 'Koro-sensei' comese from what Japanese phrase?", ["'Cannot be killed'", "'Mach speed'", "'Extremely fast moving'", "'Loves eating sweet things'"], "A"],
    ["In the webtoon 'Girls of the Wild', how did the character Ingui get her nickname 'Queen'?", ["She has royal blood", "She is extremely arrogant", "Her name means queen in Korean", "She is undefeatable when fighting in the ring"], "D"],
    ["In the webtoon 'I Want to be You, Just for a Day', what does Perion lose after losing a sword fight with Medea?", ["One of his arms", "All of his money", "One of the eyes", "His ability to talk"], "C"],
    ["In 'Bakuman', Moritaka Mashiro and Miho Azuki promise that when they both achieve their dreams, they will..?", ["Get married", "Be able to date", "Run away together", "Start a company together"], "A"],
    ["In 'The Remarried Empress', Prince Heinrey and his subodinates have the ability to turn into what?", ["Inanimate objects", "Birds", "Horses", "Other human forms"], "B"],
    ["In 'Cardcaptor Sakura', what is Yukito's true indentity?", ["The guardian Cereberus", "The magician Clow Reed", "Sakura's older brother", "The guardian Yue"], "D"],
    ["In the manga series 'Last Game', what is Yanagi's goal?", ["Become a doctor", "Take over his father's company", "Defeat Kujou", "Marry Hanazawa Kana"], "C"],
    ["In 'Detective Conan', what was the name of the Apotoxin that shrank Shinichi?", ["APTX 4869", "APTX 4968", "APTX 4698" , "APOTX 4869"], "A"],
    ["In 'The Disatrous Life of Saiki K.', what is the main characters main quote?", ["'Leave it to me!!'", "'Good grief'", "'You can do it if you believe'", "'I want to go home'"], "B"]
    ]

  # This is a function that returns the number of elements in question_list. ie the number of questions
  def number_of_questions(self):
    return len(self.question_list)

  # This is a function that shuffles the question_list
  def questions_shuffle(self):
    random.shuffle(self.question_list)

  # This is a function that returns the 'question text'. the current question number that the user is on in inputted
  def question_words(self, q):
    return self.question_list[q][0] # the 'question text' is the first element of the 'qth' element (the question that the user is currently on)

  #This is a functin that returns the answers that can be selected for the question. the current question number that the user is on in inputted
  def answer_list(self, q):
    return self.question_list[q][1] # the answers that can be selected in the second element of the 'qth' element (the question that the user is currently on)

  # This is a function that returns a list of the correct answers
  def correct_answer(self): 
    self.correct_answers = [] #sets up the array as empty to start
    for i in range(len(self.question_list)): #uses a for loop to go from 0 to the number of questions in the array question_list
      self.correct_answers.append(self.question_list[i][2]) #each iteration, the correct answer is added to the array
    return self.correct_answers # returns the list at the end

  # This is a function that returns what question number the user is one according the input of buttons that are clicked (or not clicked). the current question number that the user is on in inputted. the result of the button click for the next and back question buttons if inputted
  def question_number(self, q, next_back):
    # next_back is a variable that holds the input of buttons that change the question number that the user is on
    if next_back == "back": # if the button input is back,
      q -= 1 # the current question number that the user is on will go back one (minus 1)
    elif next_back == "next":
      q += 1 # the current question number that the user is on will go forward one (plus 1)
    else:
      q = q
    return q

  # This is a function that sets up an empty array for the users answers to go into. Zeroes will be used as place holders for questions that aren't answered yet
  def user_answer_setup(self):
    self.user_answers = [] #creates an empty array to start with
    for i in range(len(self.question_list)): #goes from 0 to the number of the questions in the list question_list
      self.user_answers.append(0) #sets up an array of zeroes with a for loop that will be. the zeros are place holders

  # This is a function that changes the list that holds the users answers that were entered
  def user_answer(self, q, answer):
    self.user_answers[q] = answer #the answer that is sent from the controller class gets stored in the list according the the question that was answered
    return self.user_answers

  # This is a function that returns a list that holds the users answers that were entered
  def final_user_answers(self):
    return self.user_answers

  # This is a function that checks the list with user answers against a list of zeroes to check if there are any unanswered questions. Unanswered questions in the user answer list are zeroes (the intial list used zeroes as place holders). The list of the user answers is inputted
  def all_answered_check(self, a):
    b = [] # using a and b just for convinience. they aren't used anywhere else in the code so it won't be confusing
    for i in range(len(self.question_list)):
      b.append(0)
    a_set = set(a) # sets the
    b_set = set(b) # lists
    if (a_set & b_set): #if the list of user answers has any zeroes in it (which are unanswered questions) it will return false
        return False
    else:
        return True #if the list of users doesn't have any zeros (unanswered questions), it will return True

  # This is a function that takes the button click result of the (reset quiz yes and no buttons). The result of the button click for resetting the quiz is inputted
  def reset_quiz(self, yes):
    return yes == "yes"
    if yes == "yes": # if the result of the button click is yes, it returns true
      return True
    else:
      return False

  # This is a function that returns a list containing the year levels that will be used to create a dropdown
  def year_level_select(self):
    self.year_levels = [9, 10, 11, 12, 13]
    return self.year_levels

class Score():
  def __init__(self):
    pass

  # Setting the initial score as 0
  score = 0

  # This is a function that compares the list of user answers to the list of the correct answers. It uses a for loop and if statement. the number of questions, a list containing the users answer, and a list containing the correct answers is inputted
  def scoring(self, questions, player_answers, correct_a):
    for i in range(questions): #number of questions is equal to the number of elements in the array question_list
      if player_answers[i] == correct_a[i]: #player answers is the array self.user_answers. correct_a is the array self.correct_answers
      #if the users answers matches up with the correct answer,
        self.score += 1 #the score will add 1
      else:
        self.score = self.score #otherwise, it will stay the same

  # This is a function that returns what the final score is
  def final_score(self):
    return self.score

  # This is a function that resets the score to 0 when the quiz is reset
  def reset_score(self, reset):
    if reset:
      self.score = 0

  # This is a function that determines and returns a message to say to the user according to what score they got. It uses if statements
  def final_message(self, score):
    if MIN_SCORE <= score <= LOW_SCORE:
      self.end_message = "Try reading more manga and webtoons"
    elif LOW_SCORE < score <= MID_SCORE:
      self.end_message = "Keep trying"
    elif MID_SCORE < score <= MAX_SCORE:
      self.end_message = "You are a genius"
    return self.end_message

class GraphicalUserInterface():
  
  # Sets the controller
  def __init__(self, controller_class):
    self.set_controller(controller_class)
    pass

  def set_controller(self, controller_class):
    self.controller = controller_class

  # This is a function that creates a window that is 400x250 and title QUIZ
  def create_window(self):
    self.window = tk.Tk()   
    self.window.geometry("400x250")
    self.window.title("QUIZ") 

  # This is a function that creates the name entry page. It has a label telling the user to enter a name, an entry box for the name and a continue button after the name is entered
  def ask_name(self):
    self.name_label = tk.Label(self.window, text = "Enter your name to continue", font = FONT, pady = PADDING)
    self.name_label.pack()
    self.name_entered = tk.Entry(self.window)
    self.name_entered.pack()
    self.name_button = tk.Button(self.window, text='CONTINUE', command = self.name_button_input)
    self.name_button.pack()
    self.name_button.mainloop()

  # This is a function that creates the select year level page. It has a label telling the user to select their year level, a dropdown menu that they can click on and then select the year level, and a start button after the year level is selected. A list of the year levels is inputted
  def select_year_level(self, year_level):
    self.year_label = tk.Label(self.window, text = "Select your year level to start", font = FONT, pady = PADDING)
    self.year_label.pack()
    self.clicked = StringVar()
    self.clicked.set("Select")
    self.dropdown = OptionMenu(self.window, self.clicked, *year_level)
		#self.dropdown.grid(row = 1, column = 2, padx = 170, pady = (20,2))
    self.dropdown.pack()
    self.year_button = tk.Button(self.window, text = "START", command = self.year_button_input)
    self.year_button.pack()

  # This is a function that creates the page where the questions are asked. It has a text box with the questions and buttons with the available answers that can be picked (the buttons is from calling another function). The question text and a list containing the available answers are inputted
  def ask_questions(self, q, answer_list):
    self.question_text = tk.Text(self.window, height = Q_HEIGHT, width = Q_WIDTH, pady = Q_PADDING, padx = Q_PADDING)
    self.question_text.insert(tk.END, q)
    self.question_text.config(state=DISABLED,wrap=WORD)
    self.question_text.pack()
    self.question_buttons(answer_list) # calls function that creates the actual radio buttons

  # This is a function that creates the buttons that have the possible answers that the user can pick for each question. It uses a for loop to create the buttons. A list containing the available answers in inputted
  def question_buttons(self, answer_list):
    answer_options = ["A", "B", "C", "D"]
    self.answer_button_list = []
    r = IntVar()
    for a in range(len(answer_list)):
      self.answer_button = tk.Radiobutton(self.window, text = answer_list[a], variable = r, value = a, command = partial(self.answer_button_input, answer_options[a]), pady = BUTTON_PADDING) 
      #make a new list with users answers to check all at once at the end
      self.answer_button_list.append(self.answer_button)
      self.answer_button.pack()

  # This is a function that creates a button to go back a question. The current question number is inputted to changes the state of the button to disabled if it is on the first question
  def previous_question(self, question): 
    previous_q_button = tk.Button(self.window, text = "BACK", command = partial(self.previous_button_input, "back"))
    if question == 0:
      previous_q_button['state'] = tk.DISABLED
    else:
      previous_q_button['state'] = tk.NORMAL
    previous_q_button.pack(side = LEFT)

  # This is a function that creates a button to go forward a question. 
  def next_question(self):  
    next_q_button = tk.Button(self.window, text = "NEXT", command = partial(self.next_button_input, "next"))
    next_q_button.pack(side = RIGHT)

  # This is a function that creates a button to submit the quiz. Whether all the questions have been answered or not is inputted
  def submit_quiz(self, completed):
    self.submit_quiz_button = tk.Button(self.window, text = "Submit", state = DISABLED, command = partial(self.submit_button_input, "next"))
    if completed:
      self.submit_quiz_button['state'] = tk.NORMAL
    else:
      self.submit_quiz_button['state'] = tk.DISABLED
    self.submit_quiz_button.pack(side = RIGHT)

  # This is a function that changes the state of the submit button according to if all questions have been answered. This function is specifically only used when the user have answered all questions as they go and is on the last question. Whether all the questions have been answered or not is inputted
  def submit_quiz_state(self, completed):
    if completed:
      self.submit_quiz_button.pack_forget #gets rid of old submit button that is disabled
      self.submit_quiz_button['state'] = tk.NORMAL
    else:
      self.submit_quiz_button['state'] = tk.DISABLED
    self.submit_quiz_button.pack(side = RIGHT)

  # This is a function that creates the end page. It has a text box that congratulates the user and refers to them by the name they entered at the start of the quiz. The text box also tells what the score was, the end message, and asks if the user wants to play again. There is a yes and no button for resetting the quiz
  def end_screen(self, player_name, end_score, total_possible_score, end_message):
    self.end_display = tk.Text(self.window, height=Q_HEIGHT, width=Q_WIDTH, pady = Q_PADDING, padx = Q_PADDING)
    end_text = "Congratulations " + str(player_name) + ". \nYou scored " + str(end_score) + "/" + str(total_possible_score) + ".\n" + end_message + ". \nWould you like to play again?"
    self.end_display.insert(tk.END, end_text)
    self.end_display.config(state=DISABLED, wrap=WORD)
    self.end_display.pack()
    yes_button = tk.Button(self.window, text = "YES", command = partial(self.yes_button_input, "yes"))
    yes_button.pack()
    no_button = tk.Button(self.window, text = "NO", command = self.window.destroy) #closes window if player doesn't want to use program again
    no_button.pack()

  # This is a function that will be called. It displays a error message if a certain condition is fulfilled
  def name_error(self):
    tk.messagebox.showwarning("Warning", message= "Please enter a valid name.")

  # This is a function that will be called. It displays a error message if a certain condition is fulfilled
  def dropdown_error(self):
    tk.messagebox.showwarning("Warning", message = "Please select a year level.")

  # This is a function that clears the current content on the page on the window
  def clear(self):
    for widget in self.window.winfo_children():
      widget.pack_forget()

  # This is a function that makes the name entered visible to the other classes via a controller class
  def name_button_input(self):
    name = self.name_entered.get()
    self.controller.name_entry(name)

  # This is a function that makes the user's answer visible to the other classes via a controller class
  def answer_button_input(self, answer):
    self.controller.send_answer(answer)

  # This is a function that makes the fact that the back button was clicked visible to the other classes via a controller class
  def previous_button_input(self, next_back):
    self.controller.question_change(next_back)

  # This is a function that makes the fact that the next button was clicked visible to the other classes via a controller class
  def next_button_input(self, next_back):
    self.controller.question_change(next_back)
 
  # This is a function that makes the fact that the submit button was clicked visible to the other classes via a controller class 
  def submit_button_input(self, next_back):
    self.controller.question_change(next_back)

  # This is a function that makes the fact that the yes button was clicked visible to the other classes via a controller class
  def yes_button_input(self, yes):
    self.controller.yes_no(yes)

  # This is a function that makes the year level selected visible to the other classes via a controller class
  def year_button_input(self):
    year = self.clicked.get()
    self.controller.year_level_entry(year)

class QuizControl():
  def __init__(self):
    self.gui = GraphicalUserInterface(self) # instantiating the classes
    self.questions = Questions()
    self.score = Score()
    pass

  # This is a function that will call other function in another class that will create the start window and page
  def set_up_window(self):
    self.gui.create_window() # calls a function in the GUI class that creates a window
    self.set_up_name() # calls a function that calls another function in another class

  # This is a function that calls a function in another class that creates the entry box for a name and a button the continue after entering the name
  def set_up_name(self):
    self.gui.ask_name()

  # This is a function that the name entered is 'sent to' and 'dealt with'. It validates the name and also calls functions that will start the quiz according to if the name entered in valid
  def name_entry(self, name):
    self.player_name = name # variable that is the name that was entered in
    self.has_numbers = any(char.isdigit() for char in self.player_name) # variable result that is returned after checking if entered name has numbers in it (if it does, true and vice versa)
    self.invalidChars = set(string.punctuation.replace("_", "")) # a set of invalid characters
    self.has_special_characters = any(char in self.invalidChars for char in self.player_name) # variable result that is returned after checking if entered name has special characters in it (if it does, true and vice versa)
    # the rest of the code will only run if the name entered is not empty, the number of characters  is less than the maximum, there are no numbers in the name entered, and if there are no special characters
    if self.player_name != '' and len(self.player_name) <= int(MAX_NAME_LENGTH) and self.has_numbers == False and self.has_special_characters == False:
      self.q_number = 0 # sets the current question number that the quiz is on to 0
      self.questions.questions_shuffle() # calls a function that shuffles the questions
      self.questions.user_answer_setup() # calls a function that creates an empty array for the users answers to go into when a question is answered
      self.number_of_questions = self.questions.number_of_questions() # defining constant value that is the number of questions
      self.last_question = int(self.number_of_questions) - 1 #defining constant value that is the number of questions minus 1
      self.set_up_year() # calls a function that will call the function in the GUI class that creates a dropdown list
    else: #else, if will call the gui function that makes the error message show up
      self.gui.name_error() # calls a function in the GUI class that will display an error message
      
  # This is a function that will set up the window for a dropdown to be created. The window is cleared and then it calls a function in the GUI class that creates the dropdown    
  def set_up_year(self):
    self.gui.clear() # calls a function in the GUI class that clears the content on the current window
    self.gui.select_year_level(self.questions.year_level_select()) 

  # This is a function that takes in what was selected for the year level dropdown. If it is "selected" (whch is what it intially was), it will call a function in the gui class that displays an error message, else, it will call the funcion that runs the questions
  def year_level_entry(self, year):
    if year == "Select":
      self.gui.dropdown_error()
    else:
      self.loop_questions()

  # This is a function that changes that question number by calling another function in another class and taking in the result of the back and next button being clicked
  def question_change(self, next_back):
    self.q_number = self.questions.question_number(self.q_number, next_back)
    self.gui.clear() # calls a function in the GUI class that clears the content on the current window
    self.loop_questions()

  # This is a function that controls how the asking questions part of the quiz runs. It calls lots of functions in other classes in order to do this
  def loop_questions(self):
    # if the current question number is equal to the number of questions, the quiz is over so it calls a function that runs the commands for when the quiz is finished
    if self.q_number == self.number_of_questions:
      self.quiz_finished()
      return None
    self.gui.clear() # calls a function in the GUI class that clears the content on the current window
    # setting variable names by calling other functions that return certain things when the current question number is inputted into those functions
    self.question = self.questions.question_words(self.q_number)
    self.a_list = self.questions.answer_list(self.q_number)
    # Calling the function that creates the page for asking questions using the two variables defines just above
    self.gui.ask_questions(self.question, self.a_list)
    # If the user is on the last question, it will display a back and submit button
    if self.q_number == self.last_question:
      self.user_answers = self.questions.final_user_answers()
      self.quiz_complete_check = self.questions.all_answered_check(self.user_answers)
      self.gui.previous_question(self.q_number)
      self.gui.submit_quiz(self.quiz_complete_check)
      # otherwise, it will display the back and next buttons for changing the question
    else:
      self.gui.previous_question(self.q_number)
      self.gui.next_question()
    
  # This is a function that takes in the answer that the user selected when answering the question. It then 'sends' that answer to a function that will store the answer in a list. In order to make the submit button change state while on the last question, the function also calls a function that changes the state of the submit button when the user is on the last question 
  def send_answer(self, answer):
    self.questions.user_answer(self.q_number, answer)
    if self.q_number == self.last_question:
      self.user_answers = self.questions.final_user_answers()
      self.quiz_complete_check = self.questions.all_answered_check(self.user_answers)
      self.gui.submit_quiz_state(self.quiz_complete_check)

  # This is a function that controls what happens when the quiz is finished. It calls a function in the GUI class that clears the content on the current window; calls the function that creates the list of correct answers; calls the function that compares the list of the user's answers to the list of correct answers by inputting the number of questions, the list of user answers, and the list of correct answers; and then calls a function that creates and displays the final screen (inputs are the user name, final socre, the nunber of questions, and the final message the depends on the users final score). It also defines some constant values
  def quiz_finished(self):
    self.gui.clear()
    self.correct_answer_list = self.questions.correct_answer()
    self.user_answers = self.questions.final_user_answers()
    self.score.scoring(self.number_of_questions, self.user_answers, self.correct_answer_list)
    self.end_score = self.score.final_score()
    self.end_message = self.score.final_message(self.end_score)
    self.gui.end_screen(self.player_name, self.end_score, self.number_of_questions, self.end_message)

  # This is a function that takes in whether the user wants to do the quiz again according to what button they clicked (yes or no). It then uses that result to reset the score and start the quiz from the start
  def yes_no(self, yes):
    reset = self.questions.reset_quiz(yes) # constant value which is whether the quiz will be reset or not
    self.score.reset_score(reset)
    if reset:
      self.gui.clear() # calls a function in the GUI class that clears the content on the current window
      self.set_up_name() #not set_up_window() cos we do not want to create another window

quiz = QuizControl()
quiz.set_up_window()
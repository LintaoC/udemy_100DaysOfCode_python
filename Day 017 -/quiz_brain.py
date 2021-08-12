class QuizBrain:

    def __init__(self,  question_list):
        #Initialise attributes
        #Below 2 parameters are mandatory and need to be specified when the user is created
        self.question_number = 0 # In which question the user is currently on
        self.question_list = question_list # Question
        self.score = 0
        #print(self.question_list[self.question_number].answer)

    def still_has_question(self):
        total_number_of_question = len(self.question_list)
        actual_question = self.question_number
        #Can return directly the expression, without the IF statement
        return actual_question < total_number_of_question
        """
        total_number_of_question = len(self.question_list)
        actual_question = self.question_number
        if actual_question < total_number_of_question:
            return True
        return False"""


    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question} ? True or False? ")
        self.check_answer(user_answer, current_answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")


"""        return user_input
    
    def check_answer(self, user_input):
        question_number = self.question_number
        correct_answer = self.question_list[question_number].answer

        if user_input == correct_answer:
            print("Yes")
        else:
            print("No")"""

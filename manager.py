def get_results():
    with open("res/user_answers.txt", "r") as user_answers:   
        # Creates empty dict of lists according to the number of questions
        survey_results = {}
        for idx, answer in enumerate(user_answers.readline()):
            if (answer.isdigit()):
                survey_results[idx] = []

        # Fills the lists of the dictionary          
        for line in user_answers:
            for idx, answer in enumerate(line):
                if(answer.isdigit()):
                    survey_results[idx].append(answer)
    print (survey_results)

def count(q_results,satisfaction_number):
    satisfaction_number_counter=0
    for result in q_results:
        if result==satisfaction_number:
            satisfaction_number_counter+=1
    return satisfaction_number_counter

def display():
    print('{:_^15}'.format("Question") +
          '{:_^15}'.format("Strongly Disagree") + 
          '{:_^15}'.format("Somewhat Disagree") + 
          '{:_^15}'.format("Neither Agree nor Disagree") +
          '{:_^15}'.format("Somewhat Agree") +
          '{:_^15}'.format("Strongly Agree"))

def main():
    display()

main()
    
    
          
       



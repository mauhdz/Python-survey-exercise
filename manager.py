from prettytable import PrettyTable
x = PrettyTable()

def get_results():
    survey_results = {}
    try:
        with open("res/user_answers.txt", "r") as user_answers:   
            # Creates empty dict of lists according to the number of questions
            for idx, answer in enumerate(user_answers.readline()):
                if (answer.isdigit()):
                    survey_results[idx] = []
    
            # Fills the lists of the dictionary          
            for line in user_answers:
                for idx, answer in enumerate(line):
                    if(answer.isdigit()):
                        survey_results[idx].append(answer)
        return survey_results
    except:
        print("Something went wrong when reading the file")
        
def count(q_results,satisfaction_number):
    satisfaction_number_counter=0
    for result in q_results:
        res= int(result)
        if res==satisfaction_number:
            satisfaction_number_counter+=1
    
    return satisfaction_number_counter

def display_no_format():
    try:
        survey_results=get_results()
        print survey_results
        
        print('{:^15}'.format("Question") +
              '{:^15}'.format("Strongly Disagree") + 
              '{:^30}'.format("Somewhat Disagree") + 
              '{:^15}'.format("Neither Agree nor Disagree") +
              '{:^20}'.format("Somewhat Agree") +
              '{:-^15}'.format("Strongly Agree"))
    
        with open("res/questions.txt", "r") as questions:
            for idx, question in enumerate(questions):
                print (question)
                for satisfaction_number,element in enumerate(survey_results[idx]):
                    print count(survey_results[idx],satisfaction_number+1)
    except:
        print("Something when wrong while displaying")

def display_pretty():
        
        try:
            survey_results=get_results()
            x.field_names = ["Question", "Strongly Disagree", "Somewhat Disagree", 
                             "Neither Agree nor Disagree","Somewhat Agree",
                             "Strongly Agree"]
            with open("res/questions.txt", "r") as questions:
                for idx, question in enumerate(questions):
                    answers_list=[]
                    for satisfaction_number,element in enumerate(survey_results[idx]):
                        answers_list.append(count(survey_results[idx],satisfaction_number+1))
                    x.add_row([question,answers_list[0], answers_list[1],answers_list[2],answers_list[3],answers_list[4]])
                print(x)
        except:
            print("Check your files")
    
                
def main():
    display_pretty()

main()
    
    
          
       



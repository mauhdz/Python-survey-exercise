import sys

#Returns only valid answer
def get_answer():
    valid_input=False
    
    while not valid_input:
        try:
            answer =int(raw_input());
            if not (1 <= answer <= 5):
                raise ValueError()
            valid_input=True
            return answer
        
        except ValueError:
            print "Enter a value between 1 to 5"      
            
def main():
    print("Hello, answer 5 to 1 according to your satisfaction")    
    with open("res/user_answers.txt","a") as user_answers, open("res/questions.txt", "r") as questions_file: 
        for line in questions_file:
            print (line)
            user_answers.write(bytes(get_answer()))
        user_answers.write("\n")
    print("Thanks for answering the survey!")    

main()



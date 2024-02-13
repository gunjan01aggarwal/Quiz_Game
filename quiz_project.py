#Import libraries.
#csv library for reading csv file.
#colorama library for displaying colourful text.
import csv 
from colorama import Fore

# This list is used for storing data comes from csv file. 
data_list=[]
score=0
#This list is used to store question and options in a particular format.
questions=[]
#Open csv file and append each row in a datalist.

with open ("E:\quizzzz\Quiz.csv",encoding="utf8") as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        data_list.append(row)

#Store question and options and correct answer in a particular format.
for i  in range(0,len(data_list)):
    question=data_list[i]["Question"]
    opt_1=data_list[i]['opt1']
    opt_2=data_list[i]['opt2']
    opt_3=data_list[i]['opt3']       
    opt_4=data_list[i]['opt4']
    correct=data_list[i]['correct_ans']
    questions.append([question,{"A":opt_1,"B":opt_2,"C":opt_3,"D":opt_4,"E":correct}])

 
# Create a function for displaying question and its options.It also track the performance. 
def quizz(questions,score):
    print("*****Welcome to the Quizzz***")
    for q in range(0,len(questions)):    
        Quest=questions[q][0]
        Opts=questions[q][1]
        print(Fore.MAGENTA+f"{q+1}. {Quest} ?")
        print(Fore.WHITE+f"A.{Opts['A']}\nB.{Opts['B']}\nC.{Opts['C']}\nD.{Opts['D']}")

        user_input=input().upper()

        if Opts[user_input]==Opts['E']:
           print(Fore.GREEN+"Your answer is correct.")
           score+=10
        else:
           print(Fore.RED+"Your answer is wrong.")
           print(Fore.WHITE+f"The correct answer is {Opts['E']}.")

    print(Fore.GREEN+f"Your Final Score : Out of {len(questions)*10} is {score}.")
    percentage=(score/len(questions))*100
    if percentage >90:
       print(Fore.GREEN+"    **Excellent performance**   ")
    elif 40< percentage <90:
       print(Fore.YELLOW+"   **Average performance**     ")
    else:
       print(Fore.RED+"      **Bad performance**        ")   
         


quizz(questions,score) 
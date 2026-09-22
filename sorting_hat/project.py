import sys
import csv
def main():
    user_input()
    check_correct_args()
    
    
    data=[]
    try:
        with open(sys.argv[1],"r") as csvfile:
            reader= csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
            output=[]
            for row in data:
                house=select_house(row["characteristic"])
                grade=select_grade(row["birthdate"])
                output.append({"name":row["name"],"house":house,"Grade":grade})
        with open(sys.argv[2],"w") as file:
            writer =csv.DictWriter(file,fieldnames=["name","house","Grade"])
            writer.writerow({"name":"name","house":"house","Grade":"Grade"})
            for row in output:
                writer.writerow({"name":row["name"],"house":row["house"],"Grade":row["Grade"]})


    except FileNotFoundError:
        sys.exit("CSV File does not found")

def check_correct_args():
    if len(sys.argv)<3 and len(sys.argv)>1:
        sys.exit("Too few Command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV file")


def select_house(char):
    if char in ["courage", "loyalty", "adventure","confidence"]:
        return "Griffindor"
    elif char in ["patience", "dedication", "honesty","smartness"]:
        return "Hufflepuff"
    elif char in ["wisdom", "creativity", "perfectionism"]:
        return "Ravenclaw"
    elif char in ["ambition", "competitive", "leadership","knowledge"]:
        return "Slytherin"
    else:
        return "No House"


def select_grade(year):
    age= 2022-int(year)
    grade= age-5
    return "Grade "+ str(grade)

def user_input():
    if len(sys.argv)==1:
        print("You have not entered Command-line arguements\n")
        selection=input("Did you want to know your Individual Grade and alloted House? Type yes or no:-").casefold().strip()
        if selection=="yes":
            user_process()
        else:
            sys.exit("Start the program again and Enter the command-line Arguements")    


def user_process():
    a=input("Enter Your name:").capitalize()
    b=input("Enter Your Characteristic:").casefold().strip()
    c=int(input("Enter Your birth year:"))
    Name=a
    house=select_house(b)
    grade=select_grade(c)
    grade=grade.capitalize()
    if c<2005:
        sys.exit("Oppsie, Your too Big to get addmited at Hogwarts,Don't worry You still have magic left in yourself😉")
    else:    
        print("Name of Addmited Student:",Name)
        print("House Alloted to a Student:",house)
        print("Grade Assigned to a Student:",grade)
        sys.exit("For Addmision purpose You can pass a whole CSV File in command-line Arguements, Thanks for using my Program")



if __name__ == "__main__":
    main()
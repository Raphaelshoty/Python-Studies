from statistics import mean as m

def validOption(option):
    try:
        option in actions
    except TypeError as t:
        print("Option must be a number !")
        return False        
        
    except Exception as e:
        print("Invalid option ", option)
        return False    
    
def enterGrades(dictionarie,name,gradeList):
    dictionarie[name] = gradeList
    print("Grades added... \n", dictionarie )

def removeStudent(dictionarie,name):
    del dictionarie[name]
    print("Student removed...", name)

def average(dictionarie, name):
    return m.mean(dictionarie[name])
    


from statistics import mean as m
actions = {1:"[1] Enter Grades",2:"[2] Remove Student",3:"[3] Student Average Grades",4:"[4] EXIT" }

act = len(actions)

grades = {}

proceed = True

while(proceed):
    print("--Welcome to Grades System--")
    print("\n")

    while(act > 0):
        print(actions.get(act))
        act -= 1

    userOption = int(input("\n What would you like to do today ? "))

    proceed = validOption(userOption)

    if(userOption == 1):
        grade = []
        more = True
        name = str(input("Student's name: "))
        
        while(more):
            score = float(input("Student's grade: "))            
            grade.append(score)
            add = (str(input("Input more ? (yes, no)")))
            if(add.upper() == "YES"):
                more = True
            else:
                more = False
            
        enterGrades(grades,name,grade)
        
    elif(userOption == 2):
        name = str(input("Student's name: "))
        removeStudent(grades,name)
        
    elif(userOption == 3):
        name = str(input("Student's name: "))
        print("Student average: ", average(grades,name))

    elif(userOption == 4):
        break

    if(str(input("Do you want proceed ? (Yes, No)")).upper() == "YES" ):
        proceed = True
    else:
        proceed = False

    act = len(actions)
        
print("Grades... ",grades)
    
    



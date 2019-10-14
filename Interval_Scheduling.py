from dataclasses import *

# struct
@dataclass
class Atividade:
    start: int
    finish: int

# funcao da atividade do deadline
def DeadLineActivities(activities):

    n = len(activities)
    # ordernacao para o deadline
    x=0
    y=1
    while(x<len(activities)):
        y=0
        while(y<len(activities)):
            if(activities[x].finish<activities[y].finish):
                temp = activities[y].finish
                activities[y].finish = activities[x].finish
                activities[x].finish = temp
                temp = activities[y].start
                activities[y].start = activities[x].start
                activities[x].start = temp
            y=y+1
        x=x+1
    
    # print das possiveis atividade deadline
    print("Atividades que podem ser feitas (pelo deadline time): ")

    i = 0
    print("(", activities[i].start, ",", activities[i].finish, ")")

    j = 1
    while(j<len(activities)):
        if(activities[j].start >= activities[i].finish):
            print("(", activities[j].start, ",", activities[j].finish, ")")
            i = j
        j = j+1      

# funcao da atividade do startline
def StartLineActivities(activities):
    
    n = len(activities)
    # ordernacao para o startline
    x=0
    y=1
    while(x<len(activities)):
        y=0
        while(y<len(activities)):
            if(activities[x].start<activities[y].start):
                temp = activities[y].finish
                activities[y].finish = activities[x].finish
                activities[x].finish = temp
                temp = activities[y].start
                activities[y].start = activities[x].start
                activities[x].start = temp
            y=y+1
        x=x+1

    # print das possiveis atividade startline
    print("Atividades que podem ser feitas (pelo start time): ")

    i = 0
    print("(", activities[i].start, ",", activities[i].finish, ")")

    j = 1
    while(j<len(activities)):
        if(activities[j].start >= activities[i].finish):
            print("(", activities[j].start, ",", activities[j].finish, ")")
            i = j
        j = j+1  

# funcao da atividade do slackline
def SlackActivities(activities):

    n = len(activities)
    # ordernacao para o slackline
    x=0
    y=1
    while(x<len(activities)):
        y=0
        while(y<len(activities)):
            if((activities[x].finish - activities[x].start) < (activities[y].finish - activities[y].start)):
                temp = activities[y].finish
                activities[y].finish = activities[x].finish
                activities[x].finish = temp
                temp = activities[y].start
                activities[y].start = activities[x].start
                activities[x].start = temp
            y=y+1
        x=x+1
    
    # print das possiveis atividades de slackline
    print("Atividades que podem ser feitas (pelo slack): ")

    i = 0
    print("(", activities[i].start, ",", activities[i].finish, ")")

    j = 1
    while(j<len(activities)):
        if(activities[j].start >= activities[i].finish):
            print("(", activities[j].start, ",", activities[j].finish, ")")
            i = j
        j = j+1  


activities = [Atividade(5,9), Atividade(1,2), Atividade(0,6), Atividade(5,7), Atividade(8,9)]

print("Atividades a serem analisadas (start time, deadline): \n")

n = 0
while(n<len(activities)):
    print("Atividade",n+1,": ","(", activities[n].start, ",", activities[n].finish, ")")
    n = n +1

# print's das três melhores formas de realizar as atividades
print("\n")
DeadLineActivities(activities)
print("\n")
StartLineActivities(activities)
print("\n")
SlackActivities(activities)

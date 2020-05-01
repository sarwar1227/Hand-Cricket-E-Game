'''Hand Cricket E-Game by SARWAR ALI(github.com/sarwar1227) using Python
           Technologies Required To Run this Code : Pyhton(32/64 bit) version 2/3+
INSTRUCTIONS TO PLAY THIS GAME :
1.First Choose Even/Odd for Toss.
2.Now Enter a random number(range 1-5) because in reality you have 5 fingers only(On a Sarcastic Node).
3.Now If You Wins the Toss,Computer Will Ask for your choice either Batting/Balling.
4.As Per your choice further 2 innings are played between you and computer(Each one will get batting and balling once).
5.Either of the player get bold if your Entered and Computer selected random number is same(Just like in real Hand Cricket Game").
6.Based On Total Score You and Computer Scored..Winner of the game is decided'''
import random,os,sys
even_odd_choice=''
name=input("Enter Your Name : ")
flag=True
score_count_user=0
score_count_computer=0
user_batting_check=True
comp_batting_check=True
user_toss_number=0
num=[1,2,3,4,5]
runs_list=[1,2,3,4,5,6,7,8,9,10]
def start_menu():
    global even_odd_choice,user_toss_number
    print("Hello",name,"!! Welcome to Hand-Cricket Game\nTurn For Toss\n What You Want...Even or Odd")
    even_odd_choice=input("Enter e/E for EVEN and o/O for ODD? : ")
    if even_odd_choice not in ['e','E','o','O']:
        print("Invalid Input.......Press any Key to Refersh")
        input()
        os.system("cls")
        start_menu()
    try:
        user_toss_number=int(input("Enter Toss Number(Range: 1 to 5 )-(becuase you have only 5 Fingers) ? : "))
        if user_toss_number not in num:
            print("Value Not in Range(1-5)............Press any Key to Refresh")
            input()
            os.system("cls")
            start_menu()
    except ValueError:
        input()
        print("Only Integer Value allowed")
        os.system("cls")
        play_again()
def toss_winner():
    global flag,user_toss_number
    x=user_toss_number
    comp_toss_number=random.choice(num)
    y=comp_toss_number
    if (x+y)%2==0 and even_odd_choice in ['e','E']:
        print("You Chose : ",x,"\nYou Won !! ",x,"+",y,"=",x+y," is EVEN")
        flag=True
    elif (x+y)%2!=0 and even_odd_choice in ['e','E']:
        print("You Chose : ",x,"\nYou Lost !! ",x,"+",y,"=",x+y," is ODD")
        flag=False
    elif (x+y)%2!=0 and even_odd_choice in ['o','O']:
        print("You Chose : ",x,"\nYou Won !! ",x,"+",y,"=",x+y," is ODD")
        flag=True
    elif (x+y)%2==0 and even_odd_choice in ['o','O']:
        print("You Chose : ",x,"\nYou Lost !! ",x,"+",y,"=",x+y," is EVEN")
        flag=False
def first_innings():
    global flag,user_batting_check,comp_batting_check,score_count_user,score_count_computer
    if flag==True:
        bat_or_ball=input("What You Want ? Batting or Balling....Enter bat for batting or ball for balling?")
        if bat_or_ball not in ['bat','ball']:
            print("Invalid Choice")
            play_again()
        elif bat_or_ball=='bat':
            print(name,",Your Batting First !!")
            while True:
                try:
                    user_score=int(input("Enter Your Number :"))
                except ValueError:
                    print("Only Integer Value Allowed")
                    input()
                    play_again()
                if user_score<0 or user_score>10:
                    print("You Entered Value Out of Range(1-10)")
                    input()
                    play_again()     
                comp_score=random.choice(runs_list)
                print("Computer Chose : ",comp_score)
                if comp_score==user_score:
                    print("Howzatt !!..........You Bold on Number ",comp_score," Your Final Score",score_count_user)
                    user_batting_check=True
                    comp_batting_check=False
                    break
                score_count_user+=user_score
        elif bat_or_ball=='ball':
            print("Computer Batting First !!")
            while True:
                comp_score=random.choice(runs_list)
                try:
                    user_score=int(input("Enter Your Number :"))
                except ValueError:
                    print("Only Integer Value Allowed")
                    input()
                    play_again()
                if user_score<0 or user_score>10:
                    print("You Entered Value Out of Range(1-10)")
                    input()
                    play_again()
                if comp_score==user_score:
                    print("Howzatt !!..........Computer Bold on Number ",comp_score," Computer Final Score",score_count_computer)
                    user_batting_check=False
                    comp_batting_check=True
                    break
                score_count_computer+=comp_score
    elif flag==False:
        bat_or_ball=random.choice(['bat','ball'])
        print("Computer Chose to",bat_or_ball)
        if bat_or_ball=='bat':
             print("Computer Batting First !!")
             while True:
                 comp_score=random.choice(runs_list)
                 try:
                     user_score=int(input("Enter Your Number :"))
                 except ValueError:
                     print("Only Integer Value Allowed")
                     input()
                     play_again()
                 if user_score<0 or user_score>10:
                     print("You Entered Value Out of Range(1-10)")
                     input()
                     play_again()
                 if comp_score==user_score:
                     print("Howzatt !!..........Computer Bold on Number ",comp_score," Computer Final Score",score_count_computer)
                     user_batting_check=False
                     comp_battin_check=True
                     break
                 score_count_computer+=comp_score
        elif bat_or_ball=='ball':
            print(name,",Your Batting First !!")
            while True:
                try:
                    user_score=int(input("Enter Your Number :"))
                except ValueError:
                    print("Only Integer Value Allowed")
                    input()
                    play_again()
                if user_score<0 or user_score>10:
                    print("You Entered Value Out of Range(1-10)")
                    input()
                    play_again()     
                comp_score=random.choice(runs_list)
                print("Computer Chose : ",comp_score)
                if comp_score==user_score:
                    print("Howzatt !!..........You Bold on Number ",comp_score," Your Final Score",score_count_user)
                    user_batting_check=True
                    comp_batting_check=False
                    break
                score_count_user+=user_score
def second_innings():
    global flag,user_batting_check,comp_batting_check,score_count_user,score_count_computer
    runs_list=[1,2,3,4,5,6,7,8,9,10]
    if user_batting_check==False and comp_batting_check==True:
        print(name,",Your Batting Now !!")
        while True:
            try:
                user_score=int(input("Enter Your Number :"))
            except ValueError:
                print("Only Integer Value Allowed")
                input()
                play_again()    
            if user_score<0 or user_score>10:
                    print("You Entered Value Out of Range(1-10)")
                    input()
                    play_again()
            comp_score=random.choice(runs_list)
            print("Computer Chose : ",comp_score)
            if comp_score==user_score:
                print("Howzatt !!..........You Bold on Number ",comp_score," Your Final Score",score_count_user)
                user_batting_check=True
                break
            score_count_user+=user_score    
    elif user_batting_check==True and comp_batting_check==False:
        print("Computer Batting Now !!")
        while True:
            comp_score=random.choice(runs_list)
            try:
                user_score=int(input("Enter Your Number :"))
            except ValueError:
                print("Only Integer Value Allowed")
                input()
                play_again()
            if user_score<0 or user_score>10:
                print("You Entered Value Out of Range(1-10)")
                input()
                play_again()
            if comp_score==user_score:
                print("Howzatt !!..........Computer Bold on Number ",comp_score," Computer Final Score",score_count_computer)
                comp_batting_check=True
                break
            score_count_computer+=comp_score
def play_again():
    choice=input("Want to play again ? (Y/N)")
    if choice in ['y','Y']:
        os.system("cls")
        result()
    elif choice in ['n','N']:
        print("Thank You....",name," For Playing this Game\nPress Any Key To End...............")
        input()
        sys.exit("Game Ended !!")
    else:
        print("Wrong Input")
        play_again()
def result():
    global score_count_user,score_count_computer
    start_menu()
    toss_winner()
    first_innings()
    second_innings()
    if score_count_user>score_count_computer:
        print(name,".....Wins this Game  !!\nYour Score :",score_count_user,"Computer Score :",score_count_computer)
    else:
        print("Computer.....Wins this Game  !!\nComputer Score :",score_count_computer,"Your Score :",score_count_user)
    play_again()
result()

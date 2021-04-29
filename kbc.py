print("Welcome To you in KBC, \nLets Start The Game...\n")
questions=[
    "How many continents in the world?",
    "2.what is the capital of india?",
    "3.ng me kon sa course padhaya jata hai?"]
options=[
    ["1","5","4","7","50:50"],
    ["chandigarh","delhi","bhopal","chennai","50:50"],
    ["counseling","tourism","software_engineer","agriculture","50:50"]]
solutions=[4,2,3,]       
solution_for_50_50=[[2,4],[2,3],[2,3]]
def kbc_body(questions,options,solutions,solution_for_50_50):
    total_score,total_lose,n,k,d=0,0,0,1,0
    for i in questions:
        print(i)
        print("Here Is Your Options...")
        for i in options[n]:
            if k==6: k=1
            print(k,':', i)     
            k+=1
        inp=int(input("Choose The Correct Answer:"))
        if inp==solutions[n]: 
            print("Congratulation! You Won\n")     
            total_score+=1
        elif inp==5:
            if d==1: print("Sorry!! You Already Choosed This option\n")
            else:
                for i in range(1): print("option Number", solution_for_50_50[n])
                inp=int(input("Enter Your Option Number:"))
                if inp==solutions[n]:                           
                    print("Congratulation! You Won Again\n")
                    total_score+=1
                    d+=1
                else:
                    print("Your Answer Is Wrong.\n")
                    total_lose+=1
        else:
            print("Your Answer Is Wrong.\n")
            total_lose+=1
        n+=1
    print(total_score,"Correct answer")
    print(total_lose,"Wrong answer")
kbc_body(questions,options,solutions,solution_for_50_50)
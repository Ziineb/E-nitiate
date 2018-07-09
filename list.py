from random import randint

def a():
    
    lis=[]
    
    choice="yes"

    while choice=="yes":
        g=eval(input("enter the grade:"))
        choice=input("Is there another grade to enter: yes or no?")
        lis.append(g)

    print("the average is:",sum(lis)/len(lis))
def b():
    choice="yes"
    sum=0
    x=0
    while choice=="yes":
        g=eval(input("enter the grade:"))
        choice=input("Is there another grade to enter: yes or no?")
        sum=sum+g
        x=x+1
    
    print("the average is:",sum/x)

def c():
    g=0
    s=0       
    x=0
    g=input("enter the grade:")

    while g!="":
        s=s+eval(g)
        x=x+1
           

    print("the average is:",s/x)

def game():
    a=0
    n=randint(1,100)
    
    uinput=eval(input("Enter a number"))
    
    while uinput!=n:
        
        if uinput<n:
            print("Low")
            a = a + 1
        elif uinput>n:
            print("high")
            a = a + 1
        if a==3:
            print("GAME OVER")
            break 

        uinput=eval(input("Enter another number"))
    else:
        print("YOU WON!")
        
        
        


    


           

            
            
                
    
        
            
            
    
    

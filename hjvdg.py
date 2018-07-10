def grades():
    sum=0
    g=eval(input("Enter a grade:"))
    while g>=0 and g<=100:
        sum=sum+g
        g=eval(input("enter next grade:"))
    print("The sum of the grades is:",sum)
    
def number():
    n=eval(input("enter a number:"))
    if n==1:
        n=eval(input("enter another number"))
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=(3*n)+1 

        print("the value is",n)

def eat():
    persons=["John","Marissa","Pete","Dayton"]
    restaurants=["Japanese","American","Mexican","French"]
    for i in range(len(persons)):
        for j in range(len(restaurants)):
            if i == j:
                print(persons[i],"loves to eat",restaurants[j])


file=open(listfile.txt,'w')
for i in range(1,5):
    file.write(str(i)+"\n")                
file.close()

            
            





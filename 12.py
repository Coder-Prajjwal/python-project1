#PROJECT 1
import random  #importing random function

def gamewin(comp,you):
    
    if(you!='r' and you!='p' and you!='s'): # if input is wrong
        return -1
    
    elif(comp==you):   #if both choose the same
        return 2
    
    elif(comp=='r'): # checks for all possibilities when computer=rock
       if(you=='p'):
          return 1
       elif(you=='s'):
           return 0
       
    elif(comp=='p'): # checks for all possibilities when computer=paper
        if(you=='r'):
           return 0
        elif(you=='s'):
            return 1 
        
    elif(comp=='s'): # checks for all possibilities when computer= scissor
         if(you=='p'):
            return 0
         elif(you=='r'):
             return 1  
       

randNo=random.randint(1,3) #finds a random number among 1,2,3

if (randNo==1):
    comp='r'
elif(randNo==2): 
    comp='p'
elif(randNo==3): 
    comp='s'    
    

you=input("Your Turn : Rock(r) Paper(p) or Scissor(s) ? ")

a=gamewin(comp,you)

#displaying what computer and we chose
print(f"Computer chose {comp}")
print(f"You chose {you}")

#displaying result
if(a==2):
   print("The game is a TIE !")
elif(a==1):
    print("You WIN !")
elif(a==0):
     print("You LOOSE !")   
elif(a==-1):
    print("Game couldn't process due to wrong input ")
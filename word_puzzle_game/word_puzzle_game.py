import random
def choose():
    words=["RAEHTF","KABRE","RENEG","OAERELANP","SSLAC","ADAT","RED","PORO","TA","OPP","REOSCE",
    "TRIPN","ROTHME","TRSIES","HRORETB","ZAANOM","RCMSOIOTF","OOELGG","OGNAM",
    "AVAUG","ANABAN"

    ]
    pick=random.choice(words)
    
    return pick
correct_answer=["father","break","green","aeroplane","data","red","poor","at","pop","source",
"print","mother","sister","brother","amazon","microsoft","google","mango"
"guava","banana"]


def first_chance():
    print("Hey Champ! lets choose the right word")
def wrong_answer():
    print("oops! wrong ")
def right_answer():
    print("Correct")
first_chance()
i=1
point=0
while i<=5:
    
    a=choose()
    print(a)
    
    user_input=input("Choose the valid word ")
    user_input_lower=user_input.lower()
    if user_input_lower in correct_answer:
        right_answer()
        point=point+1
    else:
        wrong_answer()
        point=point-1
    i+=1
print("Your total score is "+" ",point)
print("play again")

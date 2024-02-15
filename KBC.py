  

           ####################  BASIC KBC GAME   #####################


questions=[

    [
        "A. WHO WAS 1ST PRESIDENT OF INDIA","DR MANMOHAN SINGH","DR RAJENDER PRASAD","J.L NEHRU","M.K GANDHI",3
    ],

    [
        "B. Which god is also known as Gauri Nandan", "Agni","Indra","Hanuman","Ganesha",4
    ],

    [
        "C. What does not grow on tree according to a popular Hindi saying?","money","fruit","flower","leaves",1
    ],

    [
        "D. Which city is known as Pink City in India?","agra","jaipur","mumbai","kerela",2
    ],

    [
        "E. Who wrote India's National Anthem?","Rabindranath Tagore","Lal Bahadur Shastri","Chetan Bhagat","RK Narayan",1
    ],
]

levels=[1000,2000,3000,5000,10000]
money=0

for i in range(0,len(questions)):
    Question=questions[i][0]
    print(f"Question for Rs{levels[i]} is")

    print(Question)

    print(f" 1.{questions[i][1]}     2.{questions[i][2]}")
    print(f" 3.{questions[i][3]}     4.{questions[i][4]}")
    
    r=int(input("enter reply in (1-4)"))
    if(r==questions[i][5]):
        print("correct answer")

        print(f"winning amount {levels[i]}")

        money=money+levels[i]

    else:
        print("Wrong answer")
        print(f"Winning Amount ={money} ")
        break
    
print("END OF THE GAME")
    
  
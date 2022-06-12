"""
3. Write a multiplication game program for kids. The program should give the player
ten randomly generated multiplication questions to do. After each, the program
should tell them whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.
"""

import random
for i in range(0,10):
    num_1 = random.randint(0, 9)
    num_2=  random.randint(0, 9)
    print("Question "+str(i+1)+": "+str(num_1)+"x"+str(num_2))
    kid_answer=int(input("Enter your answer: ",))
    if kid_answer==(num_1)*(num_2):
        print("Right!")
    else:
        print("Wrong.The answer is:",(num_1)*(num_2))

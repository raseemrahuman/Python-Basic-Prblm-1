#A.Answer
Var = input("A class name: ")
score1 = input("Test #1 Score : ")
score2 = input("Test #2 Score : ")
score3 = input("Test #3 Score : ")
sum = int(score1) + int(score2) + int(score3)
#B.Answer
Average = (sum/300)*100
#c.Answer
#Formatting of Average we are using Round() function
#we are Roundoff avarage variable with 1
Roundoff = round(Average, 1)
#print(Roundoff)
#print()
print("\n"+ "Average score:" +" "+str(Roundoff))
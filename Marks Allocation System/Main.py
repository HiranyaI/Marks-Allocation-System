# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:-20210146 / W1912807
# Date:- 17 / 04 / 2022

#Create variables

pass_credit=0
defer_credit=0
fail_credit=0

#User inputs

pass_credit=int(input("Please enter your credits at pass : "))
defer_credit=int(input("Please enter your credits at defer : "))
fail_credit=int(input("Please enter your credits at fail : "))

#Progression Outcome

if pass_credit == 120 and defer_credit ==0 and fail_credit == 0 :
    print("Progress")
                
elif pass_credit == 100 and (defer_credit == 20 and fail_credit == 0) or (defer_credit == 0 and fail_credit == 20):
    print("Progress (module trailer)")

elif (pass_credit == 80 and (defer_credit == 40 and fail_credit == 0) or (defer_credit == 20 and fail_credit == 20) or (defer_credit == 0 and fail_credit == 40)) or (pass_credit == 60 and (defer_credit == 60 and fail_credit == 0) or (defer_credit == 40 and fail_credit == 20) or (defer_credit == 20 and fail_credit == 40)or(defer_credit == 0 and fail_credit == 60)) or (pass_credit == 40 and (defer_credit == 80 and fail_credit == 0) or (defer_credit == 60 and fail_credit == 20) or (defer_credit == 40 and fail_credit == 40)) or (pass_credit == 20 and (defer_credit == 100 and fail_credit == 0) or (defer_credit == 80 and fail_credit == 20) or (defer_credit == 60 and fail_credit == 40)or(defer_credit == 40 and fail_credit == 60)) or (pass_credit == 0 and (defer_credit == 120 and fail_credit == 0) or (defer_credit == 100 and fail_credit == 20) or (defer_credit == 80 and fail_credit == 40)or(defer_credit == 60 and fail_credit == 60)):
    print("Module retriever")

elif (pass_credit == 40 and (defer_credit == 0 and fail_credit == 80)) or (pass_credit == 20 and (defer_credit == 20 and fail_credit == 80) or (defer_credit == 0 and fail_credit == 100)) or (pass_credit == 0 and (defer_credit == 40 and fail_credit == 80) or (defer_credit == 20 and fail_credit == 100) or (defer_credit == 0 and fail_credit == 120)):
    print("Exclude")
    
else :
    print("Please enter valid data")

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:-20210146 / W1912807
# Date:- 17 / 04 / 2022

#Importing sub dolders
import Sub.Submodule_student
import Sub.Submodule_staff_member

#Create variables
user=""

print("*" * 131)
print("\n")

#Get user identity
user=input("If you are a student please enter -> s \nIf you are a staff member -> t \nPlease select : ")

print("\n")

if user == "s":
    Sub.Submodule_student.student()

elif user == "t" :
    Sub.Submodule_staff_member.staff_member()
    
else:
    print("Please enter valid data. ")

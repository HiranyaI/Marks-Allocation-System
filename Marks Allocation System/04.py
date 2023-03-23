# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:-20210146 / W1912807
# Date:- 17 / 04 / 2022

#Create variables

pass_credit=0
defer_credit=0
fail_credit=0
counter_list=[]
progress_list=[]
retriever_list=[]
excluded_list=[]
trailing_list=[]
vertical_list = [[],[],[],[]]
user_inputs=[]
folder=0

need_to_continue="Yes" 
while( need_to_continue=="Yes" ):
    #User inputs
    pass_credit=input("Please enter your credits at pass : ")
    if pass_credit.isalpha() or pass_credit =="":
        print("Integer required")
        break
           
    else:
        pass_credit=int(pass_credit)
        if pass_credit != 0 and pass_credit != 20 and pass_credit != 40 and pass_credit != 60 and pass_credit != 80 and pass_credit != 100 and pass_credit != 120:
            print("Out of range")
            break
        else:
            defer_credit=input("Please enter your credits at defer : ")
            if defer_credit.isalpha() or defer_credit =="":
                print("Integer required")
                break
            else:
                defer_credit=int(defer_credit)
                if defer_credit != 0 and defer_credit != 20 and defer_credit != 40 and defer_credit != 60 and defer_credit != 80 and defer_credit != 100 and defer_credit != 120:
                    print("Out of range")
                    break
                else:
                    fail_credit=input("Please enter your credits at fail : ")
                    if fail_credit.isalpha() or fail_credit =="":
                        print("Integer required")
                        break
                    else:
                        fail_credit=int(fail_credit)
                        if fail_credit != 0 and fail_credit != 20 and fail_credit != 40 and fail_credit != 60 and fail_credit != 80 and fail_credit != 100 and fail_credit != 120:
                            print("Out of range")
                            break

                        else:
                            #Progression Outcome
                            if pass_credit == 120 and defer_credit ==0 and fail_credit == 0 :
                                print("Progress")
                                counter_list.append("*")
                                progress_list.append("*")
                                vertical_list[0].append("*")
                                
                                pass_credit=str(pass_credit)
                                defer_credit=str(defer_credit)
                                fail_credit=str(fail_credit)
                                
                                user_inputs.append("Progress - " + pass_credit + "," + defer_credit + "," + fail_credit)
                
                            elif pass_credit == 100 and (defer_credit == 20 and fail_credit == 0) or (defer_credit == 0 and fail_credit == 20):
                                print("Progress (module trailer)")
                                counter_list.append("*")
                                trailing_list.append("*")
                                vertical_list[1].append("*")

                                pass_credit=str(pass_credit)
                                defer_credit=str(defer_credit)
                                fail_credit=str(fail_credit)
                                
                                user_inputs.append("Progress (module trailer) - " + pass_credit + "," + defer_credit +  "," + fail_credit)

                            elif (pass_credit == 80 and (defer_credit == 40 and fail_credit == 0) or (defer_credit == 20 and fail_credit == 20) or (defer_credit == 0 and fail_credit == 40)) or (pass_credit == 60 and (defer_credit == 60 and fail_credit == 0) or (defer_credit == 40 and fail_credit == 20) or (defer_credit == 20 and fail_credit == 40)or(defer_credit == 0 and fail_credit == 60)) or (pass_credit == 40 and (defer_credit == 80 and fail_credit == 0) or (defer_credit == 60 and fail_credit == 20) or (defer_credit == 40 and fail_credit == 40) or (defer_credit == 20 and fail_credit == 60)) or (pass_credit == 20 and (defer_credit == 100 and fail_credit == 0) or (defer_credit == 80 and fail_credit == 20) or (defer_credit == 60 and fail_credit == 40)or(defer_credit == 40 and fail_credit == 60)) or (pass_credit == 0 and (defer_credit == 120 and fail_credit == 0) or (defer_credit == 100 and fail_credit == 20) or (defer_credit == 80 and fail_credit == 40)or(defer_credit == 60 and fail_credit == 60)):
                                print("Do not Progress – module retriever")
                                counter_list.append("*")
                                retriever_list.append("*")
                                vertical_list[2].append("*")

                                pass_credit=str(pass_credit)
                                defer_credit=str(defer_credit)
                                fail_credit=str(fail_credit)
                                
                                user_inputs.append("Module retriever - " + pass_credit +  "," + defer_credit + "," + fail_credit)

                            elif (pass_credit == 40 and (defer_credit == 0 and fail_credit == 80)) or (pass_credit == 20 and (defer_credit == 20 and fail_credit == 80) or (defer_credit == 0 and fail_credit == 100)) or (pass_credit == 0 and (defer_credit == 40 and fail_credit == 80) or (defer_credit == 20 and fail_credit == 100) or (defer_credit == 0 and fail_credit == 120)):
                                print("Exclude")
                                counter_list.append("*")
                                excluded_list.append("*")
                                vertical_list[3].append("*")

                                pass_credit=str(pass_credit)
                                defer_credit=str(defer_credit)
                                fail_credit=str(fail_credit)
                                
                                user_inputs.append("Exclude - " + pass_credit + "," + defer_credit + "," + fail_credit)

                            else:
                                print("Total incorrect")

    

    #If user wants to enter another set of data
    try_again = input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results :")
    if try_again == "y":
        print("\n")
        continue
    
    elif try_again == "q":
        
        print("--------------------------------------------------------------------------------------------")
        print("\n")

        #Horizontal histogram

        print("Horizontal Histogram")
        
        print("Progress  ",len(progress_list),":","*" * len(progress_list))

        print("Trailer   ",len(trailing_list),":","*" * len(trailing_list))

        print("Retriever ",len(retriever_list),":","*" * len(retriever_list))
              
        print("Excluded  ",len(excluded_list),":","*" * len(excluded_list))
              
        print("\n")

        #Vertical histogram

        print("Vertical Histogram")

        print("\n")
        
        print("Progress        Trailing        Retriever        Excluded")
        for i in range(len(vertical_list)):
            for x in vertical_list:
                try:
                    print("   ",x[i], end = "           ")
                except:
                    print("   ","           ",end= " ")

            print ()

        print("\n")

        #Print user inputs 
        for j in range (0,len(user_inputs)):
                        print(user_inputs[j])

        print("\n")

        print(len(counter_list) , "outcomes in total.")
                        
        print("\n")
        print("--------------------------------------------------------------------------------------------")

        #Text file
        folder=open("text.txt","w")
        for j in range (0,len(user_inputs)):
            folder.write(user_inputs[j])
            folder.write("\n")
        folder.close()

        print("\n")

        need_to_continue="No"
        break
    
    else:
        print("Please enter valid data")
        need_to_continue="No"
        break

    




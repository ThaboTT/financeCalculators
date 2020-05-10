import math

# ---------This Programmes contains two different financial calculators-------
# the investment calculator and
# the bond calculator


calculator_type = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

investment      - to calculate the amount of interest you'll earn on interest
bond            - to calculate the amount you'll have to pay on a home loan

""")

if calculator_type.lower() == "investment":                       # 'lower()' converts inputted 'calculator_type' value to lower case
   p = int(input("Enter the deposit amount in rands:"))
   r = int(input("Enter the interest rate (as a percentage):"))
   t = int(input("Enter the investment plan period (in years):"))

   sim_interest_fom = math.ceil(p *(1 + (r/100) * t))              # simple interest formulae
   com_interest_fom = math.ceil(p * math.pow((1 + (r/100)),t))    # compound interest formulae

   interest = input("Enter your chosen interest (simple or compound):")


   if interest.lower() == "simple":
                 
    print("You will earn a total amount of" + " " + "R" + str(sim_interest_fom) + " " + "after a period of" + " " + str(t) + " " + "years" + " " + "at a rate of" + " " + str(r) + "%")

   elif interest.lower() == "compound":
    
    print("You will earn a total amount of" + " " + "R" + str(com_interest_fom) + " " + "after a period of" + " " + str(t) + " " + "years" + " " + "at a rate of" + " " + str(r) + "%")

   else :
       print("Invalid entry, n\Enter 'simple or compound'")      # error message if the user inputs neither 'simple' nor 'compound'
                                   
                             
elif calculator_type.lower() == "bond" :
                 pv = int(input("Enter the present value of the house in rands:"))
                 r = int(input("Enter the interest rate (as a percentage):"))
                 t = int(input("Enter the payback period (number of months):"))
                 
                 bond_fom = math.ceil(pv * (((r/100) * math.pow((1 + (r/100)),t))/(math.pow((1 + (r/100)),t) - 1)))    # bond repayment formulae
                             
                 print("R" + str(bond_fom) + " " + "per month will be paid" + " " + "to pay back the home loan over a period of" + " " + str(t) + "months" + " " + "at an interest rate of" + " " + str(r) + "%")

else :
        print("Invalid entry, n\Enter 'investment or bond'")        # error message if the user inputs neither 'investment' nor 'bond'


# Explanation
# The programme will first check what type of calculator has been inputted
# The first 'if' is executed if investment is inputted in which parameters questions will be prompted. 
# When the 'interest' type is inputted the programme will check the if the first 'if' within the investment calculator programme and execute the print statement if the inputted value is true.
# if is not, the second 'elif' checked and the print statement executed if is true
# if it is not the 'else' print statement will be executed and the error message displayed                                 

# if bond is inputted the programme will execute 'elif' and prompt parameters questions and execute the print statement
# if not, 'else' print statement will be executed and the error message displayed

## 6.100A PSet 1: Part A

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary=float(input('How much is your yearly salary?: '))
portion_saved=float(input('What partion of your salary to be saved? (0.1 to 1.0): '))
cost_of_dream_home=float(input('What is the cost of dream home?: '))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment=cost_of_dream_home*0.25
amount_monthly_saved=yearly_salary/12
amount_saved=0
anual_rate=0.05
mounths=0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while (amount_saved<portion_down_payment):
    month_founds=amount_saved*(anual_rate/12)
    amount_saved+=((amount_monthly_saved*portion_saved)+month_founds)
    mounths+=1

print(mounths)
# Budget-Planning

# Subpackage1:user #
*Module1:instruction
  *In this module, a user can get information of what services are available, decide if he is interested in the serivces and if he want to share this serivce with friends.
*Module2:passwordmemorizer
  *In this module, a user can save his account information(userid, password) in computer by `create`, update information by `update`, show information by `show` and delete information by `delete`.
*Module3:recommendation
  *In this module, a user is require to input his personal information.Based on his information, we provide recommended resources for him. Also collect the information about membership bugeting.
  
# Subpackage2: Budget

Free Membership
 show_budget_chart():
  Shows chart of current savings vs goal
add_amount():
Add money to the savings.
withdraw_amount():
Withdraw money from the savings

Basic Membership
user_expenditure_data():
			Get user’s data on expenditure area and the expenditure for a month
expenditure_chart():
	Displays graph of user expenditure made under each category
analysis_and_budget_suggestion():
	Displays three options for budget savings on top most concern area
reward_calculator():
Calculates the reward for each of the three options

Premium Membership(Basic Membership)
ideal_expenditure_chart(user_salary)
Displays graph of ideal vs user expenditure made under each category
analysis_and_budget_suggestion() : overridden
Displays three options for budget savings on op most concern areas
reward_calculator  : overridden
Calculates the reward for each of the three options

   

# Budget-Planning

# Subpackage1:user #
* Module1:instruction
  	* Service Available: Show the instruction of each service
  	* Interest: Decide if a user is interested in the serivces
  	* Share: If a user want to share this serivce with friends and to whom.
* Module2:passwordmemorizer
  	* Save his account information(userid, password) in computer by `create`
  	* Update information by `update`
  	* Delete information by `delete`
  	* Show information by `show`
* Module3:recommendation
  	* Personal Information:collect information
  	* Recommended resources:website, news, social media platforms
  	* Membership bugeting:free, baisc, premium
  
# Subpackage2: Budget

* **Module1:Free Membership**
 	* show_budget_chart(): 
 		- Shows chart of current savings vs goal
	* add_amount(): 
		- Add money to the savings
	* withdraw_amount():
		- Withdraw money from the savings

* **Module2:Basic Membership**
	* user_expenditure_data(): 
		- Get user’s data on expenditure area and the expenditure for a month
	* expenditure_chart():
		- Displays graph of user expenditure made under each category
	* analysis_and_budget_suggestion(): 
		- Displays three options for budget savings on top most concern area
	* reward_calculator():
		- Calculates the reward for each of the three options

* **Module3:Premium Membership(Basic Membership)**
	* ideal_expenditure_chart(user_salary):
		- Displays graph of ideal vs user expenditure made under each category
	* analysis_and_budget_suggestion() (overridden):
		- Displays three options for budget savings on op most concern areas
	* reward_calculator()  (overridden):
		- Calculates the reward for each of the three options

   

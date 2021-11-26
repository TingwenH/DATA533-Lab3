import pandas as pd
import plotly.express as px

class BasicMembership:
    def __init__(self) :
        pass

    def user_expenditure_data(self):        
        print("Please enter variable expenditure. I would call insurances as fixed expenditure that cannot be avoided at all costs")
        user_data=pd.read_excel('/home/saisree/Desktop/Labs/Block3/533-softwaredev/Lab2/Budget-Planning/package/budget subpackage/user_data.xlsx')
        data=user_data.T
        data.columns=data.iloc[0].values        
        data=data.iloc[1: , :]        
        return data

    def expenditure_chart(self):
        monthly_allowance=10000
        data=self.user_expenditure_data()        
        labels=data.columns
        values=data.iloc[0].values/monthly_allowance      
        figure = px.pie(data,values=values,names=labels,hole=0.3,color_discrete_sequence=px.colors.sequential.RdBu)
        figure.show()

    def analysis_and_suggestion(self):
        monthly_allowance=10000
        data=self.user_expenditure_data()  
        expenditure_list=list(data.iloc[0].values)
        total_expenditure=sum(expenditure_list)
        max_expenditure=max(expenditure_list)
        index_max_expenditure=expenditure_list.index(max_expenditure)
        max_expenditure_area=data.columns[index_max_expenditure]                
        expenditure_allowance_percentage=round((max_expenditure/monthly_allowance)*100,2)
        expenditure_total_expense_percentage=round((max_expenditure/total_expenditure)*100,2)
        print("{} accounts for {} % of the monthly allowance and {} % of the total expenditure".format(max_expenditure_area,expenditure_allowance_percentage,expenditure_total_expense_percentage))
        percentage_list=[10,20,25]    
        reduced_expenditure=[ (1-0.01*percent)*max_expenditure for percent in percentage_list]    
        savings_per_month=[0.01*percent*max_expenditure for percent in percentage_list]        
        print("Based on your profile, our recommendation are the following. Choose the one that is most appropriate for you")
        print("1] Reduce the expenditure on shopping from {} to {} thus savings {} per month".format(max_expenditure,reduced_expenditure[0],savings_per_month[0]))
        print("2] Reduce the expenditure on shopping from {} to {} thus savings {} per month".format(max_expenditure,reduced_expenditure[1],savings_per_month[1]))
        print("3] Reduce the expenditure on shopping from {} to {} thus savings {} per month".format(max_expenditure,reduced_expenditure[2],savings_per_month[2]))
        option=int(input("Enter an option to know about the reward points and expected annual savings goal"))        
        reward=self.rewards_calculator(option,savings_per_month[option-1])   
        print(reward)
        print("Your expected annual savings is {} !!!!".format(savings_per_month[option-1]*12))
        return savings_per_month[option-1]*12

    def rewards_calculator(self,option,savings):
        reward=""
        if(option==1):
            reward="Gift coupon to Starbucks worth {} per month".format(0.015*savings)
        elif(option==2):
            reward="{} off of your next purchase on hudson bay".format(0.15*savings)
        elif(option==3):
            reward="25% off of your membership for the next year"
        return reward
        

basic=BasicMembership()
#basic.expenditure_chart()
annual=basic.analysis_and_suggestion()

            
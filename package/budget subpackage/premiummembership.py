from basicmembership import BasicMembership
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import freemembership

class PremiumMembership(BasicMembership):
    ideal_labels=["Groceries","Travel","Shopping","Restaurant","Others"]
    ideal_values=[4,2,3,1,1]

    def __init__(self):
        pass

    def expenditure_chart(self):        
        monthly_allowance=10000
        data=self.user_expenditure_data()
        expenditure_allowance_percentage=data.iloc[0].values*100/monthly_allowance
        ideal_data= pd.DataFrame([PremiumMembership.ideal_values],columns=PremiumMembership.ideal_labels)
        labels=data.columns
        new_labels=[x if x in PremiumMembership.ideal_labels else "Others" for x in labels]
        new_data=pd.DataFrame([data.iloc[0].values,expenditure_allowance_percentage],columns=new_labels)
        whole_data= pd.concat([new_data,ideal_data])
        self.__whole_data=whole_data.fillna(0)        
        whole_labels=self.__whole_data.columns  
        print(self.__whole_data)      
        fig = go.Figure(data=[
            go.Bar(name='Actual', x=whole_labels, y=self.__whole_data.iloc[1].values),
            go.Bar(name='Ideal', x=whole_labels, y=self.__whole_data.iloc[2].values)
        ])        
        fig.update_layout(barmode='group')
        fig.show()   
        

    def analysis_and_suggestion(self):        
        diff_percentages=self.__whole_data.iloc[1].values-self.__whole_data.iloc[2].values
        whole_labels=self.__whole_data.columns
        top_three_areas=sorted(zip(diff_percentages, whole_labels), reverse=True)[:3]
        percentage_list=[10,20,25] 
        expenditure_diff,Areas=list(zip(*sorted(zip(diff_percentages, whole_labels), reverse=True)[:3]))
        savings_per_month=[]
        for ind1 in range(0,len(percentage_list)):
            sum_savings=0
            print(ind1+1,"--------------------------------------------------------------------------------")
            for ind2 in range(0,len(expenditure_diff)):
                per=percentage_list[ind1]
                diff=expenditure_diff[ind2]
                #sugg_per=round((1-0.01*per)*diff,2)
                #print(Areas[ind2],diff)
                curr_expenditure_amount=self.__whole_data.loc[0,Areas[ind2]].values[0]
                
                new_expense=round((1-0.01*per)*curr_expenditure_amount)
                new_savings=round(0.01*per*curr_expenditure_amount)
                sum_savings+=new_savings
                
                print("Reduce the expenditure on {} from {} to {} thus savings {} per month".format(Areas[ind2],curr_expenditure_amount,new_expense,new_savings))
            savings_per_month.append(sum_savings)
        option=int(input("Enter an option to know about the reward points and expected annual savings goal"))        
        reward=self.rewards_calculator(option,savings_per_month[option-1])   
        print(reward)
        print("Your expected annual savings is {} !!!!".format(savings_per_month[option-1]*12))        
        return savings_per_month[option-1]*12
    
    def rewards_calculator(self, option, savings):
        reward=""
        if(option==1):
            reward="Gift coupon to Starbucks and McDonalds worth {} per month".format(0.015*savings)
        elif(option==2):
            reward="{} off of your next purchase on hudson bay with unlimited validity ".format(0.2*savings)
        elif(option==3):
            reward="50% off of your membership for the next year"
        return reward
        #return super().rewards_calculator(option, savings)

if __name__=="__main__":
    #print("lala")
    pm=PremiumMembership()
    pm.expenditure_chart()
    annual=pm.analysis_and_suggestion()
    fm =freemembership.FreeMemberShip(annual)
    fm.add_amount(1000)
    #
    #pm.ideal_expenditure_chart()
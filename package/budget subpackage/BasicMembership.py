import pandas as pd
import plotly.express as px

class BasicMembership:
    def __init__(self) :
        pass
    def user_expenditure_data(self):
        #data_method=int(input())
        print("Please enter variable expenditure. I would call insurances as fixed expenditure that cannot be avoided at all costs")
        user_data=pd.read_excel('/home/saisree/Desktop/Labs/Block3/533-softwaredev/Lab2/Budget-Planning/package/budget subpackage/user_data.xlsx')
        data=user_data.T
        data.columns=data.iloc[0].values
        #print(user_data.iloc[1])
        #data.columns=user_data.iloc[1]
        data=data.iloc[1: , :]
        
        return data

    def expenditure_chart(self):
        data=self.user_expenditure_data()        
        labels=data.columns
        values=data.iloc[0].values        
        figure = px.pie(data,values=values,names=labels,hole=0.3,color_discrete_sequence=px.colors.sequential.RdBu)
        figure.show()

    def analysis_and_suggestion(self):
        pass
    
        
basic=BasicMembership()
basic.expenditure_chart()
        
            
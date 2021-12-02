# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +

def list():
    print('1.Password Memorizer 2.Budget Planning 3.Suggestion/Report')
    
def show(service_number):
    if service_number == 1:
        print('This service can store your userid and password.')
    elif service_number == 2:
        print('This service can help you manage your money and making a montly budget plan.')
    elif service_number == 3:
        print('This service can give you some suggestions on how to save your money.')
    else:
        print('The service you chosed is available.Pleas provide a vaild service number.')

def choice(c_num):
    if c_num == 1:
        print('This service is include in free membership')
    elif c_num == 2:
        print('This service is include in baisc membership. The monthly sibscription fee is $10.')
    elif c_num == 3:
        print('This service is include in premium membership. The monthly sibscription fee is $20.')
    else:
        print('The service you chosed is available.Pleas provide a vaild service number.')
    

# +



# -



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

class personal_info:
    def __init__(self,userid,age,email):
        self.userid = userid
        self.age = age
        self.eduction = email
    def show(self):
        print('Userid:{} Age:{} Education:{}'.format(self.userid,self.age,self.eduction))
    def update(self,newuserid,newage,newemail):
        self.userid = newuserid
        self.age = newage
        self.eduction = newemail
    def delete(self):
        self.userid = ''
        self.age = ''
        self.eduction = ''



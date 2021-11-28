{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "ea1c8168-a750-44ef-bf67-6644d0ab9238",
   "metadata": {},
   "outputs": [],
   "source": [
    "class password:\n",
    "    \n",
    "    def __init__(self,userid,password):\n",
    "        self.userid = userid\n",
    "        self.password = password\n",
    "    \n",
    "\n",
    "    def update(self,newuserid, newpassword):\n",
    "        self.userid = newuserid\n",
    "        self.password = newpassword\n",
    "        return self.userid,self.password\n",
    "    \n",
    "    def show(self):\n",
    "        print('userid: {} password: {}'.format(self.userid,self.password))\n",
    "    \n",
    "    def delete(self):\n",
    "        self.userid = ''\n",
    "        self.password = ''\n",
    "        return self.userid,self.password"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10a524b1-e1c8-47d2-bfc7-bb8b03c48436",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90db68df-4e71-4521-9017-f100f267628f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

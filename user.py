import getpass
import random, string

class User():
    '''
    A class that prompts user to signup and login to generate passwords
    '''
    user_list = []
    def __init__(self,f_name,l_name,u_name,psswd):
        '''
        a function to define user proprties
        '''
        self.f_name = f_name
        self.l_name = l_name
        self.u_name = u_name
        self.psswd = psswd
    def save_user(self):
        '''
        a function that saves user
        '''
        User.user_list.append(self)
    def check_if_userExist(u_name,psswd):

        '''
        A function to check if the user with the entered credentials exist
        '''

        current_user = " "
        for user in User.user_list:
            if user.u_name == u_name and user.psswd == psswd:
                current_user = user.u_name
        return current_user

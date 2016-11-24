##############################################
#
# Database Interface for Tattle_bot (TinyDB)
#
#   Requirements: TinyDB, pyTelegramBotAPI
#
#############################################

from tinydb import TinyDB, Query
import random
from datetime import datetime

ERR_FAILED_TO_ADD_USER = -1
ERR_ALREADY_EXISTS = -2


class Tattle_dbInterface:
    # Variables
    database_file = "tattle_users.json"

    # Initialize the constructor for this class
    def __init__(self):
        pass

    # Check if a user with this chatid exists in the database
    def CheckUserExists(self, chatid, username):
        db = TinyDB(database_file)
        query = Query()

        # result is an array of usernames of this group chat
        result = db.search( query.chatid == chatid )
        usernames = result[0]["usernames"]
        
        # Check if username is in the list
        if username in usernames:
            return True
        else:
            return False
    
    # Get list of usernames from db given a chatid
    def getUsers(self, chatid):
        db = TinyDB(database_file)
        query = Query()

        results = db.search( query.chatid == chatid)
        usernames = results[0]["usernames"] 

        return usernames

    # Add user to tattle's database
    def addUser(self, chatid, username):
        db = TinyDB(database_file)
        query = Query()

        # Error Handling : Check if user is already added
        if self.CheckUserExists(chatid, username) == True:
            return ERR_ALREADY_EXISTS
        else:
            usernames = getUsers(chatid)
            usernames.append(username)
            didSucceed = db.update({'usernames': usernames}, query.chatid == chatid)

        # Error handling : Check if successfully added
        if didSucceed != [1]:
            return ERR_FAILED_TO_ADD_USER
        
        return 0

    # Remove user from tattle's database
    def removeUser(self, chatid, username):
        pass # Don't think we need this


    # Pick a random user from the database of this current chat
    def pickUser(self, chatid):
        db = TinyDB(database_file)
        query = Query()
        current_time = datetime.now()
        
        # Get users of this group chat
        result = db.search(query.chatid == chatid)
        users = result[0]["usernames"]

        # Pick a random user
        user_count = len(users) 
        random_number = random.randint(0, user_count-1)
        chosen_user = users[random_number]

        return chosen_user




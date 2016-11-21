##############################################
#
# Database Interface for Tattle_bot (TinyDB)
#
#   Requirements: TinyDB, pyTelegramBotAPI
#
#############################################

import tinydb import TinyDB, Query
import random
from datetime import datetime
import json

ERR_FAIL_TO_ADD_USER = -1
ERR_ALREADY_EXISTS = -2


class Tattle_dbInterface:
    # Variables
    database_file = "tattle_users.json"
    current_users = []

    # Initialize the constructor for this class
    def __init__(self):
        pass

    # Check if a user with this chatid exists in the database
    def CheckUserExists(self, chatid, username):
        db = TinyDB(database_file)
        query = Query()

        # result is an array of usernames of this group chat
        result = db.search( (query.chatid == chatid) && (query.usernames == usernames) )
        usernames = result[0]["usernames"]
        
        # Check if username is in the list
        if username in usernames:
            return True
        else:
            return False
    
    # Add user to tattle's database
    def addUser(self, chatid, username):
        db = TinyDB(database_file)
        query = Query()

        # Error Handling : Check if user is already added
        if self.CheckUserExists(chaid, username) == True:
            return ERR_ALREADY_EXISTS
        
        chat_usernames = db.insert( {'chatid': chatid, 'username': username} )

        # Error handling : Check if successfully added
        if new_elementID == []:
            return ERR_FAIL_TO_ADD_USER
        
        return 0

    # Remove user from tattle's database
    def removeUser(self, chatid, username):
        pass

    # Get the user count of this group
    def getUsersCount(self, chatid):
        db = TinyDB(database_file)
        query = Query()

        results = db.search((query.chaid == chatid))

    # Pick a random user from the database of this current chat
    def pickUser(self, chatid):
        db = TinyDB(database_file)
        query = Query()
        current_time = datetime.now()

        result = db.search(chatid == chatid)

        users = result[0]["usernames"]

        user_count = len(users) 
        random_number = random.randint(0, user_count)
        chosen_user = users[random_number]

        return chosen_user

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

    # Initialize the constructor for this class
    def __init__(self):
        pass

    # Check if a user with this chatid exists in the database
    def CheckUserExists(self, chatid, username):
        db = TinyDB(database_file)
        query = Query()

        results = db.search( (query.chatid == chatid) && (query.username == username) )

        if(results == []):
            return False
        else
            return True
    
    # Add user to tattle's database
    def addUser(self, chatid, username):
        db = TinyDB(database_file)

        # Error Handling : Check if user is already added
        if self.CheckUserExists(chaid, username) == True:
            return ERR_ALREADY_EXISTS

        new_elementID = db.insert( {'chatid': chatid, 'username': username} )

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
        # TODO: make insert add user an array to key of chatid
        results = db.search((query.chaid == chatid))

    # Pick a random user from the database of this current chat
    def pickUser(self, chatid, username):
        current_time = datetime.now()
        user_count = 
        random_number = random.randint(0,)
        
        # TODO: Finish this
        return chosen_user

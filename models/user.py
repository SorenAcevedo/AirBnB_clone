#!/usr/bin/python3
""" User Class """


def User(BaseModel):
    """ User Class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """ Initializated Method """
        super().__init__()

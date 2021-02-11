#!/usr/bin/python3
""" Base class """
import uuid
from datetime import datetime


class BaseModel():
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        """ Initializated Method """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """ Save Method """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Convert to dictionary """
        attr = vars(self).keys()
        dic = {"__class__": self.__class__.__name__}
        for k in attr:
            if k in ["created_at", "updated_at"]:
                dic.update({k: getattr(self, k).isoformat()})
            else:
                dic.update({k: getattr(self, k)})
        return dic

    def __str__(self):
        """ String method"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

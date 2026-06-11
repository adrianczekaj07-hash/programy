class Tier:
    def __init__(self, alter):
        self.__alter = alter

    def __getAlter(self):
        return self.__alter

    def __setAlter(self, alter):
        self.__alter = alter

    alter = property(__getAlter, __setAlter)
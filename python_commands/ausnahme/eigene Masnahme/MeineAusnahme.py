class MeineAusnahme(BaseException):

    def __init__(self):
        print("Ausnahme von Typ", type(self), "wurde geworfen")
        
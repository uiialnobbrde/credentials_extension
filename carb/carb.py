

g_1 = 0
g_2 = 0
g_3 = 0
h_0 = 0
p = 0

def send() -> None:
    return

def convert_to_field_element(x1: int, x2: int, x3: int, alpha: int) -> tuple:
    return (x1, x2, x3, alpha)

def _subgroup_generator():
    return

def verify_signature():
    return

class DiffieHellman:
    def __init__(self):
        pass

def compute_credential(x1: int, x2: int, x3: int, alpha: int) -> int:
    x1, x2, x3, alpha = convert_to_field_element(x1, x2, x3, alpha)
    cred = (pow(g_1, x1) * pow(g_2, x2) * pow(g_3, x3)) % p
    return cred

def compute_random(w1: int, w3: int, w4: int) -> int:
    rand = (pow(g_1, w1) * pow(g_2, w3) * pow(g_3, w4)) % p
    return rand

def encrypt():
    return



class CA:
    """"""
    def __init__(self, g_1: int, g_2: int, g_3: int, h_0: int, p: int):
        self.g_1 = g_1
        self.g_2 = g_2
        self.g_3 = g_3
        self.h_0 = h_0
        self.p = p

    def compute_credential(self, x1: int, x2: int, x3: int, alpha: int) -> int:
        x1, x2, x3, alpha = convert_to_field_element(x1, x2, x3, alpha)
        cred = (pow(self.g_1, x1) * pow(self.g_2, x2) * pow(self.g_3, x3)) % self.p
        return cred

class Initiator:
    """"""
    def __init__():
        """"""
        return 

    @staticmethod
    def send():
        """"""
        return 

    def _generate_parameters():
        """"""
        return

    def sign():
        """"""
        return 
    
    def verify_signature():
        """"""
        return 

class Responder:
    """"""
    def __init__():
        """"""
        return 

    @staticmethod
    def send():
        """"""
        return 
    
    def _generate_parameters():
        """"""
        return

    def sign():
        """"""
        return 
    
    def verify_signature():
        """"""
        return 

    def verify_equality():
        """"""
        return 
    
from pydantic import Basemodel,Field

class EmailCreate(Basemodel):
    receiver_email:str
    subject:str
    body:str
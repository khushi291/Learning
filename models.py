from tortoise import fields, models

from tortoise.contrib.pydantic import pydantic_model_creator

class Customers(models.Model):
    Cust_ID: fields.IntField(pk=True, index=True, default=True)
    Phone_No: fields.CharField(max_length=10)
    Email_ID: fields.CharField(max_length=20)
    Risk_Flag: fields.CharField(max_length=20)
    
    class PydanticMeta:
        pass
    
Customer_Pydantic = pydantic_model_creator(Customers, name="Customer")
CustomerIn_Pydantic = pydantic_model_creator(Customers, name="CustomerIn", exclude_readonly=True)
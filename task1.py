from fastapi import FastAPI, HTTPException
from models import Customers, CustomerIn_Pydantic, Customer_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel

app=FastAPI()

class Message(BaseModel):
    message: str

@app.get('/')
async def index():
    return {"Hello": "World"}

@app.post('/insert_customer', response_model = Customer_Pydantic)
async def create_customer(customer: CustomerIn_Pydantic):
    new_customer = await Customers.create(**customer.dict(exclude_unset = True))
    return await Customer_Pydantic.from_tortoise_orm(new_customer)


@app.get('/get_all')
async def get_all():
    return await Customer_Pydantic.from_queryset(Customers.all())


@app.get('/get_customer_by_id/{id}', response_model = Customer_Pydantic, responses = {404: {"model": HTTPNotFoundError}})
async def get_customer(id: int):
    return await Customer_Pydantic.from_queryset_single(Customers.get(cust_id = id))


@app.put("/update_customer/{id}", response_model = Customer_Pydantic, responses = {404: {"model": HTTPNotFoundError}})
async def update_customer(id: int, customer: Customer_Pydantic):
    await Customers.filter(cust_id = id).update(**customer.dict(exclude_unset = True))
    return await Customer_Pydantic.from_queryset_single(Customers.get(cust_id = id))


@app.delete("/delete_customer/{id}", response_model = Message, responses = {404: {"model": HTTPNotFoundError}})
async def delete_customer(id: int):
    deleted_customer = await Customers.filter(cust_id = id).delete()
    if not deleted_customer:
        raise HTTPException(status_code = 404, detail = "This customer is not found.")
    return Message(message = "Succesfully Deleted")


register_tortoise(
    app,
    db_url = "postgres://postgres:khushi@localhost:5432/FastApi",
    modules = {'models' : ['models']},
    generate_schemas = True,
    add_exception_handlers = True,
)

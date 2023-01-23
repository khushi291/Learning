from unittest import result
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app=FastAPI()

class Customer(BaseModel):
    cust_id: int
    phone_no: str
    email_id: str
    risk_flag: str

try:
    conn = psycopg2.connect(host="localhost", database="FastApi", user="postgres", password="khushi", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successful!")
except Exception as error:
    print("Connection to Database failed!")
    print("Error: ", error)


@app.get("/get_all/")
def get_all():
    cursor.execute("""Select * from Customers""")
    cust = cursor.fetchall()
    return cust

@app.get("/get_customer_by_id/{cust_id}")
def get_customer(cust_id: int):
    cursor.execute("""Select risk_flag from Customers where cust_id = %s """, str(cust_id))
    result = cursor.fetchone()
    return result

@app.get("/get_customer/")
def get_customer_by_phone_no_and_email_id(ph_no: str, email: str):
    cursor.execute("""Select risk_flag from Customers where phone_no = %s and email_id = %s """, ((ph_no), (email)))
    result = cursor.fetchone()
    return result

@app.post("/insert_customer/")
def create_customer(customer: Customer):
    cursor.execute("""Insert into Customers (cust_id, phone_no, email_id, risk_flag) values(%s, %s, %s, %s) returning * """, 
    (customer.cust_id, customer.phone_no, customer.email_id, customer.risk_flag))
    new_customer = cursor.fetchone()
    conn.commit()
    return new_customer

@app.put("/update_customer/{cust_id}")
def update_customer(cust_id: int, customer: Customer):
    cursor.execute("""Update Customers set phone_no = %s, email_id = %s, risk_flag = %s where cust_id = %s returning * """,
    (customer.phone_no, customer.email_id, customer.risk_flag, cust_id))
    updated_customer = cursor.fetchone()
    conn.commit()
    return updated_customer


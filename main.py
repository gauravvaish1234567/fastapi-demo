from fastapi import FastAPI
from database import ConnectDatabase
from dotenv import load_dotenv
import os
load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
database = os.getenv("DB")

app = FastAPI()



connection = ConnectDatabase(host, user, password, database)
@app.get("/")
async def root():
    return {"message":"Api Running"}

@app.get("/api/products")
async def get_products():

    return {"data": connection.connect_database(), "status":200}
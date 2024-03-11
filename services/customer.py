from fastapi import HTTPException, status
from schema.customer import CustomerCreate, customers


class CustomerService:
    @staticmethod
    def check_existing_customer(customer: CustomerCreate):
        for cust in customers:
            if customer.username == cust.username:
                raise HTTPException(
                    status_code=409, detail="Customer already exists")


customer_service = CustomerService()
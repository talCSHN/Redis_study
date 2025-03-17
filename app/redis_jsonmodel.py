import datetime

from redis_om import (
    EmbeddedJsonModel,
    JsonModel,
    Field,
    Migrator
)
from typing import Optional

class Address(EmbeddedJsonModel):
    address_line_1: str
    address_line_2: Optional[str]
    city: str = Field(index=True)
    state: str = Field(index=True)
    country: str
    postal_code: str = Field(index=True)
 
 
class Customer(JsonModel):
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    email: str = Field(index=True)
    join_date: datetime.date
    age: int = Field(index=True)
    bio: Optional[str] = Field(index=True, full_text_search=True,
                               default="")
 
    # Creates an embedded model.
    address: Address


customer = Customer(
            first_name="Andrew",
            last_name="Brookins",
            email="Not an email address!",
            join_date=datetime.date.today(),
            age=38,
            bio="Python developer, works at Redis, Inc.",
            address=Address(
                address_line_1="123 Main St",
                address_line_2="Apt 4",
                city="Metropolis",
                state="NY",
                country="USA",
                postal_code="12345"
            ))

customer.save()

Migrator().run()

# Find all customers who live in Metropolis
# Query object
query_results = Customer.find(
                    Customer.address.city == "Metropolis",
                    Customer.address.state == "NY")

# To fetch and print all matching records
for customer in query_results:
    print(customer.first_name, customer.last_name)

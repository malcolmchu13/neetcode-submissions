-- Write your query below
Select name from customers 
WHERE NOT EXISTS (
    select id from orders 
    where customers.id = orders.customer_id 
)

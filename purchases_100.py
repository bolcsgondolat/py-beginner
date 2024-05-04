def purchases_100(sales):
    count = 0
    for customer_purchase in sales:
        total_purchase = sum(customer_purchase)
        if total_purchase >= 100:
            count += 1
    return count
sales = [[2.75], [50.0, 50.0], [150.46, 200.12, 111.30]]
purchases_100(sales)

# RUN THIS CELL TO TEST YOUR FUNCTION
import ada_c2_labs as lab
sales1 = lab.sales_data_generator(n_customers=10, seed=1)   # SHOULD OUTPUT:
print('Test 1:', purchases_100(sales1))                     # 5

sales2 = lab.sales_data_generator(n_customers=150, seed=18)
print('Test 2:', purchases_100(sales2))                     # 46

sales3 = lab.sales_data_generator(n_customers=1275, seed=42)
print('Test 3:', purchases_100(sales3))                     # 470
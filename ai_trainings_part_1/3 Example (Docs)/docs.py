
class StatsService:

    def get_monthly_sales(self, orders, year, month):
        total = 0.0
        for order in orders:
            if order['year'] == year and order['month'] == month:
                total += order['total_price']
        return total

    def get_top_customers(self, orders, limit=3):
        spending = {}
        for order in orders:
            customer_id = order['customer_id']
            spending[customer_id] = spending.get(customer_id, 0) + order['total_price']

        sorted_by_spending = sorted(spending.items(), key=lambda x: x[1], reverse=True)
        return [customer_id for customer_id, total_spent in sorted_by_spending[:limit]]


if __name__ == "__main__":
    sample_orders = [
        {'year': 2023, 'month': 7, 'customer_id': 101, 'total_price': 250.0},
        {'year': 2023, 'month': 7, 'customer_id': 102, 'total_price': 150.0},
        {'year': 2023, 'month': 7, 'customer_id': 101, 'total_price': 300.0},
        {'year': 2023, 'month': 8, 'customer_id': 103, 'total_price': 200.0},
    ]
    stats = StatsService()
    print(f"Total sales for July 2023: ${stats.get_monthly_sales(sample_orders, 2023, 7):.2f}")
    print(f"Top customers: {stats.get_top_customers(sample_orders)}")

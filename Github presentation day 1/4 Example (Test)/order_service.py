import pprint

class OrderService:

    def create_order(self, products, quantities, coupon_code=None):
        order = {
            'items': [],
            'total_price': 0.0
        }

        for product in products:
            product_id = product['id']
            qty = quantities.get(product_id, 1)
            line_price = product['price'] * qty
            order['items'].append({
                'product_id': product_id,
                'price': product['price'],
                'qty': qty,
                'line_price': line_price
            })
            order['total_price'] += line_price

        if coupon_code == 'SUMMER2025':
            order['total_price'] *= 0.8

        return order

if __name__ == "__main__":
    sample_products = [{'id': 1, 'price': 100.0}, {'id': 2, 'price': 200.0}]
    sample_quantities = {1: 2, 2: 1}
    service = OrderService()
    pp = pprint.PrettyPrinter()
    pp.pprint(service.create_order(sample_products, sample_quantities, coupon_code='SUMMER2025'))

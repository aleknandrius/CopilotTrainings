def sort_products(products, sort_order=None, category=None):
    if category:
        filtered = []
        for p in products:
            if p['category'] == category:
                filtered.append(p)

        if sort_order == 'asc':
            sorted_list = sorted(filtered, key=lambda x: x['price'])
        elif sort_order == 'desc':
            sorted_list = sorted(filtered, key=lambda x: x['price'], reverse=True)
        else:
            sorted_list = filtered
    else:
        if sort_order == 'asc':
            sorted_list = sorted(products, key=lambda x: x['price'])
        elif sort_order == 'desc':
            sorted_list = sorted(products, key=lambda x: x['price'], reverse=True)
        else:
            sorted_list = products

    return sorted_list

if __name__ == "__main__":
    sample_products = [
        {'name': 'Phone', 'category': 'Electronics', 'price': 599},
        {'name': 'Laptop', 'category': 'Electronics', 'price': 1299},
        {'name': 'Table', 'category': 'Furniture', 'price': 199},
    ]
    sorted_products = sort_products(sample_products, sort_order='desc', category='Electronics')
    for product in sorted_products:
        print(f"Name: {product['name']}, Category: {product['category']}, Price: ${product['price']}")

def build_hierarchy(categories):

    indexed = {}
    for c in categories:
        indexed[c['id']] = {
            'category': c,
            'children': []
        }

    root = []
    for c_id, data in indexed.items():
        parent_id = data['category']['parent_id']
        if parent_id and parent_id in indexed:
            indexed[parent_id]['children'].append(data)
        else:
            root.append(data)

    return root

if __name__ == "__main__":
    sample_categories = [
        {'id': 1, 'name': 'Electronics', 'parent_id': None},
        {'id': 2, 'name': 'Phones', 'parent_id': 1},
        {'id': 3, 'name': 'Laptops', 'parent_id': 1},
        {'id': 4, 'name': 'Gaming Laptops', 'parent_id': 3},
    ]
    hierarchy = build_hierarchy(sample_categories)
    print(hierarchy)

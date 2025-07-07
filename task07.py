cart = {
    'non': {'price': 3000, 'quantity': 2},
    'sut': {'price': 8000, 'quantity': 1},
    'olma': {'price': 5000, 'quantity': 5}
}

total = sum(map(lambda item: item['price'] * item['quantity'], cart.values()))

print(f"Umumiy narx: {total} so'm")

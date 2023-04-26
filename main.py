def main():
    items = [
        {'name': 'Apples', 'type': 'Wic Eligible food', 'price': 0.5},
        {'name': 'Shirt', 'type': 'Clothing', 'price': 20.0},
        {'name': 'Book', 'type': 'everything else', 'price': 10.0},
    ]
    state = 'NJ'
    total = calculate_total(state, items)
    print(f'Total for {state}: {total:.2f}')


def calculate_total(state: str, items: list) -> float:
    """
    Calculates the total amount to be charged to the customer at checkout.
    :param state: The customer's state of residence. Must be one of 'NJ', 'DE', or 'PA'.
    :param items: A list of dictionaries containing the items to be purchased. Each dictionary must contain the
                  following keys: 'name' (string), 'type' (string), and 'price' (float).
    :return: The total amount to be charged, including sales tax.
    """
    if state not in ['NJ', 'DE', 'PA']:
        raise ValueError('Invalid state')

    tax_exempt_types = ['Wic Eligible food']
    taxable_types = ['Clothing', 'everything else']
    taxable_name_substrings = ['fur']

    subtotal = sum(item['price'] for item in items)

    if any(item['type'] in tax_exempt_types for item in items):
        sales_tax = 0
    elif any(item['type'] == 'Clothing' and all(
            substring not in item['name'].lower() for substring in taxable_name_substrings) for item in items):
        if state == 'PA':
            sales_tax = 0
        else:
            sales_tax = 0.066 * subtotal
    else:
        if state == 'PA':
            sales_tax = 0.06 * subtotal
        else:
            sales_tax = 0.066 * subtotal

    total = subtotal + sales_tax

    return total


if __name__ == '__main__':
    main()

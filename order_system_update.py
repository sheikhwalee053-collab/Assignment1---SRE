STUDENT_RATE = 0.10
STAFF_RATE = 0.05

DELIVERY_CHARGES = {
    "express": 250,
    "standard": 100,
}

CUSTOMER_DISCOUNTS = {
    "student": STUDENT_RATE,
    "staff": STAFF_RATE,
}


def check_order_items(items):
    for product in items:
        if product["price"] < 0:
            raise ValueError(
                f"Price cannot be negative: {product['name']}"
            )

        if product["qty"] < 0:
            raise ValueError(
                f"Quantity cannot be negative: {product['name']}"
            )


def get_items_cost(items):
    cost = 0

    for product in items:
        cost += product["price"] * product["qty"]

    return cost


def get_customer_savings(cost, customer_type):
    discount_rate = CUSTOMER_DISCOUNTS.get(customer_type, 0)
    return cost * discount_rate


def get_shipping_cost(delivery):
    return DELIVERY_CHARGES.get(delivery, 0)


def order_total(items, customer_type, delivery):
    check_order_items(items)

    items_cost = get_items_cost(items)
    savings = get_customer_savings(items_cost, customer_type)
    shipping_cost = get_shipping_cost(delivery)

    final_amount = items_cost - savings + shipping_cost

    return round(final_amount, 2)


def print_receipt(items, customer_type, delivery):
    final_amount = order_total(items, customer_type, delivery)

    receipt_lines = [
        "========== ORDER RECEIPT =========="
    ]

    for product in items:
        quantity = product["qty"]
        name = product["name"]
        price = product["price"]
        item_cost = price * quantity

        receipt_lines.append(
            f"{quantity} x {name}: {item_cost:.2f}"
        )

    receipt_lines.extend([
        "-----------------------------------",
        f"Customer type : {customer_type}",
        f"Delivery method: {delivery}",
        f"Amount payable: {final_amount:.2f}",
        "===================================",
    ])

    return "\n".join(receipt_lines)


if __name__ == "__main__":
    order_items = [
        {
            "name": "Notebook",
            "category": "book",
            "price": 300,
            "qty": 2,
        },
        {
            "name": "USB Drive",
            "category": "electronics",
            "price": 800,
            "qty": 1,
        },
    ]

    receipt = print_receipt(
        order_items,
        customer_type="student",
        delivery="standard",
    )

    print(receipt)
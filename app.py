def calculate_discount(amount):
    """Calculate a discount based on the purchase amount."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount > 1000:
        return amount * 0.10
    elif amount > 500:
        return amount * 0.05
    else:
        return 0


def validate_username(username):
    """Validate that a username is not empty."""
    return bool(username and username.strip())


if __name__ == "__main__":
    print("DevOps Pipeline Practicum 10")
    print("Discount for ₹1500:", calculate_discount(1500))
    print("Username valid:", validate_username("admin"))
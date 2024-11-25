import random
import string


def generate_random_email(domain="example.com"):
    # Create a random string for the username
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))

    # Generate a random domain if needed
    domains = ["gmail.com", "yahoo.com", "hotmail.com", domain]
    selected_domain = random.choice(domains)

    # Combine the username and domain to form the email address
    email = f"{username}@{selected_domain}"
    return email


# Generate 5 random email addresses
for _ in range(5):
    print(generate_random_email())




def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(number)

    return average


def find_user(users, username):
    for user in users:
        if user["name"] == username:
            return user

    return None


users = [
    {"name": "Lakshay", "age": 20},
    {"name": "Akshat", "age": 21}
]

print(calculate_average([10, 20, 30]))
print(find_user(users, "Rahul"))
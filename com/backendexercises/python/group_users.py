def group_users_by_role(users):
    result = {}
    for user in users:
        role = user['role']
        name = user['name']
        result.setdefault(role, []).append(name)
    return result

users = [
    {'id': 1, 'name': 'Alice', 'role': 'admin'},
    {'id': 2, 'name': 'Bob', 'role': 'user'},
    {'id': 3, 'name': 'Charlie', 'role': 'admin'},
    {'id': 4, 'name': 'Daisy', 'role': 'user'},
    {'id': 5, 'name': 'Eve', 'role': 'moderator'},
]

print(group_users_by_role(users))

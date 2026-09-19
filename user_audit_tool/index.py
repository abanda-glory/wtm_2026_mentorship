# Raw user records: (User ID, Name, Role, is_active, Login_attempts)
users = [
    (101, "Alice", "admin", True, 1),
    (102, "Bob", "member", True, 4),
    (103, "Charlie", "editor", False, 0),
    (104, "Diana", "admin", False, 6),
    (105, "Evan", "member", True, 2),
    (106, "Fiona", "guest", True, 0),
]

active_users = 0
inactive_users = 0
security_alerts = 0

for user in users:
    if user[3] == True and user[2] == "admin":
        print(f'[GRANT]Full system access granted to {user[1]} (ID: {user[0]})')

    elif user[3] == True and user[2] == "member" or user[2] == "auditor":
        print(f'[GRANT]Standard access granted to {user[1]} (ID: {user[0]})')
    else:
        print(f'[DENIED]Account {user[1]} is inactive')

    # while True:
    if user[4] >= 5:
        print(f'[ALERT]Account {user[1]} is LOCKED due to excessive failed logins ({user[4]}) attempts')

        security_alerts  += 1

    if user[3] == True:
        active_users += 1
    else:
        inactive_users += 1

print(f"AUDIT SUMMARY REPORT\n{'='*20}")

print(f"Total Active Users Granted: {active_users}\nTotal Inactive Accounts: {inactive_users}\nTotal Security Alerts: {security_alerts}")
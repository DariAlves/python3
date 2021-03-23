# 1
for left in range(7):
    for right in range(left, 7):
        print(f"[{left}|{right}]", end=" ")
    print()

# 2
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


# 3
def validate_users(users):
    for user in users:
        def is_valid(u):
            if (len(u) > 3):
                return True
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users(["purplecat"])

# team_profile.py

team_name = "Code Warriors"

members = []

def add_member(name, role):
    members.append({"name": name, "role": role})

def show_team():
    print(f"Team: {team_name}")
    for member in members:
        print(f"  - {member['name']} ({member['role']})")

# Add founding members
add_member("Alice", "Backend Dev")
add_member("Bob", "Frontend Dev")

show_team()
"""
Author: Jorge Echavarria
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"          # str
preferred_weight_kg = 20.5           # float
highest_reps = 25                    # int
membership_active = True             # bool

# Step c: Create a dictionary named workout_stats
# Keys = friend names, Values = (yoga_minutes, running_minutes, weightlifting_minutes)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 30, 60),
    "Taylor": (20, 35, 15)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
# Add keys like "Alex_Total", "Jamie_Total", "Taylor_Total"
for friend, mins in list(workout_stats.items()):
    workout_stats[f"{friend}_Total"] = sum(mins)

# Step e: Create a 2D nested list called workout_list
friends = ["Alex", "Jamie", "Taylor"]
workout_list = [list(workout_stats[name]) for name in friends]

# Step f: Slice the workout_list
print("Yoga + Running for all friends:")
print([row[0:2] for row in workout_list])

print("Weightlifting for last two friends:")
print([row[2] for row in workout_list[-2:]])

# Step g: Check if any friend's total >= 120
for name in friends:
    if workout_stats[f"{name}_Total"] >= 120:
        print(f"Great job staying active, {name}!")

# Step h: User input to look up a friend
lookup = input("Enter a friend's name (Alex/Jamie/Taylor): ").strip().title()

if lookup in workout_stats:
    y, r, w = workout_stats[lookup]
    total = workout_stats[f"{lookup}_Total"]
    print(f"{lookup} -> Yoga: {y}, Running: {r}, Weightlifting: {w}, Total: {total}")
else:
    print(f"Friend {lookup} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {name: workout_stats[f"{name}_Total"] for name in friends}
highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"Highest total: {highest_friend} with {totals[highest_friend]} minutes")
print(f"Lowest total: {lowest_friend} with {totals[lowest_friend]} minutes")

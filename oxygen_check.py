# Oxygen Level Check
oxygen_percent = 85  # Mars pe kam hota hai

print(f"Oxygen Level: {oxygen_percent}%")

if oxygen_percent > 90:
  print("Status: perfect! ✅")
elif oxygen_percent > 50:
  print("Status: Low - Mark Needed! 😷")
else:
print("Status: DANGER! Emergency Oxygen ON! 🚨")

print("Life Support: ACTIVE")

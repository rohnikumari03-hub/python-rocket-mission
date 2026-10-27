# Alien Detector 
import random

planets = ["Mars", "Venus", "Jupiter", "Saturn", "Kepler-452b"]
status = ["No Life", "Alien Signal Found! 👽", "Water Found 💧", "Unknown Energy"]

print("Scanning Universe...")
for planet in planets:
  result = random.choice(status)
  print(f" {planet}: {result}")
  
ptint("\nMission: Search Complete!")


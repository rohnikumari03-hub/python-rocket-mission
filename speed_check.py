# Rocket Speed Calculator 
speed_kmh = 27000 # Rocket speed km/h
distance = 225000000 # To Mars

hours = distance / speed_kmh
days = hours / 24

print(f"Rocket Speed: {speed_kmh} km/h")
print(f"Time to reach Mars: {days:.1f} days")
print("Status: Hyperspace mode ON! ⚡")

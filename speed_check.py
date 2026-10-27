# Rocket Speed Calculator 
Speed_kmh = 27000 # Rocket speed km/h
distance = 225000000 # To Mars

hours = distance / speed_kmh
days = hours / 24

print(f"Rocket Speed: {speed_kmh} km/h")
print(f"Time to reach Mars: {days:.1f} days")

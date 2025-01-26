speed=int(input("Enter your speed in m/s:"))
speed_kmh= lambda speed: speed*3600/1000
print(f"Your speed is {speed_kmh(speed)} in km/h")
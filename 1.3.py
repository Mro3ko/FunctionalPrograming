def ms_to_kmh(ms):
    kh=ms*3600/1000
    return kh
speed=int(input("Enter your speed in m/s:"))
print(f"Your speed is {ms_to_kmh(speed)} in km/h")
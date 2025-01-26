avg_speed = lambda distance, hours, minutes: distance / (hours + minutes / 60)

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))


average = round(avg_speed(distance, hours, minutes),2)
print(f"Average speed: {average} km/h")

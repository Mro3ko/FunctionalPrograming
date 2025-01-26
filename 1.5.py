def avg_speed(distance, hours, minutes):
    total_time_hours = hours + (minutes / 60)
    average_speed = distance / total_time_hours
    return average_speed

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

average = round(avg_speed(distance, hours, minutes),2)
print(f"Average speed: {average} km/h")

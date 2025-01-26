speeds = [48, 47, 54, 50, 42, 68, 39, 46]

too_high = list(filter(lambda s: s > 50, speeds))

# Display the results
print(f"Recorded values: {speeds}")
print(f"Speed too high: {too_high}")
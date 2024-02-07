number_packages = int(input("How many packages do you want to send? "))

total_items = 0
total_weight = 0
largest_package_weight = 0

for i in range(number_packages):
    while True:
        weight = int(input(f"Enter the weight for package {i + 1} (from 1 to 10 kg): "))
        if 1 <= weight <= 10:
            total_items += 1
            total_weight += weight
            if weight > largest_package_weight:
                largest_package_weight = weight
            break
        else:
            print("The weight of the item must be between 1 and 10 kg.")

empty_kilograms = number_packages * 20 - total_weight
largest_empty_kilograms = largest_package_weight * number_packages - total_weight

print("Summary:")
print(f"Sent {number_packages} packages")
print(f"Total weight sent: {total_weight} kg")
print(f"Sum of empty kilograms: {empty_kilograms} kg")
print(f"The package with the most empty kilograms: {largest_empty_kilograms} kg")


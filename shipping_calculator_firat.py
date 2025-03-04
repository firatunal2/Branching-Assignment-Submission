# Package Express Shipping Calculator
# Programmer: Emily Rodriguez
# Date: 2024-03-15

# Display program header
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight input
cargo_weight = float(input("Please enter the package weight:\n"))

# Validate against maximum weight limit
if cargo_weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Request package dimensions
cargo_width = float(input("Please enter the package width:\n"))
cargo_height = float(input("Please enter the package height:\n"))
cargo_length = float(input("Please enter the package length:\n"))

# Calculate total package size
package_size = cargo_width + cargo_height + cargo_length

# Check if package exceeds size limit
if package_size > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Formula: (width * height * length * weight) / 100
transport_cost = (cargo_width * cargo_height * cargo_length * cargo_weight) / 100

# Display final shipping cost
print(f"Your estimated total for shipping this package is: ${transport_cost:.2f}")
print("Thank you!") 
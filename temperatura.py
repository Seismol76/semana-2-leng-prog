import hashlib

def convert_temperature(value, scale):
    # Validate the scale
    if scale not in ['C', 'F']:
        raise ValueError("The scale must be 'C' or 'F'")
    
    # Perform the conversion
    if scale == 'C':
        converted_temperature = (value * 9/5) + 32
        new_scale = 'F'
    else:
        converted_temperature = (value - 32) * 5/9
        new_scale = 'C'
    
    # Round to 2 decimal places
    converted_temperature = round(converted_temperature, 2)
    
    # Convert to string and generate hash
    temp_str = f"{converted_temperature:.2f}"
    hash_object = hashlib.sha256(temp_str.encode())
    hash_hex = hash_object.hexdigest()
    
    return converted_temperature, new_scale, hash_hex

# Function to get user input
def get_user_input():
    while True:
        try:
            value = float(input("Enter the temperature to convert: "))
            scale = input("Enter the scale (C or F): ").upper()
            if scale not in ['C', 'F']:
                raise ValueError("The scale must be 'C' or 'F'")
            return value, scale
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Example usage
try:
    value, scale = get_user_input()
    temp, new_scale, hash_value = convert_temperature(value, scale)
    print(f"{value}°{scale} is equal to {temp}°{new_scale}")
    print(f"SHA-256 Hash: {hash_value}")
    
except ValueError as e:
    print(f"Error: {e}")
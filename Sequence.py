import hashlib

def is_valid_reference_id(reference_id):
    """Check if the reference ID is valid (12 digits, alphanumeric)."""
    return reference_id.isalnum() and len(reference_id) == 12

def encrypt_reference_id(reference_id):
    """Encrypt the reference ID using hashlib (SHA-256)."""
    encrypted_id = hashlib.sha256(reference_id.encode()).hexdigest()
    return encrypted_id

if __name__ == "__main__":
    # Read the input Reference ID from the user
    reference_id = input("Enter the Reference ID: ")

    # Check for validity
    if is_valid_reference_id(reference_id):
        # Encrypt the Reference ID
        encrypted_reference_id = encrypt_reference_id(reference_id)

        # Print the encrypted Reference ID
        print("Encrypted Reference ID:", encrypted_reference_id)
    else:
        print("Invalid Reference ID. It should be 12 digits and alphanumeric.")

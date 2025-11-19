import base64

# Simple Base64 decode tool
# Usage:
# 1. Modify the 'encoded_string' variable,
# 2. Run the script to print the decoded result.

encoded_string = "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0="

if not encoded_string:
    print("Please insert Base64 text into 'encoded_string'.")
else:
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_text = decoded_bytes.decode('utf-8', errors='replace')
        print("Decoded text:\n", decoded_text)
    except Exception as e:
        print("Error decoding Base64:", e)

#JAfifah
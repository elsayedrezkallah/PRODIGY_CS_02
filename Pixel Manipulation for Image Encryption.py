import os

def process_image(path: str, key: int, mode: str) -> None:
    """Encrypt or decrypt an image file"""
    try:
        if mode == "e":
            print(f"Encrypting image at {path} with key {key}...")
        else:
            print(f"Decrypting image at {path} with key {key}...")
        
        with open(path, "rb+") as file:
            image = bytearray(file.read())
            for i, value in enumerate(image):
                image[i] = value ^ key
            file.seek(0)
            file.write(image)
        
        if mode == "e":
            print("Encryption successful!")
        else:
            print("Decryption successful!")
    except Exception as e:
        print(f"Error: {e}")

def main() -> None:
    """Main entry point of the program"""
    print("Welcome to the Image Encryption/Decryption Tool!")
    print("------------------------------------------------")
    
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
        if choice in ["e", "d"]:
            break
        else:
            print("Invalid choice. Please enter E to encrypt or D to decrypt.")
    
    mode = "e" if choice == "e" else "d"
    print(f"{mode.capitalize()} Mode")
    print("---------------")
    
    while True:
        path = input('Enter the path of the image: ')
        if os.path.exists(path) and os.path.isfile(path):
            break
        else:
            print("Invalid path. Please enter a valid file path.")
    
    while True:
        print("For the key, you have from 0 to 255")
        key = int(input('Enter the encryption/decryption key: '))
        if 0 <= key <= 255:
            break
        else:
            print("Invalid key. Please enter a key between 0 and 255.")
    
    process_image(path, key, mode)

if __name__ == "__main__":
    main()
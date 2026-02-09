import os

def check_files():
    print("Enviornment check")
    # Check the current working directory
    cwd = os.getcwd()
    print("Current directory in container:{}".format(cwd))

    # list files in current directory
    files = os.listdir(".")
    print("Files in current directory:{}".format(files))

    # Specifically check for your images folder
    if 'Fruit_Images' in files:
        fruit_count = len(os.listdir("Fruit_Images"))
        print("Fruit_Images folder found")
        print("Number of images: {}".format(fruit_count))
    else:
        print("Fruit_Images folder not found")

if __name__ == "__main__":
    check_files()
import os
from PIL import Image

def remove_corrupt_images(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                img = Image.open(file_path)  # Attempt to open the image
                img.verify()  # Verify if the image is valid
            except (IOError, SyntaxError) as e:
                print(f"Removing {file_path} due to error: {e}")
                os.remove(file_path)  # Remove the corrupt image

# Replace 'folder_path' with the path to your dataset folder containing images
folder_path = "C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\TrashBox_train_set"
remove_corrupt_images(folder_path)

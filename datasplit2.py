import os
import random
import shutil

# Define the root directory containing subfolders for each class
root_dir = 'C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\TrashBox_train_set'

# Define the directory where the split data will be saved
train_dir = 'C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\TrashBox_train_set\\train'
val_dir = 'C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\TrashBox_train_set\\val'

# Create train and val directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Define the percentage of data to be used for validation
val_split = 0.2  # 20% for validation

# Iterate through each class subfolder
for class_folder in os.listdir(root_dir):
    class_path = os.path.join(root_dir, class_folder)
    
    # Skip if it's not a directory
    if not os.path.isdir(class_path):
        continue
    
    # Create corresponding train and val directories for the class
    train_class_dir = os.path.join(train_dir, class_folder)
    val_class_dir = os.path.join(val_dir, class_folder)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)
    
    # List all files in the class directory
    files = os.listdir(class_path)
    
    # Shuffle the files randomly
    random.shuffle(files)
    
    # Calculate the number of validation samples
    num_val = int(len(files) * val_split)
    
    # Split the files into train and validation sets
    train_files = files[num_val:]
    val_files = files[:num_val]
    
    # Copy train files to train directory
    for file in train_files:
        src = os.path.join(class_path, file)
        dst = os.path.join(train_class_dir, file)  # Corrected: Include file name in destination path
        shutil.copy(src, dst)
    
    # Copy validation files to validation directory
    for file in val_files:
        src = os.path.join(class_path, file)
        dst = os.path.join(val_class_dir, file)  # Corrected: Include file name in destination path
        shutil.copy(src, dst)

print("Data split completed successfully.")

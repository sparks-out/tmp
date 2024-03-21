import os
import yaml

# Define the root directory containing train and val subfolders
root_dir = 'C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\TrashBox_train_set'

# Define the train and val directories
train_dir = os.path.join(root_dir, 'train')
val_dir = os.path.join(root_dir, 'val')

# Initialize lists to store train and val data
train_data = []
val_data = []

# Define function to collect file paths in each subfolder
def collect_files(folder_path):
    files = []
    for subdir, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.jpg'):
                files.append(os.path.join(subdir, filename))
    return files

# Iterate over class subfolders in train directory
for class_folder in os.listdir(train_dir):
    class_path = os.path.join(train_dir, class_folder)
    train_data.extend(collect_files(class_path))

# Iterate over class subfolders in val directory
for class_folder in os.listdir(val_dir):
    class_path = os.path.join(val_dir, class_folder)
    val_data.extend(collect_files(class_path))

# Define data dictionary
data = {'train': train_data, 'val': val_data}

# Write data dictionary to YAML file
with open('C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\data1.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)

print("Data YAML file created successfully.")

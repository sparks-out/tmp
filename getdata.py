import os
import yaml

# Define the path to the dataset folder
dataset_path = "C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\TrashBox_train_set"

# Initialize an empty dictionary to store class names and image paths
data_dict = {}

# Iterate over the subfolders
for class_name in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_path):
        image_paths = [os.path.join(class_name, img) for img in os.listdir(class_path) if img.endswith('.jpg')]
        data_dict[class_name] = image_paths

# Write the data dictionary to a YAML file
with open('C:\\Samyukta\\VIT\\Sem6\\projects\\tmp\\data.yaml', 'w') as file:
    yaml.dump(data_dict, file)

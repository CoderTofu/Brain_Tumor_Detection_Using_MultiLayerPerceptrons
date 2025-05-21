import os
import shutil
from sklearn.model_selection import train_test_split

dataset_path = '7272660'
output_base = 'Data/Liver'
train_dir = os.path.join(output_base, 'train')
test_dir = os.path.join(output_base, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

class_dirs = ['Benign', 'Malignant', 'Normal']

for class_name in class_dirs:
    image_folder = os.path.join(dataset_path, class_name, class_name, 'image')  # e.g., 7272660/Benign/Benign/image

    # Handle Normal class if it doesn't have nested structure
    if not os.path.exists(image_folder):
        image_folder = os.path.join(dataset_path, class_name, 'image')  # fallback

    if not os.path.exists(image_folder):
        print(f"Image folder not found for class {class_name}, skipping.")
        continue

    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

    if len(images) < 2:
        print(f"Skipping {class_name}: not enough images ({len(images)})")
        continue

    # Create output folders
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    train_imgs, test_imgs = train_test_split(images, test_size=0.2, random_state=42)

    for img in train_imgs:
        shutil.copy(os.path.join(image_folder, img), os.path.join(train_dir, class_name, img))
    for img in test_imgs:
        shutil.copy(os.path.join(image_folder, img), os.path.join(test_dir, class_name, img))

    print(f"{class_name}: {len(train_imgs)} train / {len(test_imgs)} test")

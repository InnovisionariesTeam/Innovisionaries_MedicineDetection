import streamlit as st
from PIL import Image
import pandas as pd
import os
import subprocess
import glob
import yaml
from datetime import datetime

# Load drug information
cfg_model_path = "/content/YOLOv5_EfficientNetLite_Streamlit_v0/runs/train/custom_yolov5s_results12/weights/best.pt"
data_yaml_path = "/content/YOLOv5_EfficientNetLite_Streamlit_v0/Medicine-Detection-9/data.yaml"
drug_info_df = pd.read_csv('/content/YOLOv5_EfficientNetLite_Streamlit_v0/Keterangan-Obat.csv', delimiter=';')

# Load class names from YAML
def load_class_names(yaml_path):
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
        return data['names']

class_names = load_class_names(data_yaml_path)

# Get the latest directory
def get_latest_directory(base_path):
    exp_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d)) and d.startswith('exp')]
    if not exp_dirs:
        return None
    return os.path.join(base_path, max(exp_dirs, key=lambda d: int(d[3:]) if d != 'exp' else 0))

# Run detection
def run_detection(image_path):
    output_base_dir = '/content/YOLOv5_EfficientNetLite_Streamlit_v0/runs/detect'
    subprocess.run([
        'python', '/content/YOLOv5_EfficientNetLite_Streamlit_v0/detect.py',
        '--weights', cfg_model_path,
        '--data', data_yaml_path,
        '--img', '512',
        '--conf', '0.4',
        '--source', image_path,
        '--save-txt',
    ])
    return get_latest_directory(output_base_dir)

# Read detected classes
def read_detected_classes(detected_image_dir, label_dir='labels'):
    detected_classes = set()
    label_path = os.path.join(detected_image_dir, label_dir)
    for file in os.listdir(label_path):
        if file.endswith('.txt'):
            with open(os.path.join(label_path, file), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    class_id = int(line.split()[0])
                    detected_classes.add(class_names[class_id])
    return detected_classes

# Display Drug Detected and Undetected Class
def display_detection_tables(detected_classes):
    st.subheader('Class Detection')

    detected_df = pd.DataFrame({
        'Available': list(detected_classes)
    })
    undetected_classes = set(class_names) - detected_classes
    undetected_df = pd.DataFrame({
        'Not Available': list(undetected_classes)
    })

    detected_df.index = pd.Index(range(1, len(detected_classes) + 1), name='No')
    undetected_df.index = pd.Index(range(1, len(undetected_classes) + 1), name='No')

    col1, col2 = st.columns(2)
    with col1:
        st.table(detected_df)
    with col2:
        st.table(undetected_df)

# Display drug information
def display_drug_information(detected_classes):
    for detected_class in detected_classes:
        drug_info = drug_info_df[drug_info_df['kelas'] == detected_class]
        if not drug_info.empty:
            drug = drug_info.to_dict('records')[0]
            st.write("-----")
            st.write(f"**Nama Obat:** {drug['nama']}")
            st.write(f"**Golongan Obat:** {drug['golongan']}")
            st.write("-----")
            st.write("**Deskripsi:**")
            st.write(drug['deskripsi'])
            st.write("-----")
            st.write("**Indikasi Umum:**")
            st.write(drug['indikasi_umum'])
            st.write("-----")
            st.write("**Komposisi:**")
            st.write(drug['komposisi'])
            st.write("-----")
            st.write("**Dosis:**")
            st.write(drug['dosis'])
            st.write("-----")
            st.write("**Aturan Pakai:**")
            st.write(drug['aturan_pakai'])
            st.write("-----")
            st.write("**Efek Samping:**")
            st.write(drug['efek_samping'])
            st.write("-----")
        else:
            st.write(f"No drug information found for {detected_class}")

# Image input and processing
def imageInput(src, display_tables=False, drug_info=False):
    image_file = st.file_uploader("Upload An Image", type=['png', 'jpeg', 'jpg'], key=src)
    col1, col2 = st.columns(2)
    if image_file is not None:
        img = Image.open(image_file)
        with col1:
            st.image(img, caption='Uploaded Image', use_column_width=True)
        ts = datetime.timestamp(datetime.now())
        upload_dir = '/content/YOLOv5_EfficientNetLite_Streamlit_v0/Medicine-Detection-9/test/images'
        os.makedirs(upload_dir, exist_ok=True)
        imgpath = os.path.join(upload_dir, str(ts) + image_file.name)
        with open(imgpath, mode="wb") as f:
            f.write(image_file.getbuffer())
        detected_image_dir = run_detection(imgpath)

        detected_images = []
        for extension in ['*.jpg', '*.jpeg', '*.png']:
            detected_images.extend(glob.glob(os.path.join(detected_image_dir, extension)))
        with col2:
            for detected_image_path in detected_images:
                img_ = Image.open(detected_image_path)
                st.image(img_, caption='Detected Image', use_column_width=True)

        detected_classes = read_detected_classes(detected_image_dir)
        
        # Display detection tables if requested (for Stock Management)
        if display_tables:
            display_detection_tables(detected_classes)

        # Display drug information if requested (for Drug Information)
        if drug_info:
            display_drug_information(detected_classes)

# Main function
def main():
    st.sidebar.title('⚙️ Options')
    datasrc = st.sidebar.radio("Select Options.", ['Stock Management', 'Drug Information'], key="datasrc")
    st.header('🤚 KNOW-STOCK: Optimalization Knowledge and Stock Management Medicine in Stall Local with Object Detection')
    st.subheader('👈🏽 Select options left-handed menu bar.')

    if datasrc == "Stock Management":
        imageInput(src=datasrc, display_tables=True)
    elif datasrc == "Drug Information":
        imageInput(src=datasrc, drug_info=True)

if __name__ == '__main__':
    main()

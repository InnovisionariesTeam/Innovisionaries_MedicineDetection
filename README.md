# KNOW-STOCK: Optimalization Knowledge and Stock Medicine in Stall Local with Object Detection

## Project Description
Dalam sehari-hari, terdapat beberapa masalah yang perlu diatasi untuk meningkatkan pengelolaan toko/warung khususnya warung kelontong dalam menjual obat-obatan dan memberikan pelayanan yang lebih baik kepada konsumen. Beberapa masalah yang perlu diperhatikan yaitu kurangnya pemahaman atau pengetahuan farmasi yang cukup dari pemilik toko/warung kelontong mengenai jenis-jenis obat yang mereka jual, serta masalah manajemen stok obat yang umum dipasaran dan wajib ada di setiap toko/warung kelontong. Oleh karena itu, kami menghadirkan "KNOW-STOCK: Optimalization Knowledge and Stock Medicine in Stall Local with Object Detection" untuk mendeteksi obat jenis apa saja yang dijual kepada konsumen, serta manajemen penyediaan stok obat pada setiap toko/warung kelontong.

## Contributor
| Full Name | Affiliation | Email | LinkedIn | Role |
| Adhi Nugroho | Universitas Sains Alqur an | adhinugroho209@gmail.com | --- | Team Member |
| Dewi Fatimah | Universitas Informatika Dan Bisnis Indonesia | dewifaa1234@gmail.com | Team Member |  |
| Gilbert O.K.D. Malau | Universitas Sumatera Utara | gilbertmalau476@gmail.com | ... | Team Lead |
| Haqqi Setiadjie | Universitas Sebelas Maret | haqqieky354@gmail.com | ... | Team Member |
| Marva Indrasari | Politeknik Indonusa Surakarta | marvaindrasari@gmail.com | ... | Team Member |
| Virgie Yunita Salsabil | Institut Teknologi Telkom Purwokerto | virgieyunitasalsa@gmail.com | ... | Team Member |
| Nicholas Dominic | Startup Campus, AI Track | nic.dominic@icloud.com | [link](https://linkedin.com/in/nicholas-dominic) | Supervisor |

## Setup
###YOLOv5 requirements
Usage: pip install -r requirements.txt
Source: https://github.com/ultralytics/yolov5/blob/master/requirements.txt

### Environment
| CPU | Intel Core i7-11700kf |
| GPU | Nvidia A100 (x1) |
| ROM | 1 TB HDD, 500 GB SSD |
| RAM | 32 GB |
| OS | Windows 10 Pro |

## Dataset
Describe your dataset information here. Provide a screenshot for some of your dataset samples (for example, if you're using CIFAR10 dataset, then show an image for each class).
- Link: https://universe.roboflow.com/innovisionaries-team-bbj4a/medicine-detection-d4vem

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Inform your model validation performances, as follows:
- For classification tasks, use **Precision and Recall**.
- For object detection tasks, use **Precision and Recall**. Additionaly, you may also use **Intersection over Union (IoU)**.
- For image retrieval tasks, use **Precision and Recall**.
- For optical character recognition (OCR) tasks, use **Word Error Rate (WER) and Character Error Rate (CER)**.
- For adversarial-based generative tasks, use **Peak Signal-to-Noise Ratio (PNSR)**. Additionally, for specific GAN tasks,
  - For single-image super resolution (SISR) tasks, use **Structural Similarity Index Measure (SSIM)**.
  - For conditional image-to-image translation tasks (e.g., Pix2Pix), use **Inception Score**.

Feel free to adjust the columns in the table below.

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | 1000 |  0.0001 | 32 | Adam | 0.093 | 88.34% | 84.15% | ... |
| vit_l_32 | 2500 | 0.00001 | 128 | SGD | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | 

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Insert an image regarding your training and evaluation performances (especially their losses). The aim is to assess whether your model is fit, overfit, or underfit.
 
### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.

### Deployment (Optional)
Describe and show how you deploy this project (e.g., using Streamlit or Flask), if any.

## Supporting Documents
### Presentation Deck
- Link: https://www.canva.com/design/DAF0PgrWxEU/b38SuRkCsrzBF6vVwmy_4w/edit?utm_content=DAF0PgrWxEU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

### Business Model Canvas
Provide a screenshot of your Business Model Canvas (BMC). Give some explanations, if necessary.

### Short Video
Provide a link to your short video, that should includes the project background and how it works.
- Link: https://drive.google.com/file/d/1ZKZfm0mlrGYXLSYV7N3vEamkxhseAApM/view?usp=drive_link
  
## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://...
- Link: https://...
- Link: https://...

## Additional Comments
Provide your team's additional comments or final remarks for this project. For example,
1. ...
2. ...
3. ...

## How to Cite
If you find this project useful, we'd grateful if you cite this repository:
```
@article{
...
}
```

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"YOUR PROJECT TITLE HERE"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.

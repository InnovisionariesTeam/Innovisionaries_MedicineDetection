# KNOW-STOCK: Optimalization Knowledge and Stock Medicine in Stall Local with Object Detection

## Project Description
Dalam sehari-hari, terdapat beberapa masalah yang perlu diatasi untuk meningkatkan pengelolaan toko/warung khususnya warung kelontong dalam menjual obat-obatan dan memberikan pelayanan yang lebih baik kepada konsumen. Beberapa masalah yang perlu diperhatikan yaitu kurangnya pemahaman atau pengetahuan farmasi yang cukup dari pemilik toko/warung kelontong mengenai jenis-jenis obat yang mereka jual, serta masalah manajemen stok obat yang umum dipasaran dan wajib ada di setiap toko/warung kelontong. Oleh karena itu, kami menghadirkan "KNOW-STOCK: Optimalization Knowledge and Stock Medicine in Stall Local with Object Detection" untuk mendeteksi obat jenis apa saja yang dijual kepada konsumen, serta manajemen penyediaan stok obat pada setiap toko/warung kelontong.

Penggunaan Computer Vision, khususnya Object Detection, terutama untuk mendeteksi dan mengidentifikasi obat-obatan. Hal ini sangat membantu dalam mengelola informasi tentang obat dan manajemen penyediaan stok. Teknologi yang bisa digunakan adalah YOLOv5 dari Ultralytics. YOLO (You Only Look Once) adalah sistem deteksi objek yang terkenal karena kecepatan dan akurasinya. Versi kelima, YOLOv5, membawa peningkatan yang signifikan dari versi sebelumnya. Untuk meningkatkan performa YOLOv5, Kami memodifikasi backbone modelnya dengan menggunakan EfficientNetLite. EfficientNetLite adalah varian dari EfficientNet yang dioptimalkan untuk perangkat dengan kemampuan komputasi yang lebih terbatas. Modifikasi ini akan meningkatkan efisiensi komputasi dan akurasi model tanpa memerlukan sumber daya komputasi yang besar. Integrasi YOLOv5 yang dimodifikasi dengan EfficientNetLite akan menghasilkan model yang tidak hanya cepat dan akurat dalam mendeteksi objek, tetapi juga efisien dalam penggunaan sumber daya.

## Contributor
| Full Name | Affiliation | Email | LinkedIn | Role |
| --- | --- | --- | --- | --- |
| Adhi Nugroho | Universitas Sains Alqur an | adhinugroho209@gmail.com | [link](...) | Team Member |
| Dewi Fatimah | Universitas Informatika Dan Bisnis Indonesia | dewifaa1234@gmail.com | [link](...) | Team Member |
| Gilbert O.K.D. Malau | Universitas Sumatera Utara | gilbertmalau476@gmail.com | [link](...) | Team Leader |
| Haqqi Setiadjie | Universitas Sebelas Maret | haqqieky354@gmail.com | [link](https://www.linkedin.com/in/haqqi-setiadjie-a6030a293/) | Team Member |
| Marva Indrasari | Politeknik Indonusa Surakarta | marvaindrasari@gmail.com | [link](...) | Team Member |
| Virgie Yunita Salsabil | Institut Teknologi Telkom Purwokerto | virgieyunitasalsa@gmail.com | [link](...) | Team Member |

## Setup
### YOLOv5 requirements
Usage: pip install -r requirements.txt, Source: https://github.com/ultralytics/yolov5/blob/master/requirements.txt

### Environment
#### Google Colaboratory Pro +
| Device | Name |
| --- | --- |
| CPU | Intel(R) Xeon(R) CPU @ 2.30GHz |
| GPU | Nvidia A100 (x1) |
| ROM | 166.8 GB |
| RAM | 83.5 GB |
| OS | Linux-5.4.104+-x86_64-with-Ubuntu-18.04-bionic |

## Dataset
Dataset terdiri dari gambar mengenai bungkus depan obat. Sumber dataset di dapat melalui pengumpulan gambar secara mandiri kemudian gambar di proses menggunakan roboflow untuk anotasi bounding box dan nama kelas, untuk kelasnya sendiri terdapat 14 kelas sebagai berikut:
- (1) bodrex_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Bodrex.jpg" width="250">

- (2) bodrexin_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Bondrexin.jpg" width="250">

- (3) decolgen_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Decolgen.jpg" width="250">
  
- (4) intunalf_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Intunalf.jpg" width="250">
  
- (5) inza_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Inza.jpg" width="250">
  
- (6) neo rheumacyl_ecer
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Neo_rheumacyl.jpg" width="250">
  
- (7) oskadon_biasa_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Oskadon.jpg" width="250">
  
- (8) oskadon_sp_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Oskadon_sp.jpg" width="250">
  
- (9) panadol extra_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Panadol_extend.jpg" width="250">
  
- (10) Panadol paracetamol_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Panadol_paracetamol.jpg" width="250">
  
- (11) Panadol_cold&flu_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Panadol_coldflu.jpg" width="250">
  
- (12) paramex_bungkus_luar
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Paramex.jpg" width="250">
  
- (13) procold_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Procold.jpg" width="250">
  
- (14) ultraflu_bungkus
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/Ultraflu.jpg" width="250">
  

Link: https://universe.roboflow.com/innovisionaries-team-bbj4a/medicine-detection-d4vem

## Results
### Model Performance
Seperti yang kami bilang di deskripsi project, tidak serta-merta menggunakan YOLOv5 Langsung tetapi melakukan modifikasi terutama pada bagian bacbonenya untuk meningkatkan performa YOLOv5 dan penyesuaian terhadap dataset yang terbatas. Disini kami memilih arsitektur yang menghasilkan weight yang kecil atau arsitektur yang ringan agar tidak merusak model. Terdapat 3 pilihan arsitektur untuk memodifikasi backbonenya sebagai berikut
- Custom YOLOv5 (Kami membuat arsitekturnya lebih lebar)
- MobileNetv3
- EfficientNetLite

Dari ketiga arsitektur tersebut sebagai bacbone kami akan mengambil salah satunya dengan cara membandingkan hasil performanya yang di training menggunakan hyperparameter, batchsize, dan crop size yang sama, hasilnya sebagai berikut:

| Arsitektur | Precision | Recall | mAP50 | mAP50-95 |
| --- | --- | --- | --- | --- |
| Custom YOLOv5 |	0.898 |	0.934 | 0.955 | 0.682
| MobileNetV3 | 0.922 |	0.916 | 0.949 |	0.702
| EfficientNetLite | 0.93 | 0.944 | 0.969 |	0.757

Dari Hasil di atas, EfficientNetLite memiliki nilai Precision, Recall, mAP50, dan mAP50-95 paling besar di antara arsitekturnya. Maka EfficientNetLite Kami pilih sebagai Backbone dari YOLOv5 sebagai model

Untuk Hasil Performa lengkap dari YOLOv5 dengan menggunakan Backbone EfficientNetLite sebagai berikut:
| Class	| Images-Instance	| Precision	| Recall	| mAP50	| mAP50-95 |
| --- | --- | --- | --- | --- | --- |
| ALL | 	74-104	| 0.93 | 0.944 |	0.969	| 0.757 |
| bodrex_bungkus | 74-8 | 0.971 |	1	| 0.995	| 0.832 |
| bodrexin_bungkus | 74-2 | 1 |	0.931 |	0.995 |	0.696 |
| decolgen_bungkus | 74-5 | 0.828 |	1 |	0.995 |	0.844 |
| intunalf_bungkus | 74-5 | 0.939 |	1 |	0.995 |	0.828 |
| inza_bungkus | 74-5 | 0.924 |	1 |	0.995 |	0.753 |
| neo rheumacyl_ecer | 74-14 |	1	| 0.797 |	0.99 |	0.617 |
| oskadon_biasa_bungkus | 74-7 | 0.909 |	0.857 |	0.858 |	0.619 |
| oskadon_sp_bungkus | 74-5 | 0.953 |	1 |	0.995 |	0.876 |
| panadol extra_bungkus | 74-7 | 0.953 |	1 |	0.995 |	0.91 |
| panadol paracetamol_bungkus | 74-12 |	0.902 |	0.917 |	0.909 |	0.623 |
| panadol_cold-Flu_bungkus | 74-7 | 0.813	| 0.857 |	0.883 |	0.549 |
| paramex_bungkus_luar | 74-10 | 1	| 0.944 |	0.995 |	0.933 |
| procold_bungkus | 74-11	| 0.953	| 0.909 |	0.971 |	0.773 |
| ultraflu_bungkus | 74-6	| 0.879 |	1 |	0.995 |	0.746 |

### Confusion Matrix

<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/confusion_matrix.png" width="750">

Dari Confusion Matrix di atas sudah banyak kelas yang sudah mencapai nilai 1.00 namun terdapat beberapa kelas yang masih di bawah 1.00, dengan nilai terendah adalah 0,86

### Grafik Training/Validation

<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/results.png" width="750">

Dari grafik Training/Validation di atas terlihat bahwa grafik loss train dan validation untuk object, box, dan kelas di setiap bertambanya epoch akan semakin berkurang mendekati nol yang mengartikan bahwa model sudah baik dan tidak over maupun under fitting, begitu juga dengan grafik metrik recall, pressisision dan mAPnya di setiap bertambahnya epoch akan bertambah mendekati 1.00

### Testing
Berikut adalah gambar-gambar testing menggunakan weight atau model dari YOLOv5 dengan menggunakan Backbone EfficientNetLite

<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/1.png" width="500">
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/2.png" width="500">
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/3.png" width="500">

### Deployment (Optional)
Aplikasi ini di-deploy menggunakan framework Streamlit, yang menyediakan antarmuka pengguna yang interaktif dan mudah digunakan. Aplikasi ini dirancang dari dataset yang telah didefinisikan dan menggunakan model YOLOv5 dan EfficientNetLite yang telah dikonfigurasi untuk deteksi obat, dengan data yang dikelola melalui Pandas dan YAML. Fokus utama aplikasi ini adalah terdapat 2 fungsi:

1. Manajemen Stok Obat
   Aplikasi memungkinkan pengguna untuk melacak dan mengelola stok obat. Fitur ini dirancang untuk membantu dalam mengorganisir dan memantau ketersediaan obat, dari deteksi aplikasi akan menampilkan tabel berupa obat yang tersedia dan yang tidak tersedia
   
3. Informasi Obat
   Selain manajemen stok, aplikasi juga memberikan informasi terperinci tentang berbagai obat. Ini termasuk keterangan obat, petunjuk penggunaan, dan informasi penting lainnya. Fitur ini sangat bermanfaat untuk pengguna yang mencari detail spesifik tentang obat, termasuk efek samping, komposisi, dan rekomendasi penggunaan.

## Supporting Documents
### Presentation Deck
- [link](https://www.canva.com/design/DAF0PgrWxEU/b38SuRkCsrzBF6vVwmy_4w/edit?utm_content=DAF0PgrWxEU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### Business Model Canvas
<img src="https://github.com/InnovisionariesTeam/Innovisionaries_MedicineDetection/blob/main/asset/BMC.png" width="750">

Tolong jelasin yaa gaiss

Jika ingin melihat BMC secara Lengkap dapat melalui [link](https://docs.google.com/document/d/1d4BoXntGU1w5FP2nKvSDpLWp9PDnaWoE/edit?usp=sharing&ouid=117040208822152496605&rtpof=true&sd=true) ini

### Short Video
- [link](https://drive.google.com/file/d/1ZKZfm0mlrGYXLSYV7N3vEamkxhseAApM/view?usp=drive_link)
  
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

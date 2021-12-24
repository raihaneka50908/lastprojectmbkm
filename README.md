# Smart Trash
## Penulis : Muhammad Raihan Ekaputra Idrisatria & Devaldi Caliesta Octadiani

[Project Brief](https://github.com/raihaneka50908/lastprojectmbkm/blob/main/Project%20Brief.pdf)

Untuk produk dalam bentuk perangkat keras masih dalam tahap pengembangan, namun kami lampirkan alat serta instruksi pengkabelan dari produk yang kami buat.

### Alat Yang Digunakan
- Sensor Ultrasonic HCSR04
- Raspberry Pi Seri 3b+
- Raspberry Pi Camera
- Resistor 470 Ohm
- Kabel Jumper 
- Motor Servo

### Bagian Pin Pada Alat Yang Digunakan
- Berikut adalah lokasi pin input dan output pada raspberry pi : 

![alt text](https://github.com/raihaneka50908/lastprojectmbkm/blob/main/gpio%20pin%20raspberry%20pi.png)

- Berikut adalah bagian pin pada motor servo

![alt text](https://github.com/raihaneka50908/lastprojectmbkm/blob/main/motor%20servo%20SG90.jpeg)

- Berikut adalah bagian pin pada sensor ultrasonik HCSR04 : 

![alt text](https://github.com/raihaneka50908/lastprojectmbkm/blob/main/sensor%20hcsr04.jpeg)

- Foto rangkaian alat pada produk : 

![alt text](https://github.com/raihaneka50908/lastprojectmbkm/blob/main/Foto%20rangkaian.jpeg)

### Pengkabelan pada Produk
#### Servo
- Red Wire (+5v) = GPIO 2
- Brown Wire = GPIO 6
- Orange Wire = GPIO 12

#### HCSR04 Ultrasonic Sensor
- VCC = GPIO 4
- Trig = GPIO 16 (Series with resistor) and GPIO 18 (Series with resistor)
- Echo = GPIO 18
- Gnd = GPIO 39

#### Simulasi Produk
1. Buka tautan berikut pada aplikasi [figma](https://github.com/raihaneka50908/lastprojectmbkm/blob/main/simulasi_smart_trash.fig)
2. Ikuti simulasi yang ada pada figma

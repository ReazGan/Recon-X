⚡ Recon-X - Web Keşif ve Tarama Aracı
Python ve modern web teknolojileri (HTML/CSS/JS) kullanılarak geliştirilmiş; bir web sitesinin keşif ve başlangıç seviyesi zafiyet taramasını yapan interaktif bir masaüstü uygulaması.

![image](https://github.com/user-attachments/assets/deafc795-62e5-4e69-ac2c-f1904da0b68c)

  

🇹🇷 Türkçe
🚀 Özellikler
* Çok Yönlü Tarama: Tek bir arayüzden Alt Alan Adı, Dizin/Dosya ve Teknoloji Tespiti taramalarını ayrı ayrı veya hep birlikte yapabilme.
* Alt Alan Adı Keşfi: Bir alan adının api, blog, dev gibi yaygın alt alan adlarını bularak saldırı yüzeyini ortaya çıkarır.
* Dizin ve Dosya Taraması: Web sunucularında unutulmuş /admin, /backup, .env gibi hassas dosya ve yönetim panellerini tespit eder.
* Teknoloji Tespiti: Hedef sitenin hangi teknolojilerle (Web Sunucusu, Backend Dili, CMS, Frontend Kütüphaneleri) inşa edildiğini analiz eder.
* Modern Arayüz: Geleneksel komut satırı araçlarının aksine, "hacker" temalı, modern, akıcı ve anlaşılır bir kullanıcı arayüzü sunar.
🛠️ Kullanılan Teknolojiler
* Backend: Python
* Arayüz (GUI): Eel (HTML, CSS, JavaScript)
* Ağ İstekleri: requests
* Paralel İşlemler: ThreadPoolExecutor
* Paketleme: PyInstaller
⚙️ Kurulum ve Çalıştırma
Gereksinimler
1. Python 3.8+: Python'un resmi sitesinden indirip kurun.
Adımlar
1. Bu depoyu klonlayın veya dosyaları indirin.
2. Terminali açıp projenin ana klasörüne gidin ve gerekli Python kütüphanelerini yükleyin.
pip install eel requests

3. Uygulamayı çalıştırmak için run.bat (veya run_silent.bat) dosyasına çift tıklayın.
📦 .EXE Haline Getirme
Projenin kaynak kodunu, bağımlılıkları olmadan herhangi bir Windows bilgisayarında çalışacak tek bir .exe dosyasına dönüştürmek için:
   1. PyInstaller'ı yükleyin: pip install pyinstaller
   2. Proje ana klasöründe bir terminal açın ve aşağıdaki komutu çalıştırın:
pyinstaller --noconfirm --onefile --windowed --add-data "web;web" app.py

      * --windowed komutu, arkada siyah komut penceresinin açılmasını engeller.
      3. Oluşturulan .exe dosyası dist klasörünün içinde yer alacaktır.
⚠️ Etik Kullanım Uyarısı
Bu araç, yalnızca eğitim ve yasal test amaçlı geliştirilmiştir. Bu aracı asla size ait olmayan veya test etme izninizin bulunmadığı sistemler üzerinde kullanmayın. İzin alınmadan yapılan tarama işlemleri yasa dışıdır ve siber suç teşkil edebilir.
🇬🇧 English
🚀 Features
      * Versatile Scanning: Perform Subdomain, Directory/File, and Technology Detection scans individually or all at once from a single interface.
      * Subdomain Discovery: Uncovers the attack surface by finding common subdomains like api, blog, dev of a domain.
      * Directory & File Brute-Forcing: Detects sensitive files and forgotten administration panels on web servers, such as /admin, /backup, .env.
      * Technology Detection: Analyzes and identifies the technologies a target site is built with (Web Server, Backend Language, CMS, Frontend Libraries).
      * Modern UI: Offers a modern, fluid, and intuitive user interface with a "hacker" theme, unlike traditional command-line tools.
🛠️ Tech Stack
      * Backend: Python
      * GUI: Eel (HTML, CSS, JavaScript)
      * HTTP Requests: requests
      * Concurrency: ThreadPoolExecutor
      * Packaging: PyInstaller
⚙️ Setup and Run
Prerequisites
      1. Python 3.8+: Download and install from python.org.
Steps
      1. Clone this repository or download the files.
      2. Open a terminal, navigate to the project's root directory, and install the required Python libraries:
pip install eel requests

      3. To run the application, double-click the run.bat (or run_silent.bat) file.
📦 Packaging into .EXE
To convert the source code into a single .exe file that runs on any Windows machine without dependencies:
         1. Install PyInstaller: pip install pyinstaller
         2. Open a terminal in the project's root directory and run the following command:
pyinstaller --noconfirm --onefile --windowed --add-data "web;web" app.py

            * The --windowed flag prevents the black console window from appearing in the background.
            3. The generated .exe file will be located in the dist folder.
⚠️ Ethical Use Disclaimer
This tool has been developed for educational and legal testing purposes only. NEVER use this tool on systems you do not own or have explicit permission to test. Unauthorized scanning is illegal and constitutes a cybercrime.

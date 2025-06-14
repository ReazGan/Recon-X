import eel
import requests
import threading
import re
import os
from concurrent.futures import ThreadPoolExecutor

# Arayüz dosyalarının bulunduğu klasörün yolunu belirliyoruz.
script_dir = os.path.dirname(os.path.realpath(__file__))
web_folder = os.path.join(script_dir, 'web')
eel.init(web_folder)

RECON_X_BANNER = """
██████╗ ███████╗ ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝ ██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║  ███╗██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║   ██║██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╔╝╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
"""

COMMON_SUBDOMAINS = [
    'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'ns2', 'test', 'dev',
    'admin', 'api', 'vpn', 'm', 'shop', 'blog', 'support', 'portal', 'owa', 'autodiscover',
    'cpanel', 'whm', 'webdisk', 'beta', 'staging', 'cdn', 'static', 'assets', 'files', 'images', 'docs'
]
COMMON_DIRECTORIES = [
    'admin', 'login', 'dashboard', 'admin-panel', 'panel', 'user', 'test', 'backup',
    'wp-admin', 'wp-login.php', 'admin.php', 'login.php', 'config.php.bak', '.env',
    'uploads', 'assets', 'css', 'js', 'images', 'vendor', 'api', 'v1', 'v2'
]

def check_subdomain(subdomain, domain):
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url, timeout=2)
        eel.add_to_log(f"[+] Alt Alan Adı: {url}", "success")()
    except requests.RequestException:
        pass

def check_directory(base_url, directory):
    url = f"{base_url}/{directory}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code in [200, 403, 301, 302]:
            eel.add_to_log(f"[+] Dizin/Dosya: {url} (Durum: {response.status_code})", "success")()
    except requests.RequestException:
        pass

@eel.expose
def detect_technologies(url):
    eel.add_to_log(f"[*] '{url}' için teknoloji analizi başlatıldı...")()
    try:
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Recon-X Scanner'})
        headers = response.headers
        content = response.text
        
        detected_techs = {}
        if 'Server' in headers: detected_techs['Web Sunucusu'] = headers['Server']
        if 'X-Powered-By' in headers: detected_techs['Backend Dili'] = headers['X-Powered-By']
        if 'wp-content' in content: detected_techs['CMS'] = 'WordPress'
        if re.search(r'react-?\.?js', content, re.I): detected_techs['Frontend'] = 'React'
            
        if not detected_techs:
            eel.add_to_log("[!] Belirgin bir teknoloji tespit edilemedi.")()
        else:
            eel.show_technologies(detected_techs)()
            
    except requests.RequestException as e:
        eel.add_to_log(f"[HATA] Hedefe ulaşılamadı: {e}", "error")()
    eel.scan_finished()()

def run_scans_in_background(target, scan_type):
    eel.add_to_log(RECON_X_BANNER)()
    eel.add_to_log(f"[*] Hedef: {target}")()
    
    base_url = target if target.startswith('http') else f"http://{target}"
    domain = target.replace('http://', '').replace('https://', '').split('/')[0]
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        if scan_type in ['subdomains', 'both']:
            eel.add_to_log(f"[*] Alt alan adı taraması başlatılıyor...")()
            executor.map(lambda sub: check_subdomain(sub, domain), COMMON_SUBDOMAINS)

        if scan_type in ['directories', 'both']:
            eel.add_to_log(f"[*] Dizin/dosya taraması başlatılıyor...")()
            executor.map(lambda directory: check_directory(base_url, directory), COMMON_DIRECTORIES)
    
    eel.scan_finished()()

@eel.expose
def start_scan(target, scan_type):
    if scan_type == 'tech':
        scan_thread = threading.Thread(target=detect_technologies, args=(target,))
    else:
        scan_thread = threading.Thread(target=run_scans_in_background, args=(target, scan_type))
    scan_thread.start()

if __name__ == "__main__":
    # DÜZELTME: port=0 parametresini ekleyerek Eel'in rastgele boş bir port bulmasını sağlıyoruz.
    eel.start('index.html', size=(900, 700), port=0)

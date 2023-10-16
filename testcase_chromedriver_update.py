import os
import re
import shutil
import time
import winreg
import zipfile
import requests

version_re = re.compile(r'^[1-9]\d*\.\d*\.\d*')  # Regular expression to match the first 4 version numbers

def getChromeVersion():
    """Query Chrome version from the registry."""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, _ = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]
    except WindowsError:
        return "1.1.1"

def get_chromedriver_version():
    chromedriver_path = os.path.join(os.getcwd(), os.pardir, "chromedriver")
    try:
        version_str = os.popen(f'{chromedriver_path} --version').read().split(' ')[1]
        return '.'.join(version_str.split('.')[:3])
    except Exception:
        return "0.0.0"

def get_chrome_zip_link(version):
    url = "https://googlechromelabs.github.io/chrome-for-testing/latest-patch-versions-per-build-with-downloads.json"
    data = requests.get(url).json()
    downloads = data.get('builds', {}).get(version, {}).get('downloads', {}).get('chromedriver', [])
    for download_info in downloads:
        download = download_info.get('url', '')
        if 'win32' in download and download.endswith('.zip'):
            return download
    return None

def download_and_extract_chromedriver(version):
    download_url = get_chrome_zip_link(version)
    if not download_url:
        print("No matching download link found for the specified version.")
        return

    with requests.get(download_url, stream=True) as file, open('chromedriver.zip', 'wb') as zip_file:
        for content in file.iter_content(chunk_size=1024):
            zip_file.write(content)

    time.sleep(5)
    parent_dir = os.path.join(os.getcwd(), os.pardir)
    with zipfile.ZipFile("chromedriver.zip", 'r') as zip_ref:
        folder_name = zip_ref.namelist()[0].split('/')[0]
        zip_ref.extractall()
        shutil.move(os.path.join(folder_name, "chromedriver.exe"), os.path.join(parent_dir, "chromedriver.exe"))
        shutil.rmtree(folder_name)
        os.remove("chromedriver.zip")

def checkChromeDriverUpdate():
    chrome_version = getChromeVersion()
    driver_version = get_chromedriver_version()
    if chrome_version == driver_version:
        print("Same Version, No need to update.")
        return

    print("Lower Version for chromedriver detected, updating...")
    try:
        download_and_extract_chromedriver(chrome_version)
        print("Chromedriver updated successfully!")
    except requests.exceptions.Timeout:
        print("Chromedriver download failed. Check the network connection and try again.")
    except Exception as e:
        print(f"Chromedriver download failed due to: {e}")

if __name__ == "__main__":
    checkChromeDriverUpdate()

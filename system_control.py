# import os
# import psutil
# import pyautogui
# import subprocess
# import shutil
# import webbrowser
# import time
# import speedtest
# import socket
# import ctypes
# from datetime import datetime

# # ✅ Open Application
# def open_application(app_name):
#     """Opens an application using its name."""
#     try:
#         subprocess.Popen(app_name)
#         return f"{app_name} opened."
#     except Exception as e:
#         return f"Error opening {app_name}: {str(e)}"

# # ✅ Close Application
# def close_application(app_name):
#     """Closes an application by its process name."""
#     os.system(f'taskkill /f /im {app_name}.exe')

# # ✅ Shutdown, Restart, Sleep, Lock
# def shutdown():
#     os.system('shutdown /s /t 0')

# def restart():
#     os.system('shutdown /r /t 0')

# def sleep():
#     os.system('rundll32.exe powrprof.dll,SetSuspendState Sleep')

# def lock():
#     os.system('rundll32.exe user32.dll,LockWorkStation')

# # ✅ Volume Control
# def adjust_volume(level):
#     pyautogui.press('volumeup' if level == 'up' else 'volumedown')

# def mute():
#     pyautogui.press('volumemute')

# # ✅ Screenshot
# def take_screenshot():
#     screenshot = pyautogui.screenshot()
#     screenshot.save(f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

# # ✅ Empty Recycle Bin
# def empty_recycle_bin():
#     os.system('PowerShell.exe -Command "Clear-RecycleBin -Force"')

# # ✅ File & Folder Operations
# def create_folder(name, path):
#     os.makedirs(os.path.join(path, name), exist_ok=True)

# def delete_folder(path):
#     shutil.rmtree(path)

# def open_folder(path):
#     os.startfile(path)

# def search_file(filename, directory):
#     for root, _, files in os.walk(directory):
#         if filename in files:
#             return os.path.join(root, filename)
#     return "File not found"

# def copy_file(src, dest):
#     shutil.copy(src, dest)

# def extract_zip(zip_path, extract_to):
#     shutil.unpack_archive(zip_path, extract_to)

# # ✅ Internet & Network Control
# def wifi_on_off(state):
#     os.system(f'netsh interface set interface "Wi-Fi" admin={"enable" if state else "disable"}')

# def check_speed():
#     st = speedtest.Speedtest()
#     return f"Download: {st.download()/1_000_000:.2f} Mbps, Upload: {st.upload()/1_000_000:.2f} Mbps"

# def get_ip():
#     return socket.gethostbyname(socket.gethostname())

# def flush_dns():
#     os.system('ipconfig /flushdns')

# # ✅ System Monitoring
# def battery_status():
#     battery = psutil.sensors_battery()
#     return f"Battery: {battery.percent}% {'Plugged In' if battery.power_plugged else 'Not Plugged In'}" if battery else "No battery detected"

# def system_uptime():
#     return time.time() - psutil.boot_time()

# def get_cpu_ram_usage():
#     return f"CPU: {psutil.cpu_percent()}%, RAM: {psutil.virtual_memory().percent}%"

# def list_running_processes():
#     return [proc.name() for proc in psutil.process_iter()]

# def kill_process(name):
#     for proc in psutil.process_iter():
#         if proc.name().lower() == name.lower():
#             proc.kill()
#             return f"{name} killed"
#     return "Process not found"

# # ✅ Media Controls
# def play_pause_media():
#     pyautogui.press('playpause')

# def next_track():
#     pyautogui.press('nexttrack')

# def previous_track():
#     pyautogui.press('prevtrack')

# # ✅ Browser & Web
# def open_website(url):
#     webbrowser.open(url)

# def google_search(query):
#     webbrowser.open(f"https://www.google.com/search?q={query}")

# # ✅ Task Manager & Modes
# def task_manager():
#     os.system("taskmgr")

# def eco_mode(jarvis_ui):
#     jarvis_ui.update_status("Eco mode activated.")
#     return "Eco mode activated."

# def gork_mode(jarvis_ui):
#     jarvis_ui.update_status("Gork mode activated.")
#     return "Gork mode activated."
# import os
# import shutil
# import psutil
# import pyautogui
# import subprocess
# import webbrowser
# import speedtest
# import socket
# import platform
# import ctypes
# import pyttsx3
# import requests
# import time
# import random
# import string
# import pyperclip
# from datetime import datetime

# def speak_text(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def shutdown_system():
#     os.system("shutdown /s /t 1")

# def restart_system():
#     os.system("shutdown /r /t 1")

# def sleep():
#     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# def lock_system():
#     ctypes.windll.user32.LockWorkStation()

# def get_weather(city):
#     api_key = "your_api_key"  # Replace with a valid OpenWeather API key
#     if api_key == "your_api_key":
#         return "API key missing. Please add a valid API key."
    
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
    
#     if data["cod"] != "404":
#         weather = data["main"]
#         return f"Temperature: {weather['temp']}°C, Humidity: {weather['humidity']}%"
#     return "City not found."

# def get_cpu_temperature():
#     try:
#         import wmi
#         sensors = wmi.WMI(namespace="root\WMI").MSAcpi_ThermalZoneTemperature()
#         return f"CPU Temperature: {sensors[0].CurrentTemperature / 10.0 - 273.15:.1f}°C"
#     except Exception:
#         return "Could not retrieve CPU temperature."

# def set_reminder(text, delay):
#     time.sleep(delay)
#     speak_text(f"Reminder: {text}")

# def open_application(app_name):
#     try:
#         subprocess.Popen(app_name)
#     except FileNotFoundError:
#         return f"Application '{app_name}' not found."

# def close_application(app_name):
#     os.system(f"taskkill /f /im {app_name}.exe")

# def list_running_processes():
#     return [proc.info for proc in psutil.process_iter(['pid', 'name'])]

# def kill_process(name):
#     for proc in psutil.process_iter():
#         if proc.name().lower() == name.lower():
#             proc.kill()
#             return "Process terminated."
#     return "Process not found."

# def adjust_volume(level):
#     os.system(f"nircmd.exe setsysvolume {level}")  # Ensure nircmd.exe is installed

# def toggle_mute():
#     os.system("nircmd.exe mutesysvolume 2")

# def play_pause_media():
#     pyautogui.press("playpause")

# def next_track():
#     pyautogui.press("nexttrack")

# def previous_track():
#     pyautogui.press("prevtrack")

# def create_folder(name, path):
#     os.makedirs(os.path.join(path, name), exist_ok=True)

# def delete_folder(path):
#     def on_rm_error(func, path, _):
#         os.chmod(path, 0o777)
#         func(path)
#     shutil.rmtree(path, onerror=on_rm_error)

# def open_folder(path):
#     os.startfile(path)

# def search_file(filename, directory):
#     for root, _, files in os.walk(directory):
#         if filename in files:
#             return os.path.join(root, filename)
#     return "File not found."

# def copy_file(src, dest):
#     shutil.copy(src, dest)

# def extract_zip(zip_path, extract_to):
#     shutil.unpack_archive(zip_path, extract_to)

# def delete_file(file_path):
#     os.remove(file_path)

# def open_file_explorer():
#     os.system("explorer")

# def battery_status():
#     battery = psutil.sensors_battery()
#     if battery:
#         return f"Battery: {battery.percent}%, Charging: {battery.power_plugged}"
#     return "Battery status unavailable."

# def system_uptime():
#     uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
#     return f"Uptime: {uptime}"

# def get_cpu_ram_usage():
#     return f"CPU: {psutil.cpu_percent()}%, RAM: {psutil.virtual_memory().percent}%"

# def check_storage():
#     return {p.device: psutil.disk_usage(p.mountpoint)._asdict() for p in psutil.disk_partitions()}

# def find_high_cpu_process():
#     process = max(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'])
#     return process.info

# def wifi_on_off(state):
#     os.system(f"netsh interface set interface name='Wi-Fi' admin={state}")

# def check_speed():
#     st = speedtest.Speedtest()
#     return f"Download: {st.download() / 1_000_000:.2f} Mbps, Upload: {st.upload() / 1_000_000:.2f} Mbps"

# def get_ip():
#     return socket.gethostbyname(socket.gethostname())

# def flush_dns():
#     os.system("ipconfig /flushdns")

# def take_screenshot():
#     screenshot = pyautogui.screenshot()
#     screenshot.save("screenshot.png")

# def clear_clipboard():
#     pyperclip.copy('')

# def open_website(url):
#     webbrowser.open(url)

# def google_search(query):
#     webbrowser.open(f"https://www.google.com/search?q={query}")

# def youtube_search(query):
#     webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

# def get_datetime():
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def change_wallpaper(image_path):
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# def write_in_notepad(text):
#     with open("notepad_temp.txt", "w") as file:
#         file.write(text)
#     os.system("notepad notepad_temp.txt")

# def generate_password(length):
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# def empty_recycle_bin():
#     os.system("rd /s /q C:\\$Recycle.Bin")

# def clear_downloads():
#     downloads_path = os.path.expanduser("~/Downloads")
#     for file in os.listdir(downloads_path):
#         file_path = os.path.join(downloads_path, file)
#         try:
#             if os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#             else:
#                 os.remove(file_path)
#         except PermissionError:
#             pass  # Handle files in use

# def list_installed_apps():
#     os.system("wmic product get name")

# def adjust_brightness(level):
#     os.system(f"nircmd.exe setbrightness {level}")  # Ensure nircmd.exe is installed

# def open_calculator():
#     os.system("calc")

# def system_info():
#     return platform.uname()

# import os
# import psutil
# import pyautogui
# import subprocess
# import shutil
# import webbrowser
# import time
# import speedtest
# import socket
# import ctypes
# from datetime import datetime

# # 1. Basic System Control
# def open_application(app_name):
#     os.system(f'start {app_name}')

# def close_application(app_name):
#     os.system(f'taskkill /f /im {app_name}.exe')

# def shutdown():
#     os.system('shutdown /s /t 0')

# def restart():
#     os.system('shutdown /r /t 0')

# def sleep():
#     os.system('rundll32.exe powrprof.dll,SetSuspendState Sleep')

# def lock():
#     os.system('rundll32.exe user32.dll,LockWorkStation')

# def adjust_volume(level):
#     pyautogui.press('volumeup' if level == 'up' else 'volumedown')

# def mute():
#     pyautogui.press('volumemute')

# def take_screenshot():
#     screenshot = pyautogui.screenshot()
#     screenshot.save(f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

# def empty_recycle_bin():
#     os.system('PowerShell.exe -Command "Clear-RecycleBin -Force"')

# # 2. File & Folder Operations
# def create_folder(name, path):
#     os.makedirs(os.path.join(path, name), exist_ok=True)

# def delete_folder(path):
#     shutil.rmtree(path)

# def open_folder(path):
#     os.startfile(path)

# def search_file(filename, directory):
#     for root, _, files in os.walk(directory):
#         if filename in files:
#             return os.path.join(root, filename)
#     return "File not found"

# def copy_file(src, dest):
#     shutil.copy(src, dest)

# def extract_zip(zip_path, extract_to):
#     shutil.unpack_archive(zip_path, extract_to)

# # 3. Internet & Network Control
# def wifi_on_off(state):
#     os.system(f'netsh interface set interface "Wi-Fi" admin={"enable" if state else "disable"}')

# def check_speed():
#     st = speedtest.Speedtest()
#     return f"Download: {st.download()/1_000_000:.2f} Mbps, Upload: {st.upload()/1_000_000:.2f} Mbps"

# def get_ip():
#     return socket.gethostbyname(socket.gethostname())

# def flush_dns():
#     os.system('ipconfig /flushdns')

# # 4. System Monitoring
# def battery_status():
#     battery = psutil.sensors_battery()
#     if battery is None:
#         return "No battery detected"
#     return f"Battery: {battery.percent}% {'Plugged In' if battery.power_plugged else 'Not Plugged In'}"

# def system_uptime():
#     return time.time() - psutil.boot_time()

# def get_cpu_ram_usage():
#     return f"CPU: {psutil.cpu_percent()}%, RAM: {psutil.virtual_memory().percent}%"

# def list_running_processes():
#     return [proc.name() for proc in psutil.process_iter()]

# def kill_process(name):
#     for proc in psutil.process_iter():
#         if proc.name().lower() == name.lower():
#             proc.kill()
#             return f"{name} killed"
#     return "Process not found"

# # 5. Media & Entertainment
# def play_pause_media():
#     pyautogui.press('playpause')

# def next_track():
#     pyautogui.press('nexttrack')

# def previous_track():
#     pyautogui.press('prevtrack')

# def set_wallpaper(image_path):
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# # 6. Browser & Web Automation
# def open_website(url):
#     webbrowser.open(url)

# def search(query):
#     webbrowser.open(f"https://www.google.com/search?q={query}")

# def open_browser_tab(url):
#     webbrowser.open_new_tab(url)

# # 7. Communication & Messaging
# def send_email(to, subject, body):
#     webbrowser.open(f"mailto:{to}?subject={subject}&body={body}")

# def open_whatsapp():
#     webbrowser.open('https://web.whatsapp.com')

# def open_telegram():
#     webbrowser.open('https://web.telegram.org')

# # 8. Security & Privacy
# def lock_system():
#     os.system('rundll32.exe user32.dll,LockWorkStation')

# def clear_browser_history():
#     os.system('RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255')

# def enable_disable_webcam(state):
#     action = "Enable-PnpDevice" if state else "Disable-PnpDevice"
#     os.system(f'powershell "Get-PnpDevice | Where-Object {{ $_.FriendlyName -like \'*camera*\' }} | ForEach-Object {{ $_ | {action} -Confirm:$false }}"')

# def enable_disable_microphone(state):
#     action = "Enable-PnpDevice" if state else "Disable-PnpDevice"
#     os.system(f'powershell "Get-PnpDevice | Where-Object {{ $_.FriendlyName -like \'*microphone*\' }} | ForEach-Object {{ $_ | {action} -Confirm:$false }}"')

# # 9. Developer & Coding Commands
# def open_vscode():
#     os.system('code')

# def run_python_script(script_path):
#     subprocess.run(['python', script_path])

# def check_git_status():
#     return subprocess.getoutput('git status')

# def install_package(package_name):
#     subprocess.run(['pip', 'install', package_name])

 

# import os
# import psutil
# import shutil
# import platform
# import webbrowser

# # 1. Get CPU Temperature (Linux example)
# def get_cpu_temperature():
#     try:
#         # Linux
#         temperature = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
#         return f"CPU Temperature: {int(temperature) / 1000} °C"
#     except Exception as e:
#         return f"Error fetching CPU temperature: {str(e)}"

# # 2. Get System Uptime
# def get_system_uptime():
#     try:
#         # Linux
#         uptime = os.popen("uptime -p").readline()
#         return f"System Uptime: {uptime}"

#         # Windows
#         # uptime = os.popen("systeminfo | find \"System Boot Time\"").readline()
#         # return f"System Uptime: {uptime}"
#     except Exception as e:
#         return f"Error fetching uptime: {str(e)}"

# # 3. Shutdown the Computer
# def shutdown_computer():
#     try:
#         # Windows
#         os.system("shutdown /s /f /t 1")  # /s: shutdown, /f: force, /t 1: delay of 1 second
#         # Linux
#         # os.system("sudo shutdown -h now")  # Requires sudo privileges
#         return "Shutting down your computer..."
#     except Exception as e:
#         return f"Error shutting down: {str(e)}"

# # 4. Open a Web Browser
# def open_browser(url="https://www.google.com"):
#     try:
#         webbrowser.open(url)
#         return f"Opening browser to {url}."
#     except Exception as e:
#         return f"Error opening browser: {str(e)}"

# # 5. List Files in a Directory
# def list_files(directory="."):
#     try:
#         files = os.listdir(directory)
#         return f"Files in {directory}: {files}"
#     except Exception as e:
#         return f"Error listing files: {str(e)}"

# # 6. Play Music (Windows)
# def play_music(file_path="C:\\path\\to\\your\\music\\file.mp3"):
#     try:
#         os.startfile(file_path)  # Windows-specific
#         return f"Playing music: {file_path}"
#     except Exception as e:
#         return f"Error playing music: {str(e)}"

# # 7. Check Disk Space
# def check_disk_space():
#     try:
#         total, used, free = shutil.disk_usage("/")
#         return f"Disk Space - Total: {total // (2**30)} GB, Used: {used // (2**30)} GB, Free: {free // (2**30)} GB"
#     except Exception as e:
#         return f"Error fetching disk space: {str(e)}"

# # 8. Get System Information
# def get_system_info():
#     try:
#         system_info = platform.uname()
#         return f"System Information: {system_info}"
#     except Exception as e:
#         return f"Error fetching system info: {str(e)}"

# # 9. Run a Command on the System (General Purpose)
# def run_system_command(command):
#     try:
#         result = os.popen(command).read()
#         return f"Command Output: {result}"
#     except Exception as e:
#         return f"Error running command: {str(e)}"

import os
import shutil
import time
import subprocess
import pyautogui
import speedtest
import psutil
import socket

def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def adjust_volume(action):
    if action == "up":
        pyautogui.press("volumeup")
    elif action == "down":
        pyautogui.press("volumedown")

def mute():
    pyautogui.press("volumemute")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot saved as screenshot.png")

def empty_recycle_bin():
    os.system("rd /s /q C:\\$Recycle.Bin")

def create_folder(folder_name, path):
    full_path = os.path.join(path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"Folder '{folder_name}' created at {path}")

def delete_folder(folder_path):
    shutil.rmtree(folder_path, ignore_errors=True)
    print(f"Folder '{folder_path}' deleted.")

def open_folder(folder_path):
    os.startfile(folder_path)

def open_application(app_name):
    try:
        subprocess.Popen(app_name)
        print(f"Opened application: {app_name}")
    except Exception as e:
        print(f"Error opening application: {e}")

def close_application(app_name):
    os.system(f"taskkill /f /im {app_name}.exe")

def search_file(file_name, search_path):
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            print(f"File found: {os.path.join(root, file_name)}")
            return os.path.join(root, file_name)
    print("File not found")
    return None

def wifi_on_off(state):
    if state:
        os.system("netsh interface set interface Wi-Fi enabled")
    else:
        os.system("netsh interface set interface Wi-Fi disabled")

def check_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    print(f"Download Speed: {st.download() / 1_000_000:.2f} Mbps")
    print(f"Upload Speed: {st.upload() / 1_000_000:.2f} Mbps")

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address: {ip_address}")

def flush_dns():
    os.system("ipconfig /flushdns")

def task_manager():
    subprocess.Popen("taskmgr")

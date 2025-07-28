import socket
import pyautogui

HOST = ''  # Listen on all interfaces
PORT = 9999

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f"[🔑 Receiver] Listening on port {PORT}...")

while True:
    conn, addr = s.accept()
    print(f"[👋 Connected] From {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            key = data.decode()
            print(f"[📥 Key received] {key}")
            pyautogui.press(key)  # Simulate key press
import sys
import socket
import threading

def scan(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Port {port} is open on {ip}")
    except:
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python portscanner.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]
    for port in range(1, 1025):
        thread = threading.Thread(target=scan, args=(target_ip, port))
        thread.start()

if __name__ == "__main__":
    main()
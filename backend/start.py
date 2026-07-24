"""Start the TravelPulse Flask dev server.

Usage:
    python start.py          # starts on port 5000
    python start.py 8080     # starts on port 8080
"""
import sys
import socket
import subprocess
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
HOST = "127.0.0.1"


def is_port_free(port, host=HOST):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) != 0


def kill_port(port):
    """Find and kill any process using the given port."""
    try:
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True, text=True, timeout=5,
        )
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 5 and f":{port}" in parts[1] and parts[3] == "LISTENING":
                pid = parts[4]
                print(f"Killing PID {pid} on port {port}...")
                subprocess.run(["taskkill", "/PID", pid, "/F"], capture_output=True, timeout=5)
                return True
    except Exception as e:
        print(f"Warning: could not kill port {port}: {e}")
    return False


def main():
    if not is_port_free(PORT):
        print(f"Port {PORT} is in use.")
        if kill_port(PORT):
            import time
            time.sleep(2)

    print(f"Starting TravelPulse on http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.\n")

    env = os.environ.copy()
    env["FLASK_DEBUG"] = "1"

    try:
        subprocess.run(
            [sys.executable, "-m", "flask", "run",
             "--host", HOST,
             "--port", str(PORT),
             "--debug"],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            env=env,
        )
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    main()

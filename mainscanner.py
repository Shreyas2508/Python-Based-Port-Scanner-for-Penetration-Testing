import socket
import sys
from datetime import datetime

def scan_target(target, ports):
    print(f"\n{'='*60}")
    print(f"Scanning: {target}")
    print(f"Time: {datetime.now()}")
    print(f"{'='*60}")

    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            print(f"[+] Port {port} is open     ({service})")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("No open ports found.")
    print(f"{'='*60}")

def parse_targets(target_input):
    return target_input.split(',')

def parse_ports(port_input):
    if '-' in port_input:
        start, end = port_input.split('-')
        return range(int(start), int(end) + 1)
    else:
        return [int(p) for p in port_input.split(',')]
      
if len(sys.argv) < 3:
    print("Usage: python3 scanner.py <target1,target2> <port_range>")
    print("Examples:")
    print("  python3 scanner.py google.com,github.com 1-1024")
    print("  python3 scanner.py 192.168.1.1 22,80,443")
    sys.exit(1)

targets = parse_targets(sys.argv[1])
ports = parse_ports(sys.argv[2])

print(f"Targets: {', '.join(targets)}")
print(f"Ports: {list(ports)}")
print(f"Started at: {datetime.now()}")

for target in targets:
    try:
        resolved_target = socket.gethostbyname(target)
        scan_target(resolved_target, ports)
    except socket.gaierror:
        print(f"[!] Could not resolve host: {target}")
        continue
    except KeyboardInterrupt:
        print("\n[!] Interrupted.")
        sys.exit(0)

print("\n[+] All scans complete.")

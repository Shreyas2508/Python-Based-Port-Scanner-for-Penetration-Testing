# Python Based Port Scanner for Penetration Testing

A lightweight, multi-target TCP port scanner built in Python. Supports scanning multiple hosts, custom port ranges, and service detection.

## Features

- Scan **single or multiple targets** (comma-separated)
- Specify **custom ports** (e.g., `22,80,443`) or **port ranges** (e.g., `1-1024`)
- **Service detection** (maps port numbers to service names)
- **Clean output** with per-target headings
- **Error handling** (invalid hosts don't crash the scan)

## Usage 

--> python3 scanner.py <targets> <ports>

## Examples

Scan multiple targets on common ports:

--> python3 scanner.py 192.168.1.1,192.168.1.5 22,80,443

Scan a target on a port range:

--> python3 scanner.py 192.168.1.1 1-1024

Single target, custom ports:

--> python3 scanner.py 192.168.1.1 21,22,80,443

## Future Improvements

□ Multithreading for faster scanning
□ Banner grabbing (extract service versions)
□ Output to file (CSV/JSON)
□ More CLI options using argparse

## Author 
Shreyas Shahi

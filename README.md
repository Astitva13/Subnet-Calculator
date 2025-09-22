# Subnet Calculator

A simple **Subnet Calculator** in Python to calculate network details for any IP address and CIDR.

## Features
- Calculates network address, broadcast address, subnet mask, CIDR, first/last usable IP, and number of hosts.
- Supports both **console-based** and **GUI-based** input.
- Validates IP/CIDR input.

## Files
- `console_calculator.py`: Command-line version.
- `gui_calculator.py`: Graphical version using Tkinter.
- `requirements.txt`: Python dependencies (none required for built-in modules).

## Usage

### Console
```bash
python console_calculator.py
```
Enter IP/CIDR when prompted, e.g., `192.168.1.10/24`.

### GUI
```bash
python gui_calculator.py
```
Enter IP/CIDR in the input box and click **Calculate**.

## License
MIT License

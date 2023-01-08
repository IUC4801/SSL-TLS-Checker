# SSL/TLS Checker

## About The Project

SSL/TLS Checker is a command-line tool for checking the SSL/TLS configuration of a server and identifying vulnerabilities.

## Features

- The SSL/TLS checker will check for vulnerabilities such as weak cipher suites, unsupported protocols, and invalid certificates.
- If any vulnerabilities are found, they will be listed in the output.
- It verifies that the certificate is valid for the specified hostname.
- It checks for the presence of TLS 1.2 and TLS 1.3 in the list of supported protocols.
- It checks for the presence of strong cipher suites.

## Requirements

- Python 3.6 or higher

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Python should be installed in the device.

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/IUC4801/SSL-TLS-Checker.git
   ```
   
2. After cloning this repository, install the following dependencies:
   ```bash
    pip install -r requirements.txt
   ```
## Usage

To check the SSL/TLS configuration of a server, run the following command:
   ```bash
    python ssl-tls-checker.py [hostname] [-p port]
   ```
   where `hostname` is the hostname of the server and `port` is the port number (default: 443).
   
## Example
To check the SSL/TLS configuration of google.com on port 443:
   ```bash
    python ssl-tls-checker.py google.com
   ```
To check the SSL/TLS configuration of google.com on port 8080:
   ```bash
    python ssl-tls-checker.py google.com -p 8080
   ```
   
## Machine configuration
- `OS:` Windows 10 64 bit
- `RAM:` 8 GB 
- `Processor:` 11th Gen Intel(R) Core(TM) i5

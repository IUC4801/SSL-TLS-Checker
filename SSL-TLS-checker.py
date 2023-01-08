import ssl
import socket
import argparse


def check_vulnerabilities(hostname, port):
    # Creating an SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.set_ciphers('HIGH')
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3

    # Creating a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wraping up the socket in an SSL/TLS context
    ssl_sock = context.wrap_socket(sock, server_hostname=hostname)

    ssl_sock.connect((hostname, port))

    # Checking for vulnerabilities
    vulnerabilities = []
    if context.check_hostname:
        try:
            ssl.match_hostname(ssl_sock.getpeercert(), hostname)
        except Exception as e:
            vulnerabilities.append(str(e))
    if context.verify_mode == ssl.CERT_NONE:
        vulnerabilities.append("certificate verification is disabled")
    if ssl_sock.cipher()[1] < 128:
        vulnerabilities.append("weak cipher suite is being used")

    # Checking for supported protocols
    protocols = ssl_sock.supported_protocols()
    if "TLSv1.2" not in protocols:
        vulnerabilities.append("TLS 1.2 is not supported")
    if "TLSv1.3" not in protocols:
        vulnerabilities.append("TLS 1.3 is not supported")

    ssl_sock.close()

    return vulnerabilities


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", help="the hostname of the website")
    parser.add_argument("-p", "--port", default=443, type=int,
                        help="the port number (default: 443)")
    args = parser.parse_args()

    # Checking for vulnerabilities
    vulnerabilities = check_vulnerabilities(args.hostname, args.port)

    if vulnerabilities:
        print("Vulnerabilities found:")
        for vulnerability in vulnerabilities:
            print(" - " + vulnerability)
    else:
        print("No vulnerabilities found")


if __name__ == "__main__":
    main()

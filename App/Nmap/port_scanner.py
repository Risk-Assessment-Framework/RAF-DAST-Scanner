import argparse  
import nmap  # user will hvae to download nmap on their local machine

# def scan_ports(target_ip, scan_args):
#     # create nmap PortScanner object
#     scanner = nmap.PortScanner()
#     target_ip = "127.0.0.1"
#     scan_args = "-sV -O -p 1-65535"
#     # perform the port scan on target_ip using the given scan arguments
#     scanner.scan(target_ip, arguments=scan_args)
#     port_data = []  # initialize an empty list to store the port scan results
#     for host in scanner.all_hosts():
#         for port in scanner[host]['tcp']:
#             # append the port information to port_data in the form of a dictionary
#             port_data.append({
#                 "port_number": port,
#                 "protocol": scanner[host]['tcp'][port]['name'],
#                 "state": scanner[host]['tcp'][port]['state'],
#                 "version": scanner[host]['tcp'][port]['version'],
#             })
#     return port_data  # return the list of port scan results
  
def scan_ports(target_ip="127.0.0.1", scan_args="-sV -O -p 1-65535"):
    scanner = nmap.PortScanner()
    scanner.scan(target_ip, arguments=scan_args)
    port_data = []
    for host in scanner.all_hosts():
        for port in scanner[host]['tcp']:
            port_data.append({
                "port_number": port,
                "protocol": scanner[host]['tcp'][port]['name'],
                "state": scanner[host]['tcp'][port]['state'],
                "version": scanner[host]['tcp'][port]['version'],
            })
    return port_data

if __name__ == '__main__':
    # define the command-line arguments using the argparse module
    parser = argparse.ArgumentParser(description='Perform a port scan on a target IP address')
    parser.add_argument('target_ip', help='The IP address of the target to scan')
    parser.add_argument('--scan-type', '-s', default='-sS', help='The type of scan to perform (default: -sS)')
    parser.add_argument('--ports', '-p', default='1-1000', help='The range of ports to scan (default: 1-65535)')
    args = parser.parse_args()  # parse the command-line arguments and store them in args

    try:
        # perform the port scan on the target IP address with the specified scan type and port range
        port_data = scan_ports(args.target_ip, f'{args.scan_type} -p {args.ports}')
        # print the port scan results in a formatted string
        for port in port_data:
            print(f"Port {port['port_number']}/{port['protocol']} is {port['state']} (version: {port['version']})")
    except nmap.PortScannerError as e:
        # handle errors related to nmap PortScanner object
        print(f"An error occurred while scanning ports: {e}")
    except KeyboardInterrupt:
        # handle keyboard interrupts (e.g. Ctrl+C)
        print("Port scanning interrupted by user")

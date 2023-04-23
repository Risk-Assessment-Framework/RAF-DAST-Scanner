import argparse  
import nmap  
import requests

CVE_API_URL = 'https://cve.circl.lu/api/cve/'

def scan_ports(target_ip="127.0.0.1", scan_args="-sV -O -p 1-65535"):
    # create nmap PortScanner object
    scanner = nmap.PortScanner()

    # perform the port scan on target_ip using the given scan arguments
    scanner.scan(target_ip, arguments=scan_args)

    # iterate through each host and port, and check for CVE vulnerabilities
    for host in scanner.all_hosts():
        for port in scanner[host]['tcp']:
            # get the port information
            port_num = port
            protocol = scanner[host]['tcp'][port]['name']
            state = scanner[host]['tcp'][port]['state']
            version = scanner[host]['tcp'][port]['version']
            service = scanner[host]['tcp'][port]['product']
            
            # check for CVE vulnerabilities associated with the service
            if service:
                cve_info = get_cve_info(service)
                if cve_info:
                    print(f"Vulnerability found on port {port_num}/{protocol}: {cve_info}")
            
            # print the port information
            print(f"Port {port_num}/{protocol} is {state} (version: {version})")
    
def get_cve_info(service):
    # send a request to the CVE API to retrieve information about the service
    url = f'{CVE_API_URL}/search/{service}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        cve_list = response.json()
        
        # return the first CVE description
        if cve_list:
            cve_id = cve_list[0]['id']
            cve_info = requests.get(f'{CVE_API_URL}/{cve_id}').json()
            return cve_info['cve']['description']['description_data'][0]['value']
        else:
            return None
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return None
        else:
            print(f"An error occurred: {e}")
            return None

if __name__ == '__main__':
    # define the command-line arguments using the argparse module
    parser = argparse.ArgumentParser(description='Perform a port scan on a target IP address')
    parser.add_argument('target_ip', help='The IP address of the target to scan')
    parser.add_argument('--scan-type', '-s', default='-sS', help='The type of scan to perform (default: -sS)')
    parser.add_argument('--ports', '-p', default='1-65535', help='The range of ports to scan (default: 1-65535)')
    args = parser.parse_args()  # parse the command-line arguments and store them in args

    try:
        # perform the port scan on the target IP address with the specified scan type and port range
        scan_ports(args.target_ip, f'{args.scan_type} -p {args.ports}')
        
    except nmap.PortScannerError as e:

        print(f"An error occurred while scanning ports: {e}")
        
    except KeyboardInterrupt:
      
        print("Port scanning interrupted by user")



# import argparse  
# import nmap  # user will hvae to download nmap on their local machine

# # def scan_ports(target_ip, scan_args):
# #     # create nmap PortScanner object
# #     scanner = nmap.PortScanner()
# #     target_ip = "127.0.0.1"
# #     scan_args = "-sV -O -p 1-65535"
# #     # perform the port scan on target_ip using the given scan arguments
# #     scanner.scan(target_ip, arguments=scan_args)
# #     port_data = []  # initialize an empty list to store the port scan results
# #     for host in scanner.all_hosts():
# #         for port in scanner[host]['tcp']:
# #             # append the port information to port_data in the form of a dictionary
# #             port_data.append({
# #                 "port_number": port,
# #                 "protocol": scanner[host]['tcp'][port]['name'],
# #                 "state": scanner[host]['tcp'][port]['state'],
# #                 "version": scanner[host]['tcp'][port]['version'],
# #             })
# #     return port_data  # return the list of port scan results
  
# def scan_ports(target_ip="127.0.0.1", scan_args="-sV -O -p 1-65535"):
#     scanner = nmap.PortScanner()
#     scanner.scan(target_ip, arguments=scan_args)
#     port_data = []
#     for host in scanner.all_hosts():
#         for port in scanner[host]['tcp']:
#             port_data.append({
#                 "port_number": port,
#                 "protocol": scanner[host]['tcp'][port]['name'],
#                 "state": scanner[host]['tcp'][port]['state'],
#                 "version": scanner[host]['tcp'][port]['version'],
#             })
#     return port_data

# if __name__ == '__main__':
#     # define the command-line arguments using the argparse module
#     parser = argparse.ArgumentParser(description='Perform a port scan on a target IP address')
#     parser.add_argument('target_ip', help='The IP address of the target to scan')
#     parser.add_argument('--scan-type', '-s', default='-sS', help='The type of scan to perform (default: -sS)')
#     parser.add_argument('--ports', '-p', default='1-1000', help='The range of ports to scan (default: 1-65535)')
#     args = parser.parse_args()  # parse the command-line arguments and store them in args

#     try:
#         # perform the port scan on the target IP address with the specified scan type and port range
#         port_data = scan_ports(args.target_ip, f'{args.scan_type} -p {args.ports}')
#         # print the port scan results in a formatted string
#         for port in port_data:
#             print(f"Port {port['port_number']}/{port['protocol']} is {port['state']} (version: {port['version']})")
#     except nmap.PortScannerError as e:
#         # handle errors related to nmap PortScanner object
#         print(f"An error occurred while scanning ports: {e}")
#     except KeyboardInterrupt:
#         # handle keyboard interrupts (e.g. Ctrl+C)
#         print("Port scanning interrupted by user")



import argparse
import agent_scanner

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Description of your program')

# Add command-line arguments
parser.add_argument('-c', '--credentials', help='File path for credentials.json')
parser.add_argument('-u', '--url', help='url for the target')
parser.add_argument('-s', '--sl', help='scan level (1-4)')

# Parse the command-line arguments
args = parser.parse_args()

zap=agent_scanner.connect_zap(agent_scanner.read_credentials_file(args.credentials))
print("Connected to ZAP")
agent_scanner.spider(zap,args.url)
print("Running scans...")
agent_scanner.report_generator(zap,args.sl,args.url)
print("Generating reports...")
agent_scanner.report_html(zap)
print("Done!")


#!/usr/bin/env python
import time
from zapv2 import ZAPv2


def spider_target(TARGET, API_KEY):
    zap = ZAPv2(apikey=API_KEY)
    print("Starting Spider for target " + TARGET)
    scan_id = zap.spider.scan(TARGET)
    while int(zap.spider.status(scan_id)) < 100:
        print("Spider Status completed: {} % ".format(
            zap.spider.status(scan_id)))
        time.sleep(1)

    print(map(str, zap.spider.results(scan_id)))
    return map(str, zap.spider.results(scan_id))


def passive_scan(TARGET, API_KEY):

    # Figure this one out

    zap = ZAPv2(apikey=API_KEY, proxies={
                'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})
    while int(zap.pscan.records_to_scan) > 0:
        print("Records to passive scan: " + str(zap.pscan.records_to_scan))
        time.sleep(2)

    print("Passive Scan Complete")

    print('Hosts: {}'.format(', '.join(zap.core.hosts)))
    print('Alerts: ')
    print(zap.core.alerts)
    return (zap.core.alerts)


def active_scan(TARGET, API_KEY):
    zap = ZAPv2(apikey=API_KEY, proxies={
                'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

    print("Active Scan for Target: {}".format(TARGET))
    scan_id = zap.ascan.scan(TARGET)

    while int(zap.ascan.status(scan_id)) < 100:
        print("Active scan completed: {} % ".format(zap.ascan.status(scan_id)))
        time.sleep(5)

    print("Active Scan Completed")
    print("Hosts: {}".format(', '.join(zap.core.hosts)))
    print('Alerts: ')
    print(zap.core.alerts)
    return (zap.core.alerts)


# The URL of the application to be tested
target = 'https://public-firing-range.appspot.com'
# Change to match the API key set in ZAP, or use None if the API key is disabled
apiKey = 'mk5f08maq9eh575sem'

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

print('Spidering target {}'.format(target))
# The scan returns a scan id to support concurrent scanning
scanID = zap.spider.scan(target)
while int(zap.spider.status(scanID)) < 100:
    # Poll the status until it completes
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)

print('Spider has completed!')
# Prints the URLs the spider has crawled
print('\n'.join(map(str, zap.spider.results(scanID))))
# If required post process the spider results

# TODO: Explore the Application more with Ajax Spider or Start scanning the application for vulnerabilities


# The URL of the application to be tested
target = 'https://appsec.asia/'
# # Change to match the API key set in ZAP, or use None if the API key is disabled
# apiKey = 'changeme'

# # By default ZAP API client will connect to port 8080
# zap = ZAPv2(apikey=apiKey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

print('Ajax Spider target {}'.format(target))
scanID = zap.ajaxSpider.scan(target)

timeout = time.time() + 60*2   # 2 minutes from now
# Loop until the ajax spider has finished or the timeout has exceeded
while zap.ajaxSpider.status == 'running':
    if time.time() > timeout:
        break
    print('Ajax Spider status' + zap.ajaxSpider.status)
    time.sleep(2)

print('Ajax Spider completed')
ajaxResults = zap.ajaxSpider.results(start=0, count=10)
print(ajaxResults)
# If required perform additional operations with the Ajax Spider results

# TODO: Start scanning the application to find vulnerabilities

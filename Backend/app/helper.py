from bs4 import BeautifulSoup
from pprint import pprint


def parse_zap_report(filename):
    with open(filename, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # find all vulnerabilities in the report
    vulnSummary = soup.find_all('table', {'class': ['summary']})
    vulnAlerts = soup.find_all('table', {'class': ['alerts']})
    vulnResults = soup.find_all('table', {'class': ['results']})

    # create a dictionary to store the vulnerabilities and their details
    result = []
    for data in vulnResults:
        headers = [th.text.strip() for th in data.find_all('th')]
        body = [td.text.strip() for td in data.find_all('td')]
        pprint(headers)
        type = headers[0]
        title = headers[1]
        # details = {body[i]: body[i+1] for i in range(0, len(body), 2)}

        # pprint(len(body))
        print(body)
        # result.append(data)
        break

    # for v in vulnerabilities:
    #     # print(v)
    #     break
    #     # extract the details of each vulnerability
    #     name = v.find('td', {'class': 'name'}).text
    #     risk = v.find('td', {'class': 'risk'}).text
    #     description = v.find('td', {'class': 'description'}).text
    #     solution = v.find('td', {'class': 'solution'}).text

    #     # add the vulnerability and its details to the dictionary
    #     result[name] = {
    #         'risk': risk,
    #         'description': description,
    #         'solution': solution
    #     }

    return result


def extract_zap_vulnerabilities(html_file_path):
    with open(html_file_path) as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Find the table containing vulnerability information
        table = soup.find('table', {'id': 'sitesTable'})

        # Extract the table headers
        headers = [th.text.strip() for th in table.find_all('th')]

        # Extract the vulnerability information
        vulnerabilities = []
        for tr in table.find_all('tr')[1:]:
            row = [td.text.strip() for td in tr.find_all('td')]
            vulnerability = dict(zip(headers, row))
            vulnerabilities.append(vulnerability)

        return vulnerabilities

from bs4 import BeautifulSoup


def parse_zap_report(filename):
    with open(filename, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # find all vulnerabilities in the report
    vulnerabilities = soup.find_all('tr', {'class': ['odd', 'even']})

    # create a dictionary to store the vulnerabilities and their details
    result = {}

    for v in vulnerabilities:
        # extract the details of each vulnerability
        name = v.find('td', {'class': 'name'}).text
        risk = v.find('td', {'class': 'risk'}).text
        description = v.find('td', {'class': 'description'}).text
        solution = v.find('td', {'class': 'solution'}).text

        # add the vulnerability and its details to the dictionary
        result[name] = {
            'risk': risk,
            'description': description,
            'solution': solution
        }

    return result

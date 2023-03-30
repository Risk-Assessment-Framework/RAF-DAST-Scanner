from flask import Flask, request
import requests

app = Flask(__name__)

# define a route for the web application
@app.route('/check_cve')
def check_cve():
    # retrieve the 'cve id' parameter from the request URL
    cve_id = request.args.get('cve_id')
    
    # validate the 'cve_id' parameter
    if not cve_id:
        return "Please provide a valid CVE ID"
    
    # send a request to the CVE API to retrieve information about the CVE
    url = f'https://cve.circl.lu/api/cve/{cve_id}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        cve_info = response.json()
        
        # return the first 10 words of the CVE description to the user
        return ' '.join(cve_info['cve']['description']['description_data'][0]['value'].split()[:10])
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return "CVE not found"
        else:
            return f"An error occurred: {e}"
        
# start the Flask app
if __name__ == "__main__":
    # TO DO: this api needs to be integrated with the main app
    app.run()

# get_json.py
# Author: Remy Brandriff
# Date: 9/21/18

# Gets & mines JSON file from GitHub API

# imports
import json
import requests
from requests.auth import HTTPBasicAuth

# Hardcoded global variables

# Headers required to get past GitHub's anti-script-requests policy
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}

# Username and password/OAuth token for Github
# Authorizes account to make request
USERNAME, PASS = "remyBrandriff", "7bccb55db1e17c6d263c11a1034f200eefab9ea9"

PROXIES = {}

# Specifies specific payload we want from the pull
# We want the first 50 requests, in order of when the request was created
PULL_PL = {'page': '1',
           'per_page': '50',
           'sort': 'created',
           'order': 'desc'}
PULL_NUM = "1"

# Indicates the API & repo we're working with
API_URL = "https://api.github.com/repos/"
REPO = "atom/atom"


# Downloads pull request from a specified repo, gets API page
def download_api(api_url, repo, pull_num, filename):

    pull_num = int(pull_num)

    for i in range(pull_num, pull_num+50):

        api_url_full = api_url + repo + "/issues/" + str(i) + "/comments"

        # Output to a JSON file we can use
        with open(filename, 'a', encoding='utf-8') as f:

            # Make request
            req = make_request(api_url_full, USERNAME, PASS, PULL_PL)

            # Convert to JSON file
            data =  req.json()

            # Dump JSON into file
            json.dump(data, f, sort_keys=True)

        # Close
        f.close()

    return req.status_code


# Make the request to the API
def make_request(api_url, username, passw, params):

    print(api_url)

    r = requests.get(api_url,
                     auth=HTTPBasicAuth(username, passw),
                     proxies=PROXIES,
                     headers=HEADERS,
                     params=params)
    return r


# Run the mining script
def mine():

    # Download JSON file
    request = download_api(API_URL, REPO, PULL_NUM, "test.json")

    # And double check
    print("\n Request Code (200 = Successful): ", request)

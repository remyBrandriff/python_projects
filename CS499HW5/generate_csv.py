# generate_csv.py
# Author: Remy Brandriff
# Date: 9/21/18

# Converts JSON file to CSV for data mining

# imports
import csv
import json
import os

# Hardcoded global variables

# The JSON file to convert, currently test file
JSON_FILE = "test.json"
CSV_FILE = "test.csv"

# The repo we're mining
REPO = "/atom/atom"


# Converts JSON file to a CSV file we can analyze
def generate_csv_file(json_file, repo):

    # Reformat the repo name so it's easier to deal with
    #repo_name = fix_repo_name(repo)

    # Open JSON file to parse it
    with (open(os.path.join(os.getcwd(), json_file), 'r')) as jsonfile:

        # Load it into the JSON interpreter so we can actually read it
        data = json.load(jsonfile)

        # Parse the info we actually want and get rid of the extra crap
        info = [data["user"]["login"],
                data["user"]["id"],
                data["created_at"],
                data["body"]]

        # Close file
        jsonfile.close()

    # Now create the CSV file we'll work with
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:

        # We have to define the writer that actually writes to the CSV file
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

        # Write the headers
        headers = "GITHUB_USERNAME," \
                  "GITHUB_ID," \
                  "DATE_CREATED," \
                  "COMMENTS"

        writer.writerow([headers])

        # Print out json file just to check
        print("\nJSON data in list form:", info)

        # Now write those contents to the CSV file
        string = ""
        for elem in info:
            string += (str(elem) + ",")
        writer.writerow([string])

        # And close the file
        csvfile.close()


# Turns '/repo/name' into 'repo-name' to make it easier
def fix_repo_name(repo):

    if str(repo).startswith("/"):
        return repo.split("/")[1] + "=" + repo.split("/")[2]

    return repo


# Run the conversion
def run_csv():
    generate_csv_file(JSON_FILE, REPO)

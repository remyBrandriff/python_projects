# csvMaker.py
# Source code by Stephen White, rewritten by Wyatt Evans for HW 5
# Date: 9/14/2018 (Updated 9/23/2018)
# Purpose: read a downloaded JSON file and produce a valid CSV

# Import the necessary libraries to create a CSV file
import csv
import json
import os
#import re

#JSON_FILE = "dataset.json"
#REPOSITORY = "/jekyll/jekyll"


# Take in a json file name and a repo that we would like to use
def produce_csv_file(json_file, csv_file):
    # Format the repo name so it will look appropriate in the CSV file (i.e. repo-name)

    # Initialize the variables used for output
    pull_num = 0
    
    # Open up the downloaded JSON file for reading so we can parse it
    with (open(os.path.join(os.getcwd(), json_file), 'r')) as pull_request_json_file:

        # Now that the file is open, load it in with a JSON interpreter so it can be read
        data = json.load(pull_request_json_file)

        # Create a CSV file that we will be writing in...
        with open(csv_file, "w+", newline="", encoding="utf-8") as csvfile:

            # Define the writer that will be responsible for writing to the CSV file
            writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='', escapechar='\\')

            # Write the title row of the CSV file
            descriptors = "REPO_NAME, PULL_ID,USER_NAME,USER_ID,STATE,CREATED_AT,CLOSED_AT"
            writer.writerow([descriptors])
    
            # Grab the information that is worth keeping from the json file
            for pull in data:
                
                #comm_per_pull.append(0)
                
                try:
                    # If there is no comment, then we won't put anything into the .csv file
                    if data[str(pull)]["message"] == "Not Found":
                        print("No Data")
                except:
                    pull_list = [data[str(pull)]["repo"]["name"], data[str(pull)]["id"], data[str(pull)]["user"]["login"],
                                  data[str(pull)]["user"]["id"], data[str(pull)]["state"],
                                  data[str(pull)]["created_at"], data[str(pull)]["closed_at"]]
                    
                    #print("\nJSON data in list form:", pull_list)
                
                    # Write the contents of pull list to the CSV file
                    string = ""
                    for element in pull_list:
                        string += (str(element) + ",")
                    writer.writerow([string])
                pull_num = pull_num + 1
        
        # Close the file
        csvfile.close()
                    
    # Close the file
    pull_request_json_file.close()

# Returns a repo name with no forward slashes (i.e. /repo/name -> repo-name)
def strip_slashes_from_repository_string(repo):
    if str(repo).startswith("/"):
        return repo.split("/")[1] + "-" + repo.split("/")[2]
    return repo


# Lets make a CSV file!
def run_csv_script():
    repolist = open("repo_list.txt", "r")
    # print(list.read())

    # for each repo in the list
    for line in repolist:
        repo = line.strip()
        repofile = repo.replace('/', '-')

        # Download the JSON file
        filename = "C:/Users/britt/OneDrive/Documents/school/CSVs/" + repofile + ".json"
        csvfile = filename.replace(".json", ".csv")
        produce_csv_file(filename, csvfile)


run_csv_script()

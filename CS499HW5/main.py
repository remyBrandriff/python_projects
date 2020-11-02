# main.py
# Author: Remy Brandriff
# Date: 9/22/18

# Main file for mining, storing, and parsing data from a GitHub API URL
# Based off demo code by Stephen White

import generate_csv as csvtool
import get_json as miningtool

# Run the program
miningtool.mine()
csvtool.run_csv()

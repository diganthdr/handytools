#This code helps to compare python code coverage reports generated from command
#'coverage report'

PREV_COVERAGE_REPORT_FILE = r"./coverage.previous" #specify full path
LATEST_COVERAGE_REPORT_FILE = r"./coverage.latest"





#STEPS
#---------------------------------
#1. Read previous report and latest into dict, {filename: coverage}
#2. Compare

#report output format below
'''
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
my/project/example.py                     3      3     0%
'''

import re
def convert_coverage_report_to_dict( coverage_filename ):
    out_map = {} #{filename: coverage}
    with open(coverage_filename, mode='r') as infile:
        #print("Filename: ", coverage_filename)
        for line in infile.readlines():
            if '.py' in line: #only py files
                line = re.sub(' +', ' ',line ) #only spaces are handled here. reports have only spaces
                tmp_list = line.split()
                filename = tmp_list[0]
                coverage = tmp_list[3].replace("%",'')
                out_map[filename]  = coverage 
    return out_map
    #print(out_map)
            

def compare_coverage_maps(previous_map, latest_map):
    for fname, coverage in previous_map.items(): #Comaprision, for O(1) for each comparsion O(n)
        if fname in latest_map and int(latest_map[fname]) < int(previous_map[fname]):
            print("File: ", fname)
            print("Previous: ",previous_map[fname])
            print("Latest: ",latest_map[fname])
            return False
    print("Code coverage change satisfactory")
    return True

def compare():
    prev_coverage = convert_coverage_report_to_dict( PREV_COVERAGE_REPORT_FILE )
    latest_coverage = convert_coverage_report_to_dict( LATEST_COVERAGE_REPORT_FILE)
    return compare_coverage_maps(prev_coverage, latest_coverage)

if __name__ == "__main__":
    compare()

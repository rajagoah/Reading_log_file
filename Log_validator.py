import os
import sys
import configparser
import logging

# initialising logger
validator_Logger = logging.getLogger(__name__)
validator_Logger.setLevel(logging.INFO)
validator_Formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
validator_Streamhandler = logging.StreamHandler()
validator_Streamhandler.setFormatter(validator_Formatter)
validator_Logger.addHandler(validator_Streamhandler)

def list_files(path):
    #list all the files in the folder
    files = os.listdir(path)
    return files

def log_validator(path, files, exception_msg, exception_line_1, exception_line_2, exception_line_3, error_msg, fatal_msg, OutOfMemory_msg):
    for file in files:
        validator_Logger.info("***************************************************************************")
        validator_Logger.info(file)
        validator_Logger.info("***************************************************************************")

        #creating the input dir
        input = os.path.join(path,file )
        log_file = open(input, 'r')
        for line in log_file:
            #treat every line as a STRING
            if line.find(exception_msg) != -1:
                if line.find(exception_line_1) == -1:
                    if line.find(exception_line_2) == -1:
                        if line.find(exception_line_3) == -1:
                            print(line)
                            continue
            if line.find(error_msg) != -1:
                print(line)
                continue
            if line.find(fatal_msg) != -1:
                print(line)
                continue
            if line.find(OutOfMemory_msg) != -1:
                print(line)
                continue
            else:
                1
    return 0

def main():

    #reading config files
    validator_config = configparser.ConfigParser()
    validator_config.read('validator_config.conf')
    path = validator_config['COMMON']['path']
    exception_line_1 = validator_config['COMMON']['exception_line_1']
    exception_line_2 = validator_config['COMMON']['exception_line_2']
    exception_line_3 = validator_config['COMMON']['exception_line_3']
    error_msg = validator_config['COMMON']['error_msg']
    fatal_msg = validator_config['COMMON']['fatal_msg']
    OutOfMemory_msg = validator_config['COMMON']['OutOfMemory_msg']
    exception_msg = validator_config['COMMON']['exception_msg']

    # Listing the files in the director
    validator_Logger.info(" Reading the files in the directory")
    files = list_files(path)

    #performing the log valiadtion
    validator_Logger.info(" Beginning Log validation")
    status = log_validator(path, files, exception_msg, exception_line_1, exception_line_2, exception_line_3, error_msg, fatal_msg, OutOfMemory_msg)

    if status == 0:
        validator_Logger.info(" **************** NO ISSUES FOUND IN THE LOGS **************** ")

if __name__ == "__main__":
    main()
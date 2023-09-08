
"""
Purpose: Illustrate tuples, sets, and dictionaries in Python.

Here are some examples for tuples, sets, and dictionaries.

"""

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

def lab_tuples():
    # Create some tuples
    tuple_labdept = ("hematology", "chemistry", "urinalysis", "bloodbank", "microbiology")
    tuple_hemo_test = ("CBC", "HH", "Sed Rate", "diff", "retic")
    tuple_chemistry_test = ("troponin", "albumin", "total protein", "BNP", "TSH")

    logger.info(f"{tuple_chemistry_test = }")
    logger.info(f"{tuple_hemo_test = }")
    logger.info(f"{tuple_labdept = }")

    #tuple practice
    duplicate_tuple = tuple_labdept * 2

    logger.info(f"duplicate the tuple: {duplicate_tuple}")

    # Create two sets

def lab_sets():

    lab_tempsA = {4, 5, 6, 7, 8}
    lab_tempsB = {5, 6, 7, 8, 9}

    logger.info(f"lab_set = {lab_tempsA}")
    logger.info(f"lab_temps = {lab_tempsB}")
    
    #set union
    lab_union = lab_tempsA | lab_tempsB
    logger.info(f"union of two sets: {lab_union}")

    #set intersection
    lab_set_int = lab_tempsA & lab_tempsB
    logger.info(f"intersection of two sets: {lab_set_int}")

    #set difference
    lab_set_diff = lab_tempsA & lab_tempsB
    logger.info(f"difference of two sets: {lab_set_diff}")

#make to lists with key:value pairs and count from file
def lab_dictionaries():
    PatientA_dict = {"test": "hemoglobin", "result": 6, "status": "critical"}
    PatientB_dict = {"test": "hemoglobin", "result": 14, "status": "normal"}

    logger.info(f"PatientA_dict = {PatientA_dict}")
    logger.info(f"PatientB_dict = {PatientB_dict}")
    
    logger.info("") #spacing for asthetics

    #word cound in key value pairs
    with open("IntroToPython-master/datafun-03-datatypes/text_woodchuck.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info("--------------Key Value pairs and word cound of dictionary----------------")
    logger.info(f"Given text_simple.txt, the word_counts_dict = {word_counts_dict}")
    

    #dictionary comprehension
    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    # Spend most of your practice on comprehensions - they are
    # key to transforming data in Python.
    
    logger.info("") #spacing for asthetics
    logger.info("-------------------dictionary comprehension--------------------------------")
    logger.info(f"word comprehension result = {word_counts_dict2}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    lab_tuples()
    lab_sets()
    lab_dictionaries()
    
    show_log()
    
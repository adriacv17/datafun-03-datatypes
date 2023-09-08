"""
Project 3 String Lists
Adrian Vega
09/08/2023

"""

# imports first
import random

   
from util_datafun_logger import setup_logger

# Set up logging.................................

logger, logname = setup_logger(__file__)

# Create about five lists. I'll use listA, listB, etc,
# but yours should make sense for your domain. 

qc_result = ["pass", "fail", "invalid", "pass", "fail", "invalid"]

test_directory = ["CBC", "CMP", "BMP", "UA", "TOX"]

lab_departments = ["hematology", "chemistry", "urinalysis", "bloodbank", "microbiology"]

qc_frequency = ["daily", "weekly", "monthly", "quarterly", "biannualy", "yearly"]

shifts = ["nightshift", "dayshift", "midshift", "nightshift", "dayshift", "midshift"]

wetprep_results = ["clue cells", "no clue cells", "yeast", "no yeast", "trichomonas", "no trichomonas"]

urine_colors = ["red", "amber", "orange", "brown", "straw", "yellow", "clear"]

lab_reviewflags = ["critical", "delta", "fyi"]

# reusable functions next

# Task 4 ####################################################
# Use the built-in functions: len(), set(), and zip() 
# to combine 2 or more lists into tuples.

#combine two lists using zip
def combine_twolists_zip():
    uadept_tuple = tuple(zip(urine_colors, wetprep_results))
    logger.info(f"combined list into tuple: {uadept_tuple}")
    logger.info("-----------------------------------------------")#break for readability

#Making new list with set
def new_list_set():
    lst_new = tuple(set(wetprep_results))
    logger.info(f"new tuple using set(): {lst_new}")

#combine two lists using len
def combine_lists_len():
    using_len = len(wetprep_results)
    logger.info(f"lenth of list: {using_len}")
    qc_tuple = [(qc_result[i], qc_frequency[i]) for i in range (0, len(qc_result))]
    logger.info(f"using len to combine two lists into tuple: {qc_tuple}")

# Use random.choice() to pick a random value from one of your lists.
# Customize the sentence generator to create random sentences about your domain. 

def pick_randomvalue():
    rand_value = random.choice(lab_reviewflags)
    logger.info(f"print random word value: {rand_value}")

def create_random_sentence():
    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")

    # Create a random sentence
    # e.g. "The angry dog runs quickly."
    sentence = (
        f"The {random.choice(qc_frequency)} {random.choice(qc_result)} "
        f"{random.choice(lab_departments)} {random.choice(lab_reviewflags)}."
    )

    logger.info(f"Random sentence: {sentence}")

# Choose one of the text data files in the repo - or add another related your your domain.
# Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
# Sort the list. 
# Use len() to get the length display it to the console.
# How good is your list? 

def process_text_labwords():
    with open("IntroToPython-master/datafun-03-datatypes/text_labwords.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        list_words_sorted = sorted(list_words)
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words and sort
        word_ct = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"The sorted lis of words is: {list_words_sorted}")
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")






def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# call functions and execute code
# use if __name__ == "__main__":

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    combine_twolists_zip()
    new_list_set()
    combine_lists_len()
    pick_randomvalue()
    create_random_sentence()
    create_random_sentence()
    process_text_labwords()

    show_log()
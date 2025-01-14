"""
Project 3 Numeric Lists
Adrian Vega
09/08/2013

"""

# import some standard modules first - how many can you make use of?

import statistics as stats
import math


# TODO: import from local util_datafun_logger.py
#  
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions

# this list is a list of 20 values of patient results with a mix of normal range results
# and some critical results as well.

hemoglobin_values = [16, 17, 18, 16, 14, 15, 6, 7, 13, 12,
                     15, 16, 17, 16, 10, 4, 5, 6, 15, 15]

# list x and y made from validating a cooler where we have hours vs temperature 
# to see how long a back-up cooler can last

time_x = list(range(1, 11))

temp_y = [4, 4, 5, 5, 5, 6, 6, 7, 7, 8 ]


# TODO: define some custom functions


def lab_statistics():
    '''This function is used for illustrating descriptive statistics in the lab'''

    logger.info(f"hemoglobin_values: {hemoglobin_values}")

    # Descriptive: Averages and measures of central tendency
    # Use statistics module to get mean, median, mode
    # for a values list

    mean = stats.mean(hemoglobin_values)
    median = stats.median(hemoglobin_values)
    mode = stats.mode(hemoglobin_values)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = stats.stdev(hemoglobin_values)
    variance = stats.variance(hemoglobin_values)

    logger.info(f"stdev: {stdev:.2f}")
    logger.info(f"variance: {variance:.2f}")


def lab_correlation_and_prediction():
    '''This function illustrates correlation and prediction for numeric list'''
    logger.info(f"time_x list: {time_x}")
    logger.info(f"temp_y list: {temp_y}")

    # Use to lists of equal size and using statistics module 
    # calculate correlation between two list
    correlationxy = stats.correlation(time_x, temp_y)
    logger.info(f"correlation between x and y: {correlationxy:.2f}")

    # Calculate slope and intercept of line of best fit
    slope, intercept = stats.linear_regression(time_x, temp_y)
    logger.info(f"The equation of the best fit line is: y = {slope:.2f}x + {intercept:.2f}")

    # Predicting values at a future time
    timemax = max(time_x)
    new_time = timemax * 15

    # Predict the y value at the future time  y = mx + b 
    # where m is the slope and b is the y intercept
    new_temp = slope * new_time + intercept

    logger.info(f"I predict that when x = {new_time}, y will be about {new_temp:.2f}")



def lab_built_in_functions():
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calcuate the max and min scores
    max_value = max(hemoglobin_values)
    min_value = min(hemoglobin_values)

    logger.info(f"Given hemoglobin_values list: {hemoglobin_values}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(hemoglobin_values)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(hemoglobin_values)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    # Create a set from given list
    hemoglobin_set = set(hemoglobin_values)
    logger.info(f"The set of the list hemoglobin_values is {hemoglobin_set}")

    logger.info(f"Given hemoglobin_list: {hemoglobin_values}")
    # Return a new list soreted in ascending order
    asc_hgb = sorted(hemoglobin_values)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_hgb}")

    # Return a new list soreted in descending order
    desc_hgb = sorted(hemoglobin_values, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_hgb}"
    )


def list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    # Make short list and print it
    lst = [1, 2, 3, 4, 5, 7, 8 ,9]
    logger.info(f"Short list = {lst}")

    # append 10 to the end of the list
    lst.append(10)
    logger.info(f"Appending 10 to list gives {lst}")

    # extend the list with another list
    lst.extend([10, 11, 12])
    logger.info(f'Extending list with [10, 11, 12] gives {lst}')

    # insert an item at a given position (0 = first item)
    i = 7
    newvalue = 77
    lst.insert(i, newvalue)
    logger.info(f'Inserting value 77 to position 7 gives {lst}')

    # remove an number 5
    item_to_remove = 5
    lst.remove(item_to_remove)
    logger.info(f'Removing number 5 from list gives {lst}')

    # Count how many times 2 appears in the list
    ct_of_2 = lst.count(2)
    logger.info(f'How many times is 2 in lst: {ct_of_2}')

    # Sort the list in ascending order using the sort() method
    lst.sort()
    logger.info(f'Sorted list = {lst}')

    # Sort the list in descending order using the sort() method
    lst.sort(reverse=True)
    logger.info(f'Descending sorted list = {lst}')

    # Copy the list to a new list
    new_lst = lst.copy()
    logger.info(f"new_lst is = {new_lst}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_lst.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_lst is: {new_lst}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_lst.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_lst is: {new_lst}"
    )

def lab_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info(f"Hemoglobin list: {hemoglobin_values}")

    # TRANFORMATIONS ............................

    # FILTER and MAP are critical tranformations in big data applications

    #Filter results for less than 7 meaning it is a critical result.
    results_less_than_7 = list(filter(lambda x: x < 7, hemoglobin_values))
    logger.info(f"Critical Hemoglobin Results: {results_less_than_7}")


    # Map each each x to cuberoot of x (hint: use math module)
    # cast the result to a list using square brackets
    cbrt_list = list(map(lambda x: x**(1/3) , hemoglobin_values))
    logger.info(f"Cube root list: {cbrt_list}") 


    # Use the built in map() function to calculate the volume of a cube with 
    # a side equal to the value in your list. Hint: Volume = side * side * side
    volume_list = list(map(lambda x: x ** 3 , hemoglobin_values))
    logger.info(f"Volume of a cube with each side: {volume_list}")


def lab_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info(f"Hemoglobin values: {hemoglobin_values}")   

    # Use a list comprehension to filter (start within square brackets) to 
    # get x (for each x in list1) if x is less than 4 or some other cutoff.

    Hgb_values2 = [x for x in hemoglobin_values if x < 7]
    logger.info(f"List comprehension critical values less than 7: {Hgb_values2}")

    # Use a list comprehension to triple each value in your list1, 
    # that is to get x*3 (for x in list1) 

    Trp_values = [x * 3 for x in hemoglobin_values]
    logger.info(f'Hemoglobin values tripled: {Trp_values}')

    # Use a list comprehension to transform your numeric list 
    # into another numeric list using a transformation of your choice.

    ###male version
    normal_range_hemoglobin_male = [x for x in hemoglobin_values if  x <= 17 and x >= 14]
    logger.info(f"Results in normal adult male range hemoglobin: {normal_range_hemoglobin_male}")

    ###female version
    normal_range_hemoglobin_female = [x for x in hemoglobin_values if  x <= 15 and x >= 12]
    logger.info(f"Results in normal adult female range hemoglobin: {normal_range_hemoglobin_female}")





def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())



# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    lab_statistics()
    lab_correlation_and_prediction()
    lab_built_in_functions()
    list_methods()
    lab_list_transformations()
    lab_list_comprehensions()
    
    show_log()




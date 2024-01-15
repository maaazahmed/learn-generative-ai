
def add_tow_numbers(num1, num2):
    """
    this function adds two numbers
    :param num1: first number
    :param num2: second number
    :return: sum of two numbers
    
    """
    return num1 + num2


def add_three_numbers(num1, num2, num3):
    """
    this function adds three numbers
    :param num1: first number
    :param num2: second number
    :param num3: third number
    :return: sum of three numbers
    """
    return num1 + num2 + num3
    

add_three_numbers(1, 2, 3)




# # create a function that takes a list of numbers and returns the sum of the numbers
# def sum_list(numbers):
#     """
#     this function takes a list of numbers and returns the sum of the numbers
#     :param numbers: list of numbers
#     :return: sum of the numbers
#     """
#     total = 0
#     for number in numbers:
#         total += number
#     return total




# # create a function that takes a list of numbers and returns the average of the numbers
def average_list(numbers):
    """
    this function takes a list of numbers and returns the average of the numbers
    :param numbers: list of numbers
    :return: average of the numbers
    """
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)




# create list of tuples like [(0,0),(0,0)] and make a dictnary

def make_dict(list_of_tuples):
    """
    this function takes a list of tuples and returns a dictionary
    :param list_of_tuples: list of tuples
    :return: dictionary
    """
    dictionary = {}
    for tuple in list_of_tuples:
        dictionary[tuple[0]] = tuple[1]
    return dictionary 

make_dict([(0,0),(0,0)])


# write a function that takes 2 number 1st one is table lit table of 2 and second number is end of table like 2 *  20

def table_of_number(table, end):
    """
    this function takes 2 number 1st one is table lit table of 2 and second number is end of table like 2 * 20
    :param table: table of 2
    :param end: end of table
    :return: table of 2
    """
    for i in range(1, end + 1):
        print(table * i)

table_of_number(2, 20)
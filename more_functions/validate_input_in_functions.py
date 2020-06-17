"""
Program: validate_input_in_functions.py
Author: Paul Ford
Last date modified: 06/17/2020
Purpose: Validates a users score and prints it back out.
         I have it where it prints and returns the end
         due to the wording in the assignment.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    If the default value for test_score is used print name and test score
    If the value submitted for score, test data, then print out name and test score
    :param test_name: Name on Test
    :param test_score: Score either entered in or gathered from user
    :param invalid_message: Changes the invalid message for bad data
    :return: Returns (Name: test_score)
    """
    # if test score is default we will print out name and 0
    if test_score != 0:
        try:
            # check all bad data if its bad
            if isinstance(test_score, str) or int(test_score < 0) or int(test_score > 100):
                raise ValueError
        except ValueError:
            print(invalid_message)
            while True:
                try:
                    # ask the user for new data since the function data was bad
                    test_score = int(input('Please enter your test score: '))
                    if int(test_score < 0) or int(test_score > 100):
                        raise ValueError
                except ValueError:
                    print(invalid_message)
                    continue
                else:
                    break
    # return {test_name: test_score}
    # prints first because that what the assignments says to do
    print(test_name + ': ' + str(test_score))
    return test_name + ': ' + str(test_score)


if __name__ == '__main__':
    pass

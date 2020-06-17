def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    # if test score is default we will ask until
    # we get valid data
    if test_score != 0:
        while True:
            try:
                test_score = int(test_score)
                if int(test_score < 0) or int(test_score > 100):
                    raise ValueError
                    continue
            except ValueError:
                print(invalid_message)
                test_score = int(input('Please enter your test score: '))
                continue
            break
    # return {test_name: test_score}
    return test_name + ': ' + str(test_score)


if __name__ == '__main__':
    print(score_input('Paul', 50))

# if not test_score.isdigit():
# print(invalid_message)

def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    while True:
        try:
            test_score = int(input('Please enter your test score: '))
        except ValueError:
            print(invalid_message)
            continue
        if int(test_score < 0) or int(test_score > 100):
            print(invalid_message)
            continue
        else:
            break
    # return {test_name: test_score}
    return test_name + ': ' + str(test_score)


if __name__ == '__main__':
    print(score_input('Paul'))

# if not test_score.isdigit():
# print(invalid_message)

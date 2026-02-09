"""
Returns the score in the form of a word into an integer

Parameters:
    score (str): Word descriptor of score. Must contain at least 1 character

Returns:
    result (int): Integer version of score value. Either 0, 3, 5, or 10 dependent on score
"""
def scoreToNumber(score):
    score = str.upper(score)
    result = 0
    first = score[0]
    if first == "G":
        result = 10
    elif first == "O":
        result = 5
    elif first == "P":
        result = 3
    return result

def main():
    score1 = input('Enter score 1 as Great, Ok, or Poor: ')
    score2 = input('Enter score 2 as Great, Ok, or Poor: ')
    score3 = input('Enter score 3 as Great, Ok, or Poor: ')
    x1 = scoreToNumber(score1)
    x2 = scoreToNumber(score2)
    x3 = scoreToNumber(score3)
    xmax = max(x1, x2, x3)
    some_avg = (x1 + x2 + x3) / 3
    print(f'The maximum score was {xmax}')
    print(f'The avg score on 1-10 scale would have been \
{round(some_avg, 2)}')

main()
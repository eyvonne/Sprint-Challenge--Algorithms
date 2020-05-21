'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if len(word) < 2:
        return 0
    else:
        if word[0:2] == 'th':
            return count_th(word[1:]) + 1
        else:
            return count_th(word[1:])
# This seems like the faster and easier way to do this, why wouldn't we use it?


def count_th_iterative(word):
    count = 0
    for i in range(len(word)-1):
        if word[i:i+2] == 'th':
            count += 1
    return count

"""
Interviewbit - Amazon
Bulls and Cows

link: https://www.interviewbit.com/problems/bulls-and-cows/

Problem Description:
    You are playing the Bulls and Cows game with your friend.
    You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
    Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls. 
    Given the secret number and your friend's guess, return the hint for your friend's guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Problem Constraints:
    1 <= secret.length, guess.length <= 100000
    secret.length == guess.length
    secret and guess consist of digits only.

Example Input:
    Input 1:
    secret = "1807", guess = "7810"
    Input 2:
    secret = "1123", guess = "0111"

Example Output:
    Output 1:
    "1A3B"
    Output 2:
    "1A1B"
"""

# @param A : string
# @param B : string
# @return a strings
def solve(a, b):
    bulls = 0
    cows = 0
    digit_counts1, digit_counts2 = dict(), dict()
    for c1, c2 in zip(a, b):
        if c1 == c2:
            bulls += 1
        else:
            digit_counts1[c1] = 1 if c1 not in digit_counts1 else digit_counts1[c1] + 1
            digit_counts2[c2] = 1 if c2 not in digit_counts2 else digit_counts2[c2] + 1

    cow_digits = set(digit_counts1.keys()).intersection(set(digit_counts2.keys()))
    for c in cow_digits:
        cows += min(digit_counts1[c], digit_counts2[c])
    
    return f"{bulls}A{cows}B"

if __name__ == "__main__":
    print(solve("6020943525972", "7157627311068"))
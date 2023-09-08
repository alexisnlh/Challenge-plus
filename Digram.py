import sys

"""
    We are given a string S consisting of N lowercase letters. A sequence of
    two adjacent letters inside a sting is called a digram. The distance
    between two digrams is the distance between the first letter of the first
    digram and the first letter of the second digram. For example, in sting
    S = 'akcmz' the distance between digrams 'kc' and 'mz' is 2.

    We want to find the distance between the furthest identical digrams inside
    string S.

    Write a function:

        def solution(S)

    that, given a string S consisting of N letters, returns the distance
    between the two identical digrams in the string that lie furthest away
    from each other. If there are no two identical digrams inside S, your
    function should return -1.

    Examples:

    1. Given S = 'aakmaakmakda' you function should return 7. The furthest
    identical digrams are 'ak's, starting in positions 2 and 9 (enumerating
    from 1): 'aakmaakmakda'

    2. Given S = 'aaa' your function should return 1. The furthest identical
    digrams are 'aa's starting at positions 1 and 2.

    3. Given S = 'codility' your function should return -1. These are no two
    identical digrams in S.

    Write an efficient algorithm for the following assumptions:

        - N is an integer within the range [2...300,000].
        - String S is made only of lowercase letters (a-z).
"""


def solution(s):
    if len(s) < 3:
        return -1

    digrams_dict = {}
    count_max = 0

    for index in range(len(s) - 1):
        if s[index:(index + 2)] in digrams_dict:
            count_origin = digrams_dict[s[index:(index + 2)]]
            difference = ((index + 1) - count_origin)
            if count_max < difference:
                count_max = difference
        else:
            digrams_dict[s[index:(index + 2)]] = index + 1
    if count_max == 0:
        return -1
    return count_max


def main():
    try:
        input_string = input("Introduzca la cadena de string que desea verificar (q --> EXIT): ").lower()
        if input_string == "q":
            sys.exit("Proceso finalizado!")

        result = solution(input_string)
        if result == -1:
            print(f"No hay digram en el string ingresado: {result}")
        else:
            print(f"Resultado del digram: \n{result}")
    except Exception as error:
        print(f"Error Exception: {error}")
        sys.exit()


if __name__ == '__main__':
    main()

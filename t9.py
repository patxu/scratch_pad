"""
Has some similarity to: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Problem Statement:
T9 is a type of keypad commonly seen on mobile phones (see picture below). To type with T9, a user enters digits and a program (also called an input method) translates the input into English words with the help of a dictionary stored on the device.

The main function will be given two inputs:

**`input_digits`**: an integer array (contains only 2-9 and length is up to 25)

**`valid_words`**: a string array, defines a list of valid English words. (up to 50)


A 2D string array of all the possible word combinations that the given input can be mapped to. More specifically, the return value is of format **`[<word combinations 1>, <word combinations 2>, ...]`** where each **`<word combinations>`** is an array of words, which represents one word or a list of words the input digits can be translated into.

For example, let's say 'cat' is given as a valid word and the input is 228. The only **`<word combinations>`** in this case is [**`"cat"`**].

In a different example, where all of "some", "time" and "sometime" are given as valid words, and the input of 76638463. Both **`["some", "time"]`** and **`["sometime"]`** are valid **`<word combinations>`**s


"""


class Solution:
    t9 = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    def test(self):
        inputs = [
            (
                [2, 2, 8],
                ["act", "bat", "cat", "acd", "test"],
                [["act"], ["bat"], ["cat"]],
            ),
            (
                [7, 6, 6, 3, 8, 4, 6, 3],
                ["some", "time", "rome", "sometime", "so", "me"],
                [
                    ["rome", "time"],
                    ["so", "me", "time"],
                    ["some", "time"],
                    ["sometime"],
                ],
            ),
        ]

        for input in inputs:
            input, valid_words, expected = input
            output = self.solution(input, valid_words)
            if output == expected:
                print("Success:")
            else:
                print("Failure:")
            print(
                "\tinput: ", input, "\n\texpected: ", expected, "\n\toutput: ", output
            )

    def solution(self, input_digits, valid_words):
        results = []
        self.helper(0, input_digits, "", [], set(valid_words), results)

        return results

    # example input for first test case
    # 228
    # ['a', 'b', 'c'], ['a', 'b', 'c'], ['t', 'u', 'v']
    def helper(
        self, depth, input_digits, candidate, words_so_far, valid_words, results
    ):
        if candidate in valid_words:
            if len(input_digits) == depth:
                results.append(words_so_far + [candidate])
            else:
                self.helper(
                    depth,
                    input_digits,
                    "",
                    words_so_far + [candidate],
                    valid_words,
                    results,
                )

        if len(input_digits) > depth:
            for char in self.t9[input_digits[depth]]:
                self.helper(
                    depth + 1,
                    input_digits,
                    candidate + char,
                    words_so_far[:],
                    valid_words,
                    results,
                )


Solution().test()

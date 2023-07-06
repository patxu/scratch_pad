'''
Simple boilerplate for writing and testing technical interview questions.

Problem Statement:


'''

class Solution():
    def test(self):
        inputs = [('value', False), ('value', True)]

        for input in inputs:
            value, expected = input
            output = self.solution(value)
            if output == expected:
                print('Success:', input, output)
            else:
                print('Failure:', input, output)

    def solution(self, input):
        pass

Solution().test()
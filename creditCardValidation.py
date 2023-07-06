'''
Credit Card validation

In order to ensure the credit card number is valid, we want to run some very basic validation.

You need to ensure the string **is only composed of digits [0-9] and is between 12 and 16 characters long** (although most cards are 15 to 16, let's keep it simple).

- Starting with the rightmost digit, which is the check digit, and moving left, double the value of every second digit. If the result of this doubling operation is greater than 9 (e.g., **`8 * 2 = 16`**), then add the digits of the product (e.g., **`16`**: **`1 + 6 = 7`**, **`18`**: **`1 + 8 = 9`**).
- Take the sum of all the digits.
- If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is **valid** according to the Luhn algorithm, otherwise it is not valid.
'''

class Solution():
    def test(self):
        inputs = [('4111111111111111', False), ('5454545454545454', False), ('378282246310005', True)]

        for input in inputs:
            number, expected = input
            output = self.solution(number)
            if output == expected:
                print('Success:', input, output)
            else:
                print('Failure:', input, output)

    def solution(self, card_number):
        if len(card_number) < 12 or len(card_number) > 16:
            return False
        
        luhn_sum = 0

        for index, char_num in enumerate(card_number):
            try:
                num = int(char_num)
            except:
                return False
            
            
            if index % 2 == 1:
                product = num * 2
                if product > 9:
                    for digit in str(product):
                        luhn_sum += int(digit)
                else:
                    luhn_sum += product
            else:
                luhn_sum += num
        
        return luhn_sum % 10 == 0

Solution().test()
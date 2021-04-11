class Validator:
    def __init__(self, text):
        """
        Initialize parser

        :param text: Text passed into parser
        """
        self.text = text
        self.valid = False
        self.operators = ['+', '-', '*', '/', '^', '√', '!']
        self.constants = ['π', '(', ')']
        self.functions = ['sin', 'cos']

        # Run calculator's input validation
        if self.validate(text):
            self.valid = True
        else:
            self.valid = False

    def validate(self, text):
        """
        Validates text from user input

        :param text: Text to validate
        :return: True if text is valid otherwise false.
        """
        index = 0
        comma = False
        prevChar = None
        openedParentheses = 0
        closedParentheses = 0

        # Check if input is not empty
        if len(text) == 0:
            print('Empty field')
            return False

        # Check if first char is not arithmetic operator or comma
        if len(text) > 0 and (text[0] in self.operators or text[0] == ','):
            print('First character can not be an operator/comma')
            return False

        # Check if last char is not arithmetic operator or comma
        if len(text) > 0 and ((text[-1] in self.operators and text[-1] != '!') or text[-1] == ','):
            print('Last character can not be an operator/comma (except !)')
            return False

        while index < len(text):
            char = text[index]

            # Check if number is after comma
            if comma and not char.isnumeric():
                print('Number is excepted after comma')
                return False
            elif comma and char.isnumeric():
                comma = False

            # Check for math functions
            if char == 's' or char == 'c':
                # Check if operator is set before function
                if prevChar and (prevChar not in self.operators and prevChar != '('):
                    print(prevChar)
                    print('No arithmetic operator before function')
                    return False

                if self.__is_valid_math_function(text, index):
                    index += 4
                    openedParentheses += 1
                    prevChar = '('
                    continue
                else:
                    print('Invalid math function')
                    return False

            # Check if character is valid
            if char not in self.operators + self.constants and char != ',' and not char.isnumeric():
                print('Char is not in operators/constants and not numeric or comma')
                return False

            # Check if there is not a arithmetic operator before left parenthesis or constants
            if prevChar and (char in self.constants and char != ')' and prevChar not in self.operators):
                print('No arithmetic operator before left parenthesis or constants')
                return False

            # Count parentheses
            if char == '(':
                openedParentheses += 1
            if char == ')':
                closedParentheses += 1

            # Check if operator is not followed by another operator
            if prevChar and (char in self.operators and prevChar in self.operators) and prevChar != '!':
                print('Operator is followed by another operator')
                return False

            # Check if parentheses are not empty
            if prevChar and (char == ')' and prevChar == '('):
                print('Empty parentheses')
                return False

            # Check for double comma
            if prevChar and (char == ',' and prevChar == ','):
                print('Found multiple commas')
                return False

            # Check for number before comma
            if prevChar and (char == ',' and not prevChar.isnumeric()):
                print('No number before comma')
                return False

            # Set comma flag
            if char == ',':
                comma = True

            prevChar = char
            index += 1

        # Check if number of opened parentheses = number of closedParentheses
        if openedParentheses != closedParentheses:
            print('Opened and closed parentheses are not equal.')
            return False

        return True

    def is_valid(self):
        """
        Returns valid status.

        :return: True if user input is valid otherwise false.
        """
        return self.valid

    def __is_valid_math_function(self, text, index):
        """
        Validates math functions (sin, cos)

        :param text: Input from calculator
        :param index: Current index
        :return: True if math function is valid otherwise false.
        """
        if index + 3 < len(text):
            function = str(text[index] + text[index + 1] + text[index + 2])
            if function in self.functions and text[index + 3] == '(':
                return True
            return False

        return False


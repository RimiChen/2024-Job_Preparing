s = "1-(     -2)"

class Solution:
    def calculate(self, s: str) -> int:
        ### remove blank
        s = s.replace(" ", "")
        string_array = list(s)
        print(string_array)
        special_char = ["+", "-", "(", ")"]        
        processing_stack = []
        index = 0
        while index < len(string_array):
            if string_array[index] not in special_char:
                ### start parsing number
                # print("not special", string_array[index])
                new_number, index = self.combine_numbers(string_array, index, special_char)
                processing_stack.append(new_number)
            else:
                # print("special", string_array[index])
                if string_array[index] == ")":
                    new_number, processing_stack = self.compute(processing_stack, special_char)
                    # processing_stack.append(new_number)
                else:
                    processing_stack.append(string_array[index])
                index = index + 1
            print("stack", processing_stack)
            # index = index + 1
        result, index = self.compute(processing_stack, special_char)
        return result
    ### for processing decimal number > 9
    def combine_numbers(self, string_array, index, special_char):
        number = 0
        new_index = index
        while new_index < len(string_array) and string_array[new_index] not in special_char:
            number = number * 10 +int(string_array[new_index])
            new_index = new_index + 1
            print("new_index", new_index, "number", number)
        return number, new_index
    ### resolve negative number
    def get_number(self, processing_stack):
        if len(processing_stack) >0:
            print("current key", processing_stack[-1])
            number = int(processing_stack[-1])
            processing_stack.pop()
            if  len(processing_stack) > 0 and processing_stack[-1] =="-":
                processing_stack.pop()
                return (-1)*number, processing_stack
            else:
                return number, processing_stack
        else:
            return 0, processing_stack
    ### compute the equation
    def compute(self, processing_stack, special_char):
        answer = 0
        while len(processing_stack) > 0 and processing_stack[-1] != "(":
            # print("answer", answer)
            if processing_stack[-1] not in special_char:
                ### number
                computing_result, processing_stack = self.get_number(processing_stack)
                print("get number ", computing_result)
                if answer == 0:
                    answer = computing_result
                else:
                    answer = answer + computing_result
                    # processing_stack.pop()
            else:
                processing_stack.pop()

        if len(processing_stack) > 0 and processing_stack[-1] == "(":
            print("( prepare to pop", answer)
            processing_stack.pop()

        processing_stack.append(answer)
        return answer, processing_stack

class Reference_Solution:
    def calculate(self, s):
        def evaluate(i):
            res, digit, sign = 0, 0, 1
            
            while i < len(s):
                if s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                elif s[i] in '+-':
                    res += digit * sign
                    digit = 0
                    sign = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    subres, i = evaluate(i+1)
                    res += sign * subres
                elif s[i] == ')':
                    res += digit * sign
                    return res, i
                i += 1

            return res + digit * sign
        
        return evaluate(0)

if __name__ == "__main__":
    solution = Solution()
    ans = solution.calculate(s)
    print(ans)
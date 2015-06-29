class Solution:
    def __init__(self):
        self.stack = []
        self.cur_num = ""
        self.index = 0
        
    def __reset__(self):
        self.stack = []
        self.cur_num = ""
        self.index = 0
        
    # @param {String} s
    # @return {integer}
    def calculate(self, s):
        self.__reset__()

        while self.index < len(s):
            ch = s[self.index]
            if is_space(ch):
                self.index += 1
                continue
            print ch, '%d', self.index

            # if is '(' or operator,just push it to the stack
            if is_left_brace(ch) or is_operator(ch):
                self.stack.append(ch)
                self.index += 1
                continue
            
            if is_num(ch):
                # if the first ele is number
                while self.index < len(s):
                    if is_num(s[self.index]):
                        self.cur_num += s[self.index]
                        self.index += 1
                    else:
                        break

                ch_int = int(self.cur_num)
                self.handle_num(ch_int)
                self.cur_num = ""
                continue

            if is_right_brace(ch):
                top = self.stack.pop()
                if is_left_brace(ch):
                    self.index += 1
                    continue
                else:
                    self.stack.pop()
                    self.handle_num(top)
                    self.index += 1
                    continue
        return self.stack[0]

    def handle_num(self, num):
        if len(self.stack) == 0:
            self.stack.append(num)
            return
        # get the top ele in the stack
        top = self.stack.pop()

        # if th top ele is '(', push the num to the stack
        if is_left_brace(top):
            self.stack.append(top)
            self.stack.append(num)
            return
        # if the top ele is operator ,
        # do the operation and push the ans to the stack
        if is_operator(top):
            pre_value = self.stack.pop()
            if top == '+':
                new_value = pre_value + num
            else:
                new_value = pre_value - num
            self.stack.append(new_value)

    def dump_stack(self):
        for ch in self.stack:
            print ch

def is_num(val):
    return '0' <= val <= '9'

def is_space(val):
    return val == ' '

def is_operator(val):
    return val == '+' or val == '-'

def is_left_brace(val):
    return val == '('

def is_right_brace(val):
    return val == ')'


if __name__ == "__main__":
    s = Solution()
    print s.calculate('(1+(4+5+2)-3)+(6+8)')


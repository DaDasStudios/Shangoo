import eval_math

class Drawer():
    def __init__(self, expression):
        ''' Class to work with strings and get show the manual results into a string '''
        self.terms = []
        self.original_exp = expression
        self.operations_dict = {
            'plus': [],
            'minus': [],
            'mult': [],
            'div': []
        }
        self.dot_pos = 0 # Position of the '.' in the strs
        self.point_pos = []

    def split_negative_operations(self, expression: str):
        ''' Finding ```*- | /-```characters in expression, and replace them into a new expression\n
        This is because this character have to be replaced first than other due their sign '''
        mul_signs = ['*-','/-']
        for d_sign in mul_signs:
            if d_sign in expression:
                __idx = expression.find(d_sign)
                __end_idx = __idx + 2 
                for j in expression[__idx+2:]:
                    if j == '.': __end_idx += 1
                    else:   
                        try:
                            float(j)
                            #print('Plused')
                            __end_idx += 1
                        except ValueError: 
                            #print(end_idx)
                            self.terms.append(expression[__idx:__end_idx])
                            expression = expression.replace(expression[__idx:__end_idx],'',1)
                            break
        return expression

    def split_signs(self):
        ''' Replacing the rest of the operations which have a ```positive``` sign
            \nHowever if you don't pass positive operations, it will call automatically ```split_negative_operations``` function, and to solve this issue  '''
        expression = self.original_exp + ' '
        signs = ['+','-','*','/']
        current_idx = 0
        end_idx = 0
        # No matter if there's + sign at beggining of the expression
        if not expression[0] in signs:
            expression = f'0+{expression}'
        # Finding *- | /- characters in expression, and replace them into a new expression
        expression = self.split_negative_operations(expression)
        #print('New expression replaced:', expression)
        for i in expression:
            if i in signs:
                end_idx = current_idx
                for j in expression[current_idx+1:]:
                    if j == '.': end_idx += 1
                    else:   
                        try:
                            float(j)
                            #print('Plused')
                            end_idx += 1
                        except ValueError: 
                            #print(end_idx)  
                            current_expression = expression[current_idx+1:end_idx+1]                
                            self.terms.append(str(float(current_expression)))
                            # Adding the positions of the point of the numbers
                            self.point_pos.append(current_expression.find('.'))
                            break
            current_idx += 1
        # Finding the point position
        #print(f'Point position list: {self.point_pos}')
        self.dot_pos = max(self.point_pos)
        #print(f'Dot position: {self.dot_pos}')
        return self.terms

    def built_columns(self, terms: list):
        ''' Building the columns, lining up the digit in a matrix '''
        global dot_axis
        __terms_len = len(terms)
        self.lenght_list = ['' for i in range(__terms_len)]
        __len_idx = 0
        for term in terms:
            # Create a new list with the lenght of the numbers
            self.lenght_list[__len_idx] = len(term)
            __len_idx += 1
        #print(f"List with the numbers lenght: {self.lenght_list}")
        biggest_num = terms[self.lenght_list.index(max(self.lenght_list))]
        #print(f"The biggest found number is: {biggest_num}")
        # Setting the dot axis
        dot_axis = str(biggest_num).find('.')
        #print(f"Dot axis is: {dot_axis}")
        digit_matrix = [[0 for column in range(len(biggest_num))] for row in range(__terms_len)]
        #print(f"Empty digit matrix: {digit_matrix}")
        __row_idx = 0
        for num in terms:
            __colm_idx = dot_axis + 1 
            for digit in num[num.find('.')+1:]:
                digit_matrix[__row_idx][__colm_idx] = int(digit)
                __colm_idx += 1
            __row_idx += 1
        #print(f"Right filled matrix next to dot: {digit_matrix}")
        __row_idx = 0
        for num in terms:
            __colm_idx = dot_axis - 1
            for digit in eval_math.reversed_str(num[:num.find('.')]):
                digit_matrix[__row_idx][__colm_idx] = int(digit)
                __colm_idx -= 1
            __row_idx += 1
        #print(f"Left fille matrix next to dot: {digit_matrix}")
        __row_idx = 0
        for row in digit_matrix:
            digit_matrix[__row_idx].pop(dot_axis)
            __row_idx += 1
        #print(f"Digits matrix with the dots: {digit_matrix}")
        return digit_matrix

    def draw_sum(self, terms: list):
        ''' Return a string built with the real procediment for solving a math plus '''
        # Creating the residues list
        residues_list = [0 for _ in range(len(terms[0]))]
        #print(f"Empty residues list: {residues_list}")
        # Creating the results list 
        results_list = [0 for _ in range(len(terms[0]))]
        # Doing the sum
        __len_terms = len(terms[0])
        __clm_idx = -1
        current_result = 0
        for first in range(__len_terms):
            for i in terms:
                try:
                    current_result += i[__clm_idx]
                except TypeError: pass
            current_result += residues_list[__clm_idx]
            if current_result > 9 and __len_terms+__clm_idx == 0: pass
            elif current_result > 9:
                residues_list[__clm_idx-1] = int(str(current_result)[:-1])
                current_result = int(str(current_result)[-1])
            results_list[__clm_idx] = current_result
            #print(f'Current result: {current_result}')
            __clm_idx -= 1
            current_result = 0
        #print(f"Filled residues list: {residues_list}")
        #print(f"Results list: {results_list}")

        def build_str(residues, matrix_digit, results):  
            ''' Building the final string with the manual result '''
            # Build a str with the results
            result_str = ''
            def draw_lines(sign: bool):
                lines = ''
                for _ in range(len(residues)+1):
                    if _ == 0: lines += ' ─'
                    else: lines += '──' 
                if sign: lines += ' +'
                return lines
            cont = 0
            for residue in residues:
                if cont == dot_axis: result_str += ' '
                result_str += ' '+str(residue)
                cont += 1
            result_str += '\n'  
            result_str += draw_lines(False)
            result_str += '\n'
            for row in matrix_digit:
                cont = 0
                for digit in row:
                    if cont == dot_axis: result_str += '.'
                    result_str += ' '+str(digit)
                    cont += 1
                result_str += '\n'
            result_str += draw_lines(True)
            result_str += '\n'
            cont = 0
            for result in results:
                if cont == dot_axis: result_str += '.'
                result_str += ' '+str(result)
                cont += 1
            return result_str

        result_str = build_str(residues_list, terms, results_list)
        return result_str

    def draw_subtraction(self, terms: list):
        ''' Return the strings wth the answers operated manually '''
        # ? Drawing results in a new str
        def build_str(digit_matrix: list, result_list: list):
            results_str = ''

            def draw_lines(sign: bool):
                lines = ''
                for _ in range(len(result_list)+1):
                    if _ == 0: lines += ' ─'
                    else: lines += '──' 
                if sign: lines += ' -'
                return lines

            for row in digit_matrix:
                cont = 0
                for clm in row:
                    if cont == dot_axis: results_str += '.'
                    results_str += f' {clm}'
                    cont += 1
                results_str += '\n'
            results_str += draw_lines(True)
            results_str += '\n'
            cont = 0
            for digit in result_list:
                if cont == dot_axis: results_str += '.'
                results_str += f' {digit}'
                cont += 1
            return results_str

        # Creating the results list
        results_list = [0 for _ in range(len(terms[0]))]
        #print(f"Empty results list: {results_list}")
        # ? Doing the first string without results
        last_result_str = build_str(terms, results_list)
        # ? Doing the substraction
        __len_terms = len(terms)
        __clm_idx = -1

        def take_one(idx: int):
            ''' A recursion function for take one dependeinof if the next digit is > 0, else try with the next's next '''
            #print(f'Index: {idx}')
            new_terms = terms[0][:idx]
            for digit in reversed(new_terms):
                #print(f'\n{digit}')
                __index = self.index_last(new_terms, digit)
                if digit > 0:        
                    terms[0][__index] -= 1
                    terms[0][__index+1] += 10
                    #print(f'{digit} Mayor que 0 con index {__index}')
                    break
                else:
                    #print('Enter in recursion')
                    #print(f'Calculated index {__index}')
                    #print(f'We need take one again in {__index-1}')
                    #print(terms[0][:idx])
                    take_one(__index)
                    #print(f'{digit} Menor que 0')
                    take_one(__index+1)
                    #print('We leave')
                    break
            #print(f'Renoved matrix: {terms}')

        for times in range(len(terms[0])):
            current_result = terms[0][__clm_idx]
            for row in range(__len_terms-1):
                current_result -= terms[row+1][__clm_idx]
            if current_result < 0:
                #print(f'We call `take one` in index {__clm_idx}')
                take_one(__clm_idx)
                current_result = terms[0][__clm_idx]
                for row in range(len(terms)-1):
                    current_result -= terms[row+1][__clm_idx]
            results_list[__clm_idx] = current_result
            __clm_idx -= 1
        #print(f"Filled digit matrix: {terms}")
        #print(f"Results: {results_list}")

        results_str = build_str(terms, results_list)
        results_str = last_result_str + '\n\n────────────\n\n' + results_str
        return results_str

    def draw_multiply(self, terms: list):
        ''' Return a string solved like real life '''
        __sample = self.get_len(terms[-1])
        __real_result = len(str(float(eval(self.original_exp))))
        terms[-1] = self.del_zeros(terms[-1])
        results_matrix = [[0 for _ in range(__real_result)] for i in range(__sample)]
        #print(f"Empty results list: {results_matrix}")

        # ? Validation
        def validation(result: str, row, clm, retard):
            ''' Validating if the lenght of current result is greater than 1, then resort the results list '''
            if len(str(result)) > 1:
                letters = self.split_words(str(result))
                __delay = 0
                for letter in reversed(letters):
                    results_matrix[row][clm-__delay-retard] = int(letter)
                    __delay += 1
                #print(letters)
                
        # ? Doing multiplication     
        def multiply_line(row_base: int, result_var: int, retard: int):
            __clm_idx = -1
            __rest_rslt = 0
            __sample_rslt = 0
            for i in terms[row_base]:       
                #print(f"The residue to sum: {__rest_rslt}")
                result = result_var
                result *= terms[row_base][__clm_idx] 
                try:
                    if __sample + __clm_idx == 0:
                        result += __rest_rslt
                    elif result > 9:
                        #print(f"Sample of {result}", end='')
                        result += __rest_rslt
                        __sample_rslt = int(str(result)[-1])          
                        __rest_rslt = int(str(result)[:-1])
                        #print(f" = {__sample_rslt} and the rest: {__rest_rslt}")        
                    else:
                        result += __rest_rslt
                    results_matrix[retard][__clm_idx-retard] = result
                    #print(f"Current result: {result}")
                    #print(F'ROW: {retard}')
                    validation(result, retard, __clm_idx, retard)
                except TypeError: break
                __clm_idx -= 1
            start_idx = LEN_RESULTS_LIST-len(results_matrix[retard])-retard
            end_idx = LEN_RESULTS_LIST-retard
            #print(f"Start index: {start_idx}, End index: {end_idx}")
            #print(f"Last results matrix: {results_matrix}")
            #results_matrix[retard] = self.fill_spaces(results_matrix[retard], LEN_RESULTS_LIST, start_idx, LEN_RESULTS_LIST)
            return result
        
        # ? Sum the results matrix using the manual way
        def sum_results():
            ''' Sum the results like manual way '''
            residue_list = [0 for x in range(len(results_list))]
            #print(f"Empty residues list: {residue_list}")
            #print(f"Empty results list: {results_list}")
            # Now to iterate the results matrix list and sum the digits...
            __clm_idx = -1
            for element in results_matrix[-1]:
                __row_idx = -1
                result = 0
                for each in results_matrix:
                    #print(f'Current number: {results_matrix[__row_idx][__clm_idx]}')
                    result += results_matrix[__row_idx][__clm_idx]
                    __row_idx -= -1
                #print(f"Last result {result}")
                result += residue_list[__clm_idx]
                if LEN_RESULTS_LIST - __clm_idx == 0:
                    pass
                elif result > 9:
                    #print(f"The residue is: {(str(result))}")
                    residue_list[__clm_idx-1] = int(str(result)[:-1])
                    result = int(str(result)[-1])
                # Setting the result into the list
                results_list[__clm_idx] = result
                #print(f"Sumed result: {result}")
                __clm_idx -= 1
            #print(f"Filled residue list: {residue_list}")

        # ! Main part
        # List for the final results
        global LEN_RESULTS_LIST
        results_list = [0 for i in range(len(results_matrix[-1])+len(results_matrix)-1)]
        LEN_RESULTS_LIST = len(results_list)
        #print(f"Lenght of the results list: {LEN_RESULTS_LIST}")

        retard_row = 0
        for digit in reversed(terms[-1]):
            #print(f"\nWe are multiplying by: {digit}")
            result_var = multiply_line(0, digit, retard_row)
            retard_row += 1

        #print(f"Filled results matrix: {results_matrix}")
        # Sum the results
        sum_results()

        # ? Building the result string
        def build_str():
            ''' Return a ```str``` similar to the real procedure when you solve a multiplication '''
            result_str = ''

            # Create lines function
            def draw_lines(sign: bool, type: str):
                lines = ''
                for _ in range(len(results_list)+1):
                    if _ == 0: lines += ' ─'
                    else: lines += '──' 
                if sign: lines += f' {type}'
                return lines

            # Part of the matemathic expression
            for list in terms:
                result_str += '\n'
                # ? The spaces for lining up the terms
                __rest = len(results_list) - len(list)
                for i in range((__rest*2)-2):
                    result_str += ' '
                for elmnt in list:
                    result_str += f' {elmnt}'
            result_str += '\n' + draw_lines(True, 'x')
            # Multipliy section  
            for list in results_matrix:
                result_str += '\n'
                for elmnt in list:
                    result_str += f' {elmnt}'
            result_str += '\n' + draw_lines(True, '+') + '\n'
            # Results section
            for elmnt in results_list:
                result_str += f' {elmnt}'
            return result_str
        #print(f'The results are: {results_list}')

        # Replacing the left zeros into ' ' 
        __row = 0
        for list in results_matrix:
            results_matrix[__row] = self.replace_zeros(results_matrix[__row], ' ')
            __row += 1
        # Doing the same with the results
        results_list = self.del_zeros(results_list)
        # Removing the lists with only ' '
        __row = 0
        black_list = []
        __idx = 0
        for list in results_matrix:
            if self.check_str(list, ' '):
                black_list.append(__idx)
            __idx += 1
        # Deleting the lists
        __retard = 0
        for idx in black_list:
            results_matrix.pop(idx-__retard)
            __retard += 1
        return build_str()

    def draw_division(self, terms: list):
        ''' Return a string solved like real life '''
        # Escentials
        result_list = []
        residues_list = []
        # Transform the whole list, deleting the zeros at left
        for row in range(len(terms)):
            terms[row] = self.del_zeros(terms[row])
        #print(f"Transformed list: {terms}")    
        
        # We gotta identify the diviser, deleting the zeros at left side, then create a new string, concatenate and transform to int
        diviser_list = terms[-1]
        diviser_str = ''
        for digit in diviser_list: diviser_str += str(digit)
        global DIVISER
        DIVISER = int(diviser_str)
        #print(f"The diviser is: {DIVISER}")

        def get_dividend(terms: list, start_idx: int):
            ''' To try get the maximum number for divide without get a decimal number '''
            numbers_str = ''
            end_idx = start_idx+1 
            for digit in terms[start_idx:]:
                numbers_str += str(digit)
                if int(numbers_str) >= DIVISER: return int(numbers_str), end_idx
                end_idx += 1

        def try_next(current_number: str, current_idx: int):
            ''' Trying return a new number for dividing '''
            new_term = str(current_number)
            end_idx = current_idx + 1
            #print(f'The term what we are working on: {new_term} from index: {end_idx}')
            for digit in terms[0][current_idx:]:
                new_term += str(digit)
                if int(new_term) >= DIVISER: return int(new_term), end_idx
                end_idx += 1

        def try_divide(dividend: int):
            ''' Return the result of divide two numbers (Dividend divided by Diviser) '''
            result = 0
            module = None
            try:
                result = dividend / DIVISER
                module = dividend % DIVISER
            except ZeroDivisionError: pass

            return int(result), module
                     
        # Get the maximum dividend
        try:
            dividend = get_dividend(terms[0], 0)
            dividend_num = dividend[0]
            # Next index to use
            __next_idx = dividend[1]
            # Get the results and modules
            current_results = try_divide(dividend_num)
            current_result = current_results[0]
            rest = current_results[1]
            #print(f"\ninital rest: {rest}")
            # Saving escentials
            residues_list.append(dividend_num)
            result_list.append(current_result)
        except TypeError:
            dividend_num = None
            __next_idx = None
            rest = ''
            for digit in self.convert_list_to(terms[0], str):
                rest += digit
            rest = int(rest)
            result_list.append(0)
            
        #print(f"Next index to dividide: {__next_idx}")
        # Repeat it indefintely until to find the decimal limit
        while dividend_num != None:
            # When -dividend_num- equals -None- that means that we've found the decimal limit
            try:
                #print(f"\nThe maximum number to divide in this occasion is {dividend_num}")
                #print(f"Current result: {current_result} and the rest is dividing {dividend_num} by {DIVISER} = {rest}")
                dividend = try_next(rest, __next_idx)
                #print(f"Dividen list: {dividend}")
                dividend_num = dividend[0]
                __next_idx = dividend[1]       
                current_results = try_divide(dividend_num)
                current_result = current_results[0]
                rest = current_results[1]
                residues_list.append(dividend_num)
                result_list.append(current_results[0])
                #print(f"Next index to divide: {__next_idx}")
            except TypeError: 
                dividend_num = None
        # Once we reached the decimal limit, we proceed to get the decimals
        else:
            # If the rest equals zero the operation is done
            if rest == 0: 
                #print(f"We've finished! ")
                pass
            else:
                result_list.append(f'.')
                for time in range(9):
                    if rest == 0: break
                    dividend_num = str(rest)
                    dividend_num += '0'
                    dividend_num = int(dividend_num)
                    #print(f"New rest for using in decimals: {rest}")
                    current_results = try_divide(dividend_num)
                    current_result = current_results[0]
                    rest = current_results[1]
                    #print(f"Current result: {current_result} and the rest is dividing {dividend_num} by {DIVISER} = {rest}")
                    residues_list.append(dividend_num)
                    result_list.append(current_result)
        #     print(f"We reached the decimal part!")

        # print(f"Residues/Module list: {residues_list}")
        # print(f"Result list: {result_list}")

        def build_str():
            ''' Return a string with all the manual procedure '''
            def build_result():
                result_str = ''
                for elmnt in result_list: result_str += str(elmnt)
                return result_str

            __len_residue = len(residues_list) 
            total_result_str = ''
            retard = ' '
            limit_idx = len(str(residues_list[0])) + __len_residue
            limit_cont = len(str(residues_list[0]))
            cont = 0
            # If the lenght of tha list is less than 3, we will add the missing objects as an empty strings
            if __len_residue < 3:
                for item in range(3-__len_residue):
                    residues_list.append('')
            #
            for residue in self.convert_list_to(residues_list, str):
                if cont == 0:
                    retard += ' '
                    total_result_str += residue
                    total_result_str += self.add_spaces(limit_idx-len(residue), '') + f'    {DIVISER}' + '\n' + retard 
                elif cont == 1:     
                    #retard += ' '
                    total_result_str += residue 
                    total_result_str += self.add_spaces(limit_idx-len(residue), '') + '  ────────────────' + '\n' + retard
                elif cont == 2:
                    total_result_str += residue 
                    total_result_str += self.add_spaces(limit_idx-len(residue), '') + f'  {build_result()}' + '\n' + retard
                   
                else:
                    total_result_str += residue + '\n' + retard
                retard += ' '
                cont += 1

            #print(limit_idx)
            return total_result_str

        result_str = build_str()
        print('The result str:\n',result_str)
        return(result_str)

    def filter_signs(self, elements: list):
        ''' Filtering all the elements into a brand new ```dict```, they'll be separated by ```+ or -``` operation, and ```/ or *``` opertations, no mattering the sign'''
        self.signs_law = {
            'plus_minus': [], 'mul_div': []
        }
        for element in elements:
            if '*' in element or '/' in element:
                self.signs_law['mul_div'].append(element)
            elif '+' in element or '-' in element:
                self.signs_law['plus_minus'].append(element)
        return self.signs_law

    def filter_type_operation(self):
        ''' Filter the operations even more, return a dict with every operation type 
        \nYou must have had called ```filter_signs``` function, else this won't gork '''
        for element in self.signs_law:
            for number in range(len(self.signs_law[element])):
                _current = self.signs_law[element][number][0]
                if _current == '+':
                    self.operations_dict['plus'].append(self.signs_law[element][number])
                elif _current == '-':
                    self.operations_dict['minus'].append(self.signs_law[element][number])
                elif _current == '/':
                    self.operations_dict['div'].append(self.signs_law[element][number])
                elif _current == '*':
                    self.operations_dict['mult'].append(self.signs_law[element][number])

        return self.operations_dict

    # ! Strings set

    def split_words(self, text: str):
        words_list = [None for x in range(len(text))]
        idx = 0
        for letter in text:
            words_list[idx] = letter
            idx += 1
        return words_list

    def index_last(self, text: str, ocurrence: str):
        ''' Find the last ocurrence of a str, and return the index of it '''
        index = 0
        for i in text:
            if i == ocurrence: index += 1
        return index

    def lineup(self, *args):
        """ Return a str lined up with the lists received before """
        lenght = len(args[0])
        for i in args:
            if len(i) == lenght: pass
            else: return 'Same lenght in lists!'
        # Separating elements for indexes
        serie = ''
        rows_text = []
        for elmn in range(lenght):
            for list in args:                     
                serie += list[elmn]
                serie += ' '
            rows_text.append(serie.split())
            serie = ''
        lenght_texts = [int(i) for i in range(lenght)]
        index = 0
        for list in rows_text:
            lenght_texts[index] = self.max_str(list)+2
            index += 1
        fnl_serie = ''
        size = len(args)
        for i in range(size):
            for j in range(len(args[i])):
                rmng = lenght_texts[j] - len(args[i][j])
                fnl_serie += self.add_spaces(rmng, args[i][j])
            fnl_serie += '\n'   
        return fnl_serie.strip()

    def add_spaces(self, times:int, text:str):
        ''' Add a amount of spaces to a str '''
        for space in range(times):
            text += ' '
        return text

    def max_str(self, list:list):
        """ Return the str with the largest text of the list """
        lenghts = []
        for i in list:
            lenghts.append(len(i))
        return int(max(lenghts))

    # ! Lists

    def convert_list_to(self, list: list, object: type):
        ''' Return a list with all elements converted to what you choiced '''
        new_list = ['' for x in range(len(list))] 
        cont = 0
        for element in list:
            new_list[cont] = object(element)
            cont += 1
        return new_list

    def index_last(self, list: list, obj: str):
        ''' Find the last ocurrence of somethin in a list, and return the index of it '''
        index = 0
        return_idx = 0
        for i in list:
            if i == obj: return_idx = index
            index += 1
        return return_idx

    def del_zeros(self, list: list):
        ''' Delete all the left zeros in the passed list, this is useful for ```draw_multipliying``` function '''
        idx_list = []
        idx = 0
        for element in list:
            #print(list)
            #print(f'Element: {element}')
            if element == 0:
                idx_list.append(idx)
                #print(f'Apended {idx}')
            else: break
            idx += 1
        # Pop the indexes
        retard = 0
        for idx in idx_list:
            list.pop(idx-retard)
            retard += 1
        return list

    def replace_zeros(self, list: list, new_str: str):
        ''' Replace the zeros into the new one given '''
        idx = 0
        for element in list:
            if element == 0: list[idx] = new_str
            else: break
            idx += 1
        return list

    def check_str(self, list: list, character: str):
        ''' Checking if the list only contains the character given, return a bool \n ```True``` if there's only the same thing\n ```False```if not '''
        witness = False
        for element in list: 
            if element == character: witness = True
            else:
                witness = False
                break
        return witness

    def get_len(self, list: list):
        ''' Return a ```int``` which is the list lenght excepting the ```''``` characters '''
        cont = 0
        for element in list:
            if not element == '': cont += 1
        return cont  
        
    def fill_spaces(self, list: list, limit: int, start_idx: int, end_idx: int):
        spaces_amount = limit - len(list)
        # Refill spaces
        for i in range(limit+1):
            #print(i)
            if i < start_idx: list.insert(i, 0)
            elif i > end_idx: 
                if list.insert(i+1, 0) == None:
                    list.append(0)
                else: list.insert(i+1, 0)
        return list
            

if __name__ == '__main__':
    MyDrawer = Drawer('50/8')
    terms = MyDrawer.split_signs()
    #terms = MyDrawer.convert_list_to(terms, float)
    #terms.sort(reverse = True)
    #terms = MyDrawer.convert_list_to(terms, str)
    print("Terms list:", terms) 
    lined = MyDrawer.built_columns(terms)
    print('Lined up columns:',lined)
    results = MyDrawer.draw_division(lined)
    print("\nThe results are:\n",results)

    #print(MyDrawer.fill_spaces([9,2,5,1],5, 2, 4))
    #print(MyDrawer.index_last([5,0,2,6],2))
    #print('\n',[5,0,1,16,0][:-3])
    #print(f'\n{MyDrawer.draw_plus(terms)}\n')
    # lawed = MyDrawer.filter_signs(terms)
    # print("Signs law dict:", lawed)
    # operations_sep = MyDrawer.filter_type_operation()
    # print("Dict with every operation:", operations_sep)

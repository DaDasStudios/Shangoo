import math

# ! Main

def pre_eval(expression: str, format: dict = {}, measure: str = 'deg'):
    ''' Return a ```str``` formated with all the important math symbols '''
    # * Default symbols to use
    main_format = {
        '%':'*1/100',
        '^':'**'
    }
    print(f'Init expression: {expression}')
    # ? Confirm if is there a abs
    if '|' in expression:
        expression = get_val_abs(expression)
    # ? Confirm is is there a log base x
    if 'logy' in expression:
        expression = get_logy(expression)
    # ? Confirm is is there a ln
    if 'ln' in expression:
        expression = get_ln(expression)
    # ? Confirm if is there a log10
    if 'log' in expression:
        expression = get_log(expression)
    # ? Confirm if is there a root
    if '√' in expression:
        expression = getn_root(expression)
    # ? Confirm if is there a factorial
    if '!' in expression: 
        expression = get_factorial(expression)
    # ? Confirm if is there a Combination expression (nCr)
    if 'ncr' in expression.lower():
        expression = get_ncr(expression)
    # ? Confirm if is there a Permutation expression (nPr)
    if 'npr' in expression.lower():
        expression = get_npr(expression)
    # ? Confirm sin⁻¹
    if 'sin⁻¹' in expression:
        expression = get_arcsen(expression, measure)
    # ? Confirm cos⁻¹
    if 'cos⁻¹' in expression:
        expression = get_arcos(expression, measure)
    # ? Confirm tan⁻¹
    if 'tan⁻¹' in expression:
        expression = get_arctan(expression, measure)
    # ? confirm csc
    if 'csc' in expression:
        expression = get_csc(expression, measure)
    # ? Confirm sec
    if 'sec' in expression:
        expression = get_sec(expression, measure)
    # ? Confirm ctg
    if 'ctg' in expression:
        expression = get_ctg(expression, measure)
    # ? Confirm sin
    if 'sin' in expression:
        expression = get_sin(expression, measure)
    # ? Confirm cos
    if 'cos' in expression:
        expression = get_cos(expression, measure)
    # ? Confirm tan
    if 'tan' in expression:
        expression = get_tan(expression, measure)

    keys = main_format.keys() # * Getting the keys is necessary, and it eases us to replace the str
    for symbol in keys:
        if symbol in expression:
            expression = expression.replace(symbol, main_format[symbol])
    # ? Now, we'll do the same with the dict provided by user
    keys_user = format.keys()
    for symbol in keys_user:
        expression = expression.replace(symbol, format[symbol])            

    print(f'Readable expression by eval function: {expression}')
    return expression

# ! Math

def factorial(number: int):
    ''' Return a str with the normal operations in factorial '''
    text = str()
    for i in range(1, abs(number)):
        text += '*{}'.format(i)
    return text

# ! Getters

def get_factorial(expression: str):
    # Get number of factorial
    while True:
        idx = expression.index('!')
        # Find nearest and most possible convertion from str to int
        try:
            for i in reversed(range(idx)): 
                if idx != i:
                    int(expression[i:idx])
                    position_factorial = int(expression[i:idx])
        except ValueError:
            position_factorial = int(expression[i+1:idx])
        # * Replace the ! symbol with the real operation
        #print(position_factorial)
        #print(expression)
        expression = expression.replace('!',factorial(position_factorial),1)
        #print(expression)
        if not '!' in expression: break # * If there'rent more ! symbols, it means the expression is replaced at all
    return expression

def get_val_abs(expression: str):
    ''' Get the abs of a number inside ```| x |``` '''
    indexes = [0,0]
    cont = 0
    index = 0
    for i in expression:
        if cont == 2:
            break
        if '|' == i:
            indexes[cont] = index
            cont += 1
        index += 1
    number = expression[indexes[0]:indexes[1]]
    text_abs = number + '| '
    # todo: we need to call a recursive function to eval the expression inside ||, the calculate abs, replace in original
    # todo: expression and return it, the keep compiling the text
    abs_value = abs(eval(
        pre_eval(text_abs[1:-2],
        {'²':'**2', '³':'**3'}
        )))
    #print(number, text_abs, abs_value)
    expression = expression.replace(text_abs.replace(' ',''), str(abs_value))
    return expression

def getn_root(expression: str):
    ''' Return the ```enesim``` root of any number, the format is the following: ```x√y```'''
    while True:
        expression = expression + ' '
        # * Setting the escentials
        idx = expression.index('√')
        #print(f'√ index is: {idx}')
        inital_idx = idx
        final_idx = idx
        built_text = ''
        exponent_text = ''
        # * Finding the '√' character
        for i in expression[idx+1:]:
            if i == '.': pass
            built_text += i
            try:
                float(built_text)
                final_idx += 1
            except ValueError:
                final_idx += 1
                built_text = built_text[:-1]
                #print(f'Faided in {i}')
                break
        #print(f'Final index is: {final_idx}')
        # * Getting the exponent
        for i in reversed(expression[:idx]):
            if i == '.': pass
            exponent_text += i
            try:
                float(exponent_text)
                inital_idx -= 1
            except ValueError:
                exponent_text = exponent_text[:-1]
                #print(f'Failed in getting exponent in {i}')
                break
            #print(f'Unreversed exp: {exponent_text}')
        #print(f'Initial index is: {inital_idx}')
        # * Getting the base
        exponent_text = reversed_str(exponent_text)
        #print(f'Exponent text is: {exponent_text}')
        if exponent_text == '':
            #print(f'!Exponent text is empty, therefore we assing default value (1/2)')
            exponent = 1/2
        else: 
            exponent = 1/float(exponent_text)
        #print(f'Exponent is: {exponent}')
        #print(f'Built text is: {built_text}')
        # * Replacing the original text into the new one
        result = float(built_text) ** exponent
        expression = expression.replace(expression[inital_idx:final_idx], str(result))
        #print(f'New expression is: {expression}')
        # * Checking if there'rent '√' remaining
        if not "√" in expression: break
    return expression

def get_log(expression: str):
    ''' Return a expression replaced with the result of a ```log``` '''
    while True:
        expression += ' '
        # * Define all escentials
        words = ['l','o','g']
        cont = 0
        idx = expression.find('log')
        final_log_text_idx = idx
        # * Getting the limit of 'log' word
        for i in expression[idx:]:
            if cont == 3:
                break
            if i in words:
                final_log_text_idx += 1
                cont += 1
        #print(f'Main index: {idx}, Final index for log word: {final_log_text_idx}')
        # * Getting the num for operate
        final_idx = final_log_text_idx
        for i in expression[final_log_text_idx:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    # print(f'Failed in {i}')
                    break
        # * Calculating the result
        result = math.log10(float(expression[final_log_text_idx:final_idx]))
        #print('Result = ', result, 'Number for be operating:', expression[final_log_text_idx:final_idx])
        # * Replace in expression
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print('New expression: ',expression)
        # * Validating if there's a new log10
        if not 'log' in expression:
            break
    return expression

def get_logy(expression: str):
    ''' Return a expression replaced with the result of a ``` log base x``` of ```y``` '''
    while True:
        expression += ' '
        # * Define all escentials
        words = ['l','o','g','y']
        cont = 0
        idx =  expression.find('logy')
        final_text_log_idx = idx
        # * Getting the word log
        for i in expression[idx:]:
            if cont == 4:
                break
            if i in words:
                final_text_log_idx += 1
                cont += 1
        #print(f'Main index of log word is: {idx}, final index of word is: {final_text_log_idx}')
        # * Getting the base num
        base_num_idx = final_text_log_idx
        for i in expression[final_text_log_idx:]:
            if i == '.': 
                base_num_idx += 1
            else:
                try: 
                    float(i)
                    base_num_idx += 1
                except ValueError:
                    break
        #print(f"The number's limit index is: {base_num_idx}, the number converted to float is: {float(expression[final_text_log_idx:base_num_idx])}")
        # * Getting the number showed as a power
        final_idx = base_num_idx
        final_idx += 1
        # Finding the ^ in expreession
        power_idx = expression.find('^', base_num_idx)
        # Getting the numbers in power
        for i in expression[power_idx:]:
            if i == '^':
                pass
            elif i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(expression[power_idx+1:final_idx])
        #print(f'The ^ character is in index: {power_idx}, The limit index is: {final_idx} The number in power is: {float(expression[power_idx+1:final_idx])}')
        # * Getting result 
        result = math.log(float(expression[final_text_log_idx:base_num_idx]),float(expression[power_idx+1:final_idx]))
        # * Replace original expression into the new one
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print('Result =', result, 'New expression:', expression)
        if not 'logy' in expression:
            break
    return expression

def get_ln(expression: str):
    ''' Return a expression replaced with the result of a ```ln``` '''
    while True:
        expression += ' '
        # * Define all escentials
        words = ['l','n']
        cont = 0
        idx = expression.index('ln')
        final_ln_text_idx = idx
        # * Getting the limit of 'log' word
        for i in expression[idx:]:
            if cont == 2:
                break
            if i in words:
                final_ln_text_idx += 1
                cont += 1
        #print(f'Main index in: {idx}, Final index in: {final_ln_text_idx}')
        # * Getting the number for being operating
        final_idx = final_ln_text_idx
        for i in expression[final_ln_text_idx:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'The number to work is: {expression[final_ln_text_idx:final_idx]}')
        # * Getting the result with math library
        result = math.log(float(expression[final_ln_text_idx:final_idx]),math.e)
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print('The result is: ', result, 'The new expression is: ', expression)
        if not 'ln' in expression: break
    return expression

def get_ncr(expression: str):
    ''' Return the combination of ```n``` in base ```k``` replaced in the original str '''
    expression = expression.lower()
    while True:
        expression += ' '
        # * Define escentials
        word = ['n','c','r']
        idx = expression.find('ncr')
        final_idx_word = idx
        cont = 0
        # * Getting limit of 'nCr' word
        for i in expression[idx:]:
            if cont == 3:
                break
            if i in word:
                cont += 1
        final_idx_word += cont
        #print(f"Main index: {idx}, Limit word's index: {final_idx_word}")
        # * Getting the numbers
        final_idx = final_idx_word
        for i in expression[final_idx_word:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print('Final index:',final_idx ,'The mumber is:',expression[final_idx_word:final_idx])
        # * Getting the n number
        init_idx = idx
        for i in reversed(expression[:idx]):
            if i == '.':
                init_idx -= 1
            else:
                try:
                    float(i)
                    init_idx -= 1
                except ValueError:
                    break
        #print(f'Init index: {init_idx}, Number in init index: {expression[init_idx:idx]}')
        # * Getting result and replace the word into the new one
        result = math.comb(int(float(expression[init_idx:idx])),int(float(expression[final_idx_word:final_idx])))
        expression = expression.replace(expression[init_idx:final_idx], str(result))
        #print(f'The result is {result} and the new expression is: {expression}')
        if not 'ncr' in expression:
            break
    return expression

def get_npr(expression: str):
    ''' Return the permutation of ```n``` in base ```k``` replaced in the original str'''
    expression = expression.lower()
    while True:
        expression += ' '
        # * Define escentials
        word = ['n','p','r']
        idx = expression.find('npr')
        final_idx_word = idx
        cont = 0
        # * Getting limit of 'nPr' word
        for i in expression[idx:]:
            if cont == 3:
                break
            if i in word:
                cont += 1
        final_idx_word += cont
        #print(f"Main index: {idx}, Limit word's index: {final_idx_word}")
        # * Getting the numbers
        final_idx = final_idx_word
        for i in expression[final_idx_word:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print('Final index:',final_idx ,'The mumber is:',expression[final_idx_word:final_idx])
        # * Getting the n number
        init_idx = idx
        for i in reversed(expression[:idx]):
            if i == '.':
                init_idx -= 1
            else:
                try:
                    float(i)
                    init_idx -= 1
                except ValueError:
                    break
        #print(f'Init index: {init_idx}, Number in init index: {expression[init_idx:idx]}')
        # * Getting result and replace the word into the new one
        result = math.perm(int(float(expression[init_idx:idx])),int(float(expression[final_idx_word:final_idx])))
        expression = expression.replace(expression[init_idx:final_idx], str(result))
        #print(f'The result is {result} and the new expression is: {expression}')
        if not 'npr' in expression:
            break
    return expression

def eng_plus_minus(expression: str, exponent: int):
    ''' Return the result from the forum ```x = num/10^y``` '''
    x = float(expression)
    x = x/10 ** exponent
    return x

def get_sin(expression: str, measure: str):
    ''' Return the expression updated with the ```sin```, it receives radians '''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'sin')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = sen(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'sin' in expression.lower():
            break
    return expression

def get_cos(expression: str, measure: str):
    ''' Return the expression updated with the ```cos```, it receives radians '''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'cos')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = cos(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'cos' in expression.lower():
            break
    return expression

def get_tan(expression: str, measure: str):
    ''' Return the expression updated with the ```tan```, it receives radians '''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'tan')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = tan(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'tan' in expression.lower():
            break
    return expression

def get_csc(expression: str, measure: str):
    ''' Return the expression updated with the ```csc``` it means ```1/sec``` of a radian'''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'csc')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = sen(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(1/result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'csc' in expression.lower():
            break
    return expression

def get_sec(expression: str, measure: str):
    ''' Return the expression updated with the ```sec``` it means ```1/cos``` of a radian'''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'sec')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = cos(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(1/result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'sec' in expression.lower():
            break
    return expression
    
def get_ctg(expression: str, measure: str):
    ''' Return the expression updated with the ```ctg``` it means ```1/tan``` of a radian'''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'ctg')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = tan(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(1/result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'ctg' in expression.lower():
            break
    return expression

def get_arcsen(expression: str, measure: str):
    ''' Return the ```sen⁻¹``` of a number, range ```-1:1``` replaced inside the expression'''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'sin⁻¹')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        #print(final_idx_sin)
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = arcsen(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'sin⁻¹' in expression:
            break
    return expression

def get_arcos(expression: str, measure: str):
    ''' Return the ```cos⁻¹``` of a number, range ```-1:1``` replaced inside the expression'''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'cos⁻¹')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = arccos(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'cos⁻¹' in expression.lower():
            break
    return expression
    
def get_arctan(expression: str, measure: str):
    ''' Return the ```tan⁻¹``` of a number, range ```-1:1``` replaced inside the expression'''
    while True:
        expression += ' '
        # * Gettin main indexes
        main_indexes = find_word(expression, 'tan⁻¹')
        # * Define escentials
        idx = main_indexes[0]
        final_idx_sin = main_indexes[1]
        final_idx = final_idx_sin
        # * Getting number
        for i in expression[final_idx_sin:]:
            if i == '.':
                final_idx += 1
            else:
                try:
                    float(i)
                    final_idx += 1
                except ValueError:
                    break
        #print(f'Number: {expression[final_idx_sin:final_idx]}')
        # * Getting result
        result = arctan(float(expression[final_idx_sin:final_idx]), measure)
        expression = expression.replace(expression[idx:final_idx], str(result))
        #print(f'Result is: {result}, New expression: {expression}')
        if not 'tan⁻¹' in expression.lower():
            break
    return expression

# ! Trigonometry

''' All of these depend of the measure that is selected, and they return the function what you've choiced '''
def sen(unit: float, measure: str = 'deg'): 
    converted = any_to_rad(unit, measure)
    result = math.sin(converted)
    return result

def cos(unit: float, measure: str = 'deg'): 
    converted = any_to_rad(unit, measure)
    result = math.cos(converted)
    return result

def tan(unit: float, measure: str = 'deg'): 
    converted = any_to_rad(unit, measure)
    result = math.tan(converted)
    return result

def arcsen(unit: float, measure: str = 'deg'): 
    x = math.asin(unit)
    x = convert_all_to_any(x, measure)
    return x

def arccos(unit: float, measure: str = 'deg'): 
    x = math.acos(unit)
    x = convert_all_to_any(x, measure)
    return x

def arctan(unit: float, measure: str = 'deg'): 
    x = math.atan(unit)
    x = convert_all_to_any(x, measure)
    return x

''' Depending of this variable the angle measure will change between, rad, gra, cen '''

# ! Convertions 

# ? The objetive is convert all into radians
def any_to_rad(unit: float, measure: str):
    ''' It can receive, deg, rad or cen, so depeding of it, it converts them into radians '''
    #print("we're converting into radians, unit:", unit, " You're working with:", measure)
    if measure == 'cen': result = math.pi*unit / 200
    elif measure == 'rad': result = unit
    elif measure == 'deg': result = math.pi*unit / 180
    #print(f"Num converted to radians is: {result}")
    return result

def convert_all_to_any(unit: float, measure: str):
    if measure == 'deg':
        x = math.degrees(unit)
    elif measure == 'rad':
        x = math.radians(unit)
    elif measure == 'cen':
        x = unit * 200 / math.pi
    return x

# ! Strings

''' All related to strings '''
def reversed_str(text: str):
    ''' Return a reversed string '''
    serie = ''
    for i in reversed(text):
        serie += i
    return serie 

def find_word(expression: str, word: str):
    ''' Return the final and start index of a expression '''
    expression += ' '
    word_list = [letter for letter in word]
    idx = expression.find(word)
    final_idx_word = idx
    cont = 0
    len_word = len(word_list)
    for i in expression[idx:]:
        if cont == len_word: break
        if i in word:
            cont += 1
    final_idx_word += cont
    #print(f'Start index of <{word}> is: {idx}, Final index is: {final_idx_word}')
    return idx, final_idx_word

# ! Lists

def reversed_list(list: list):
    ''' Return a new inversed list '''
    new_list = ['' for x in range(len(list))]
    idx = -1
    for i in list:
        new_list[idx] = i
        idx -= 1
    return new_list

  
if __name__ == '__main__':
    formated_expression = pre_eval('tan⁻¹0.886+sin⁻¹0.5',{'²':'**2', '³':'**3'}, 'deg')
    print(f'Result = {eval(formated_expression)}')






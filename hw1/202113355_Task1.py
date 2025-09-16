# get two inputs and save them into m, n as string
# m, n = input().split()
debug_mode = True


def multiply_single_digit(x: str, y: str) -> tuple[str, str]:
    """
    Multiply two single-digit as str and split the result into...

    - carry: the quotient when divided by 10 as str
    - remainder : the remainder when divided by 10 as str

    Args:
        x (int): first digit (0-9)
        y (int): second digit (0-9)

    Returns:
        tuple: A tuple (carry, remainder)
            carry (str): (the result of multiplication) // 10
            remainder (str): (the result of multiplication) % 10
    """

    x_int, y_int = map(int, [x, y])

    result = x_int * y_int

    carry = result // 10
    remainder = result % 10

    return (str(carry), str(remainder))

def add_single_digit(x: str, y: str) -> tuple[str, str]:
    """
    Add two single-digit as str and split the result into...

    - carry: the quotient when divided by 10 as str
    - remainder : the remainder when divided by 10 as str

    Args:
        x (str): first digit (0-9)
        y (str): second digit (0-9)

    Returns:
        tuple: A tuple (carry, remainder)
            carry (str): (the result of addition) // 10
            remainder (str): (the result of addition) % 10
    """
    
    x_int, y_int = map(int, [x, y])

    if debug_mode:
        print(f"    add_single_digit: current task is {x_int} + {y_int}")

    result = x_int + y_int

    carry = result // 10
    remainder = result % 10

    if debug_mode:
        print(f"    add_single_digit: we got carry: {carry} remainder: {remainder}")

    return (str(carry), str(remainder))

def add_integers(m: str, n: str) -> str:
    """
    Add two integers and return the result string
    
    For example, add_integers("123", "123") returns "246"

    Args:
        m (str): first string of integer 
        n (str): second string of integer 

    Returns:
        str: the string of result of the addition
    """
    # put the longer digits string into m, shorter on into n
    if len(n) > len(m):
        m, n = n, m

    # reverse strings of m, n
    m = m[::-1]
    n = n[::-1]

    m += "0"

    result = ""

    current_carry = "0"

    for i in range(len(n)):
        if debug_mode:
            print(f"current task is {m[i]} + {n[i]} when the current carry is {current_carry}")
        current_carry, s = add_single_digit(n[i], current_carry)
        tmp, s = add_single_digit(m[i], s)

        if current_carry == "1" or tmp == "1" :
            current_carry = "1"
        
        result += s
    
    
    for i in range(len(n), len(m)):
        current_carry, s = add_single_digit(m[i], current_carry)
        result += s

    result = result[::-1]

    # remove "0" from the beginning of the string if exist
    result = result.lstrip("0")
    
    if debug_mode:
            print(f"add_integers: we got {result}")

    return result

def multiply_digit_string(single_digit: str, digits: str) -> str:
    """
    Multiply one digit integer string and multiple digits integer string and return the result of the multiplication

    For example, multiply_digit_string("2", "123") returns "246"

    Arg:
        single_digit (str): the string composed of only one digit
        digits (str): the string composed of multiple digit

    Returns:
        str: the string result of the multiplication
    """
    digits = digits[::-1]
    digits += "0"
    current_carry = "0"

    result = ""

    for i in range(len(digits)):
        c_m, s = multiply_single_digit(single_digit, digits[i])
        c, tmp = add_single_digit(s, current_carry)
        _, current_carry = add_single_digit(c_m, c)
        result += tmp

    result = result[::-1]
    result = result.lstrip("0")
    
    if debug_mode:
            print(f"multiply_digit_string: we got {result}")
    return result


def basic_multiply(m, n):
    # put the longer digits string into m, shorter on into n
    if len(n) > len(m):
        m, n = n, m

    padding = ""
    result = "0"

    n = n[::-1]

    print(f"m : {m}, n : {n[::-1]}")

    for single_digit in n:
        tmp = multiply_digit_string(single_digit, m)         
        tt = tmp
        tmp += padding
        result = add_integers(result, tmp)
        padding += "0"

        print(f"m : {m}")
        print(f"single digit : {single_digit}")
        print(f"single digit * m  : {tt}")
        
        if int(single_digit) * int(m) != int(tt):
            print(f"it shulde be {int(single_digit) * int(m)}")
            print("WRONG!!!!")
            break


        print(f"result = {result}")

        

        print("-"*50)

    print(result)

basic_multiply("123456789123456789", "987654321987654321")

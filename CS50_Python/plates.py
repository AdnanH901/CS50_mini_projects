def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    '''
    Returns a boolean statement under the basis of a string being a "Vanity plate".
    The axioms for a vanity plate are:

    - All vanity plates must start with at least two letters # [DONE]

    - Vanity plates may contain a maximum of 6 characters (letters or numbers)
      and a minimum of 2 characters # [DONE]

    - Numbers cannot be used in the middle of a plate; they must come at the end.
      For example, AAA222 would be an acceptable vanity plate; AAA22A would not be
      acceptable.

    - The first number used cannot be a "0" [DONE] (via first_num function)

    - No periods, spaces, or punctuation marks are allowed # [DONE] (via punc_check function)
    '''
    # Create a function dealing with each of these cases seperatley.
    return 2 <= len(plate) <= 6 and plate[0].isalpha() and plate[1].isalpha() and middle_num_check(plate) and first_num(plate)[0] != "0" and punc_check(plate)

def punc_check(string):
    '''
    Checks if a given character is or is not a punctuatuon mark.
    '''
    punc = [ ";" , "," , ":" , "?" , "!" , "." , "_" ,
              '"' , "'" , "-" , "|" , "(" , ")" , "*" ,
              "[" , "]" , "{" , "}" , "/" , "&" , "\\" ]
    for char in string:
        for i in range(len(string)):
            if char == punc[i]:
                return False
    return True

def first_num(string):
    '''
    Checks, from left to right, what number is the first number in the string.
    '''
    for char in range(len(string)):
        if string[char].isnumeric():
            return [string[char],char]
    # To deal with the case when there is no nuber in the string.
    return [None,0]

def middle_num_check(string):
    # To deal with the case when there is no number in the string.
    num_string = None
    if first_num(string)[0] != None:
        num_string = string[first_num(string)[1]:len(string)]
    return num_string == None or num_string.isnumeric()
main()

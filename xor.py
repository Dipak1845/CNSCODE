def xor_and_with_127(input_string): 
    result_and = "" 
    result_xor = ""
    
    for char in input_string: 
        result_and += chr(ord(char) & 127) 
    print("After bitwise AND with 127: ", result_and)
    
    for char in input_string: 
        result_xor += chr(ord(char) ^ 127) 
    print("After bitwise XOR with 127: ", result_xor)
    
input_string = "\HelloWorld" 
print("Original String:", input_string) 
xor_and_with_127(input_string)

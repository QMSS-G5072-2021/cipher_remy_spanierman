def cipher(text, shift, encrypt=True):
    
    '''
    Description: The cipher uses inputs of string data and shifts the letters within the alphabet by the 
    designated shift input. Thus it encrypts strings so they no longer appear in their original form. 
    
    Inputs:
        Text: String data to be ciphered
        Shift: The number of positions in the alphabet to shift (positive to the right, negative to the left)
        Encrypt: Boolean True/False to determine whether the shift input is activated for the string
    Output:    
        Returns string that is shifted respective amount of letters denoted with shift input when Encrypt is True.
    
    Use Case Example:    
        Input: cipher('Hello',5,encrypt=True)
        Output: 'Mjqqt'
        Input: cipher('Hello',5,encrypt=False)
        Output: 'Hello'
    '''    
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
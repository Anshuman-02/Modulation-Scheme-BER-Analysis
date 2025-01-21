def lzw_encode(message):
    dictionary = {chr(i): i for i in range(256)}
    p = ""
    result = []
    for c in message:
        pc = p + c
        if pc in dictionary:
            p = pc
        else:
            result.append(dictionary[p])
            dictionary[pc] = len(dictionary)
            p = c
    if p:
        result.append(dictionary[p])
    return result

def lzw_decode(encoded_message):
    dictionary = {i: chr(i) for i in range(256)}
    result = chr(encoded_message[0])
    s = result
    for k in encoded_message[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == len(dictionary):
            entry = s + s[0]
        else:
            raise ValueError("Bad compressed k: %s" % k)
        result += entry
        dictionary[len(dictionary)] = s + entry[0]
        s = entry
    return result

# Get input from user
message = input("Enter a message to encode: ")

# Encode and decode the message
encoded_message = lzw_encode(message)
print("Encoded:", encoded_message)
decoded_message = lzw_decode(encoded_message)
print("Decoded:", decoded_message)

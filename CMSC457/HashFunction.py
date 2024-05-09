import math

class HashFunction():
    
    def BaseHash(input):

        char_arr = list(input)

        hash_val = 0

        prime_arr = [1,2,3,5,7,11,13,17,23,29]

        for i in range(len(char_arr)):
            val = ord(char_arr[i])
            hash_val += val * prime_arr[i % 10] * pow(10,i)

        result = ""

        while len(result) < 64:
            result += hex(hash_val)[2:]
        
        result = result[0:64]
                        
        return result
    
    if __name__ == "__main__":
        print(BaseHash("This is the Message I want to send"))


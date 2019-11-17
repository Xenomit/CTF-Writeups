import binascii
import ctypes
from random import randint

alphabet = list("ABCDEFGHJKLMNPQRSTUVWXYZ23456789")

def func_5(ptr_to_or_area):

    for i in reversed(range(1, 5)):
        dl = ptr_to_or_area[i - 1]; 
        bl = ptr_to_or_area[i];

        ptr_to_or_area[i] = ((dl >> 3) | (bl << 5)) & 0xff;
    
    ptr_to_or_area[0] = (ptr_to_or_area[0] << 5) & 0xff
    return ptr_to_or_area



def get_position_in_alphabet(c):
    global alphabet
    return alphabet.index(c)


def clean_serial_func(serial):
    return serial.replace("-", "")
    

def check_serial(clean_serial, len_serial):
    final_results = []

    for i in range(2):
        part_of_serial = clean_serial[i*8:i*8+8][::-1]
        res_func_5 = [0x00] * 12

        for c in part_of_serial:
            res_func_5 = func_5(res_func_5)
            char_index = get_position_in_alphabet(c)
            res_func_5[0] = res_func_5[0] | char_index
        
        final_results += res_func_5

    final_results = [x for x in final_results if x != 0x0]
    return final_results + [0x00]*4


def checksum(final_values):
    counter = 0

    for i in range(8):
        counter = counter * 1664117991;
        counter = ctypes.c_uint(final_values[i] - counter).value;

    rest = int(counter % 0xfff1)
    
    return rest ^ 0x317



def is_valid(serial):   
    clean_serial = ''

    clean_serial = clean_serial_func(serial);
    final_values = check_serial(clean_serial, len(clean_serial));

    checksum(final_values)

    last_bytes = int(binascii.hexlify(bytearray(final_values[8:][::-1])), 16)
    check = checksum(final_values)

    if checksum(final_values) == last_bytes:
        print ('#### VALID SERIAL ####')
        return True

    return False
    

def gen_random_serial():
    serial = ''

    for i in range(16):
        if i % 4 == 0 and i != 0:
            serial += '-'
            serial += alphabet[randint(0, len(alphabet)-1)]
        else:
            serial += alphabet[randint(0, len(alphabet)-1)]        

    return serial


def main():
    global alphabet

    #serial = "ABCD-EFGH-JKLM-NPQR" # Wrong example
    #serial = "4UYU-TJY9-2BW2-98Y7" # Correct example
    print("""  _     ___  _____  ___   ___  ___  ___  __  __                        _  _     _  __                            
 | |   / _ \|_   _|| _ \ |_ _||_ _||_ _| \ \/ / ___  _ _   ___  _ __  (_)| |_  | |/ / ___  _  _  __ _  ___  _ _  
 | |__| (_) | | |  |   /  | |  | |  | |   >  < / -_)| ' \ / _ \| '  \ | ||  _| | ' < / -_)| || |/ _` |/ -_)| ' \ 
 |____|\___/  |_|  |_|_\ |___||___||___| /_/\_\ \___||_||_\___/|_|_|_||_| \__| |_|\_\\___| \_, |\__, |\___||_||_|
                                                                                           |__/ |___/            
""")
    
    serial = gen_random_serial()

    while not is_valid(serial):        
        serial = gen_random_serial()
        print(serial, end="\r")

    print(serial)


if __name__ == '__main__':
    main()

from sys import stdin

addr = 0
string_list = []
count = 0
var_dict = {}
label_dict = {}


def process():
    for i in string_list:
        arr = i.split()
        check(arr)


reg_dict = {"R0": "000",
            "R1": "001",
            "R2": "010",
            "R3": "011",
            "R4": "100",
            "R5": "101",
            "R6": "110",
            "FLAGS": "111"}
inst_dict = {"add": "00000",
             "sub": "00001",
             "movI": "00010",
             "movR": "00011",
             "ld": "00100",
             "st": "00101",
             "mul": "00110",
             "div": "00111",
             "rs": "01000",
             "ls": "01001",
             "xor": "01010",
             "or": "01011",
             "and": "01100",
             "not": "01101",
             "cmp": "01110",
             "jmp": "01111",
             "jlt": "10000",
             "jgt": "10001",
             "je": "10010",
             "hlt": "10011"}


def check(arr):
    result = ""
    length = len(arr)

    if length == 2:
        if arr[0] in inst_dict:  # Type E
            result = result + inst_dict[arr[0]] + label_dict[arr[1]]

    elif length == 3:
        if arr[0] == "mov" and arr[2][0] == "$" and arr[1] in reg_dict:  # Type B
            result += "00010" + reg_dict[arr[1]] + f'{int(arr[2][1:]):08b}'

        elif arr[0] in inst_dict and arr[2][0] == "$" and arr[1] in reg_dict:  # Type B
            result += inst_dict[arr[0]] + reg_dict[arr[1]] + f'{int(arr[2][1:]):08b}'

        elif arr[0] in inst_dict and arr[2] in reg_dict and arr[1] in reg_dict:  # Type C
            result += inst_dict[arr[0]] + "00000" + reg_dict[arr[1]] + reg_dict[arr[2]]

        elif arr[0] in inst_dict and arr[1] in reg_dict and arr[2] in label_dict:
            result += inst_dict[arr[0]] + reg_dict[arr[1]] + f'{label_dict[arr[2]]:08b}'


    elif length == 4:
        if arr[0] in inst_dict and arr[1] in reg_dict and arr[2] in reg_dict:  # Type A
            result += inst_dict[arr[0]] + "00" + reg_dict[arr[1]] + reg_dict[arr[2]] + reg_dict[arr[3]]

    elif length == 1:
        if arr[0] in inst_dict:
            result += inst_dict[arr[0]]+"0"*11


def main():
    for line in stdin:
        if line != "":  # If empty string is read then stop the loop
            ln = line.strip()
            string_list.append(ln)
            Ln = ln.split()

            if Ln[0] == "var":
                global count
                count += 1
                var_dict[Ln[1]] = 0


            # label:

            elif Ln[0][-1] == ":":
                global addr
                count += 1
                label_dict[Ln[0][0:-1]] = addr
                addr += 1


def substituting_var_address():
    c = 0
    for i in var_dict:
        c += 1
        var_dict[i] = addr + c


if __name__ == "_main__":
    main()
    substituting_var_address()
    process()  # perform some operation(s) on given string

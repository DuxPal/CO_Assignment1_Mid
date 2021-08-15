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
v = []
addr = 0
c = 0


def check(arr):
    result = ""
    leng = len(arr)
    global addr
    global c
    #   A=4     B=3       c=3       D =3      E=2      F=1

    if leng == 1:
        if arr[0] in inst_dict:
            result = result + inst_dict[arr[0]] + "00000000000"
            addr += 1
            print(result)
            return

    elif leng == 2:

        if arr[0] == "var":
            v.append(arr[1])
            c = c + 1

        elif arr[0] in inst_dict:         # Type E
            result = result + inst_dict[arr[0]]

    elif leng == 3:
        if arr[0] in inst_dict:  # Type D,C,B
            val = inst_dict[arr[0]]
            result = result + val

            if arr[1] and arr[2] in reg_dict:  # Type C
                result = result + "00000" + reg_dict[arr[1]] + reg_dict[arr[2]]

            elif arr[1] in reg_dict:
                result += reg_dict[arr[1]]
                #
                #
                #

    elif leng == 4:
        if arr[0] in inst_dict:  # Type A
            result = result + inst_dict[arr[0]]

            # value(binary string) of register
            if arr[1] in reg_dict:
                result = result + "00" + reg_dict[arr[1]]

                if arr[2] in reg_dict:
                    result = result + reg_dict[arr[2]]

                    if arr[3] in reg_dict:
                        result = result + reg_dict[arr[3]]
                        print(result)
                        return


def main():
    from sys import stdin

    for line in stdin:
        if line == '':  # If empty string is read then stop the loop
            break
        process(line)   # perform some operation(s) on given string


def process(line):
    ln = line.split()
    check(ln)
    return

if __name__ == "__main":
    main()

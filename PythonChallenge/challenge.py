# challenge 00
print(2**38)

# challenge 01
input_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
c='a'
chr(ord(c))

# challenge 02

# challenge 03
f3 = open("ch3.txt", 'r')
input_str = f3.read()
#print(input_str)
input_list = list(input_str)
output_list = []
stack = []
f_buf = []
b_buf = []
for chr in input_list:
    if 64 < ord(chr) < 91:
        f_buf.append(chr)
        if len(stack) > 3:
            stack.clear()
            break
    elif 96 < ord(chr) < 123:
        stack.append(chr)

print(output_list)


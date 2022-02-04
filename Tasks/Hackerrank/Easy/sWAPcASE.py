# # sWAP cASE
# # ------------------------------------------------------------------------------



def swap_case(s):
    new_s = ''
    for i in range(len(s)):
        if s[i] == s[i].upper():
            new_s += s[i].lower()
        else:
            new_s += s[i].upper()
    s = new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
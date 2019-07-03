import unicodedata
def len_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def echo_sd(text):
    print("__人",end="")
    display_len = len_count(text)/2)-1
    for i in range(display_len):
        print("人",end="")

    print("人__")
    print("＞ " + text + " ＜")
    print("￣Y^", end="")
    
    for i in range(display_len):
        print("Y^",end="")
    print("Y￣")

t = input("Input : ")
echo_sd(t)

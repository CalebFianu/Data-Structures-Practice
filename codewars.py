def narcissistic( value ):
    # Code away
    new_val = [int(a) for a in str(value)]
    
    sum = 0
    for i in range(len(new_val)):
        sum = sum + (int(new_val[i])**len(new_val))
    # return sum

    if sum == value:
        return True
    elif sum != value:
        return False

def to_jaden_case(string):
    # ...
    new_str = string.split(" ")
    newer = []
    for char in new_str:
        newer.append(char.title())
    
    print(' '.join([str(item) for item in newer]))


def maskify(cc):
    for i in range(len(cc)):
        aa = cc.replace(cc[:4],'#')
        space = (len(cc) - 3)*"#"
    return str(space) + aa

def high_and_low(numbers):
    
    new_list = numbers.split(" ")
    max = int(new_list[0])
    min = int(new_list[0])
    for i in range(len(new_list)):
        if int(new_list[i]) > max:
            max = int(new_list[i])
    
    
    for i in range(len(new_list)):
        if int(new_list[i]) < min:
            min = int(new_list[i])
    
    return str(max) + " " + str(min)

print(high_and_low("1 3 2"))

# print(maskify("fAIb('-PA>8NCCmz"))
# print(to_jaden_case("new one"))
#print(narcissistic(371))
def encyrption(input_value):
    import random
    import string
    import textwrap

    # global result
    output = textwrap.wrap(input_value, 1)
    len_output = len(output)
    len_len_output = len(str(len_output))
    index = int(119/len_output)
    aralık = index
    len_aralık = len(str(aralık))
    letters = string.ascii_letters + string.digits +string.digits +string.punctuation
    random_str = ''.join(random.choice(letters) for i in range(120))
    for newstring in output: 
        random_str = random_str[:index] + newstring + random_str[index + 1:]
        index += aralık
    random_str = str(len_output).rjust(2,"&") + str(random_str)[10] + str(len_len_output) + str(random_str) + str(aralık).rjust(2,"%") + str(random_str)[10] + str(len_aralık)
    result = random_str
    return result

def decyrption(result):
    # global user_pw
    password = []
    first_part = result[:4]
    if not "&" in first_part:
        pw_lenght = first_part[:2]
    else:
        pw_lenght = first_part[1]
    pw_lenght = int(pw_lenght)
    second_part = result[-4:]
    if not "%" in second_part:
        pw_range = second_part[:2]
    else:
        pw_range = second_part[1]
    pw_range = int(pw_range)
    str_part = result[4:-4]
    st_range = pw_range
    for pw in range(pw_lenght):
        password.append(str_part[pw_range])
        pw_range+=st_range
    user_pw = "".join(password)
    return user_pw

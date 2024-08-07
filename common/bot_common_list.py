


async def revers_text(data) -> str:

    step = 28
    line = data['input_text']
    new_str = ''
    my_str = ''
    last_word = ''
    num_simbol_in_line = 0
    count_simbol = 0
    line_number = 1
    for word in line.split():
        if line_number % 2:
            num_simbol_in_line = count_simbol + len(word)
            if num_simbol_in_line < step:
                my_str += ' ' + word
                count_simbol += len(word)
            else:
                last_word = word
                my_str += '\n'
                line_number += 1
                num_simbol_in_line = 0
                count_simbol = len(word)
        else:
            num_simbol_in_line = count_simbol + len(word)
            if num_simbol_in_line < step:
                last_word += ' ' + word
                count_simbol += len(word)
            else:
                new_str = last_word[::-1]
                my_str += new_str + '\n' + word
                line_number += 1
                num_simbol_in_line = 0
                count_simbol = len(word)
    return my_str
def grep(pattern, flags, files):

    pattern_list = []
    line = 0

    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as file:

            for counter, line in enumerate(file, start=1):

                match_pattern = pattern
                match_line = line

                if '-i' in flags:
                    match_line = line.lower()
                    match_pattern = pattern.lower()

                clean_line = match_line.strip('\n')

                is_match = match_pattern in clean_line

                if '-x' in flags:
                    is_match = (match_pattern == clean_line)

                if '-v' in flags:
                    is_match = not is_match

                if is_match == True:

                    if '-l' in flags:
                        pattern_list.append(f'{file_name}\n')
                        break

                    if '-n' in flags:
                        line = f'{counter}:{line}'


                    if len(files) > 1:
                        line = f'{file_name}:{line}'

                    pattern_list.append(line)

    return "".join(pattern_list)

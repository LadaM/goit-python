def solve_riddle(riddle, word_length, start_letter, reverse=False):
    # normalizing the given problem to not special-case it later
    problem = riddle[::-1] if reverse else riddle

    for i in range(len(problem)):
        if problem[i] == start_letter:
            return problem[i : (i + word_length)]    

    # if no word was found, return an empty string
    return ''

print(solve_riddle('mi1rewopret', 5, 'p', True))
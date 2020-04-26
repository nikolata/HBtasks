def possible_moves_finder(lilys):
    possible_moves = []
    for index, frog in enumerate(lilys):
        direction = 0
        if (frog == '<'):
            direction = -1
        elif (frog == '>'):
            direction = 1
        jump_over_frog = index + (direction * 2)
        small_jump = index + (direction)

        if (direction == 0):
            continue

        # small jump cases
        if small_jump >= 0 and small_jump < len(lilys) and lilys[small_jump] == '_':
            temp_lilys = list(lilys)
            temp_lilys[index] = '_'
            if (direction == -1):
                temp_lilys[small_jump] = '<'
            elif (direction == 1):
                temp_lilys[small_jump] = '>'
            possible_moves.append(temp_lilys)

        # big leap cases
        if jump_over_frog >= 0 and jump_over_frog < len(lilys) and lilys[jump_over_frog] == '_':
            temp_lilys = list(lilys)
            temp_lilys[index] = '_'
            if (direction == -1):
                temp_lilys[jump_over_frog] = '<'
            elif (direction == 1):
                temp_lilys[jump_over_frog] = '>'
            possible_moves.append(temp_lilys)

    return possible_moves


def recursion(final_lilys, temp, all):
    if temp[-1][-1] != final_lilys:
        next_move = []
        for lily in temp:
            legal_moves = possible_moves_finder(lily[-1])
            for move in legal_moves:
                temptemp = list(lily)
                temptemp.append(move)
                next_move.append(temptemp)
                if (move == final_lilys):
                    break
        temp = next_move
        all.append(temp)
        recursion(final_lilys, temp, all)
    return all[-1][-1]


def play_game(frogs_count):
    start = list('>' * (frogs_count // 2) + '_' + '<' * (frogs_count // 2))
    final = list('<' * (frogs_count // 2) + '_' + '>' * (frogs_count // 2))
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(recursion(final, [[start]], [[[]]]))))


if __name__ == '__main__':
    play_game(6)

'''
def test(cur_lilys, final, path, ind_move, visited):
    if cur_lilys == final:
        return path
    if path not in visited:
        if ind_move + 1 == len(possible_moves_finder(cur_lilys)) and cur_lilys != final:
            test(path[-2], final, path[:-1], ind_move + 1, visited)
        possible_moves = possible_moves_finder(cur_lilys)
        if len(possible_moves) == 1 and possible_moves[0] != final or possible_moves == []:
            path.append(possible_moves[0])
            visited.append(path)
            test(path[-2], final, path[:-1], ind_move + 1, visited)
        path.append(cur_lilys)
        test(possible_moves[ind_move], final, path, ind_move + 1, visited)
    else:
        test(path[-2], final, path[:-1], ind_move + 1, visited)
'''
from copy import deepcopy

def board_fill(lock):
    N = len(lock)
    for i in range(N):
        for j in range(N):
            if lock[i][j] != 1:
                return False
    return True

def check(key, lock):
    M = len(key)
    N = len(lock)
    for i in range(-M+1,N):
        for j in range(-M+1,N):
            result = deepcopy(lock)
            for m_i in range(0, M):
                for m_j in range(0, M):
                    if 0 <= i+m_i < N and 0 <= j+m_j < N:
                        result[i+m_i][j+m_j] = key[m_i][m_j] + lock[i+m_i][j+m_j]

            if board_fill(result):
                return True
    
    return False

def solution(key, lock):
    key_rot = []
    key_rot.append(key)
    for i in range(3):
        new = list(zip(*key_rot[-1][::-1]))
        key_rot.append(new)
    
    for i in range(4):
        possible = check(key_rot[i], lock)
        if possible:
            return True

    return False

q1 = [[[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]]
print(solution(*q1))
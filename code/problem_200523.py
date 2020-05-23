# M.D

def pre(strs):
    mylist = list(zip(*strs))
    cnt = 0
    for m in mylist:
        if len(set(list(m))) == 1:
            cnt += 1
        else:
            break
    answer = strs[0][:cnt]
    return answer

import numpy as np
import math
def monster(x, y, r, d, target) :
    answer = 0
    current_pos = np.array([0, 0])
    mouse_click = np.array([x, y])
    mouse_vector = mouse_click - current_pos

    for [a, b] in target :
        monster_pos = np.array([a, b])
        monster_vector = monster_pos - current_pos
        cosine_angle = np.dot(mouse_vector, monster_vector) / (np.linalg.norm(mouse_vector) * np.linalg.norm(monster_vector))

        angle = np.arccos(cosine_angle)
        inner_angle = np.degrees((angle))

        distance = math.sqrt(a*a + b*b)

        if inner_angle < d and distance < r:
            answer += 1
    
    return answer


def pang(board):
    answer = 0
    return answer
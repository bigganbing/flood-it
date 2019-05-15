import copy

fx = [0, 0, 1, -1]
fy = [1, -1, 0, 0]
total_colors = 6
list_vis = []

# 返回当前还有多少种颜色未被着色
def check_uncoloured():
    global total_colors, N, vis, map
    uncoloured = 0
    judge = [0]*10
    for i in range(N):
        for k in range(N):
            if vis[i][k] != 1 and judge[map[i][k]] == 0:
                uncoloured += 1
                judge[map[i][k]] = 1
    return uncoloured

def paint_map(c):
    for i in range(N):
        for k in range(N):
            if vis[i][k] == 1:
                map[i][k] = c

# 对点(x,y)周边，颜色为c的联通区域中的点染色
def paint(x, y, c):
    global total_colors, N, vis, map
    vis[x][y] = 1
    paint_map(c)
    for i in range(4):
        xx = x + fx[i]
        yy = y + fy[i]
        if xx<0 or yy<0 or xx>N-1 or yy>N-1 or vis[xx][yy]==1:    # 越界或者已经着色，continue
            continue
        if map[xx][yy] == c:          # 颜色相同，继续着色
            paint(xx, yy, c)
        else:                       # 颜色不同，纳入待扩张集合
            vis[xx][yy] = 2

def idas(dep, lim_dep):
    global total_colors, N, vis, map, list_vis

    list_vis.append(copy.deepcopy(map))
    # list_vis.insert(0, vis)

    if dep == lim_dep:
        if check_uncoloured() == 0:
            return 1
        else:
            return 0
    if dep + check_uncoloured() > lim_dep:
        return 0
    for c in range(total_colors):
        temp_vis = copy.deepcopy(vis)
        temp_map = copy.deepcopy(map)
        flag = 0
        for i in range(N):
            for k in range(N):
                if map[i][k] == c and vis[i][k] == 2:
                    paint(i, k, c)
                    flag = 1
        if flag==0:
            continue
        if idas(dep+1, lim_dep) == 1:
            return 1
        vis = copy.deepcopy(temp_vis)
        map = copy.deepcopy(temp_map)

    list_vis.pop()

    return 0

def main(n, matrix_str):
    global total_colors, N, vis, map, list_vis

    vis = [[0] * 10 for _ in range(10)]  # 着色标记， 0表示未着色，1表示已经着色，2表示待着色
    map = [[0] * 10 for _ in range(10)]  # 原颜色矩阵
    list_vis = []

    N = int(n)
    matrix = matrix_str.strip().split()

    # list_vis.append(copy.deepcopy(vis))

    if N > 10 or N < 2:
        return 'N input error! Please make sure 2 <= N <= 10.'

    if len(matrix) != N*N:
        return 'Matrix input error! Please make sure the matrix you enter is N*N.'

    l = 0
    for i in range(N):
        for k in range(N):
            if int(matrix[l])>=0 and int(matrix[l]) <= 5:
                map[i][k] = int(matrix[l])
                l += 1
            else:
                return 'Color in the matrix you enter error! Please make sure the color you enter is greater than or equal to 0 and less than or equal to 5.'

    paint(0, 0, map[0][0])

    # list_vis.append(copy.deepcopy(vis))

    for lim_dep in range(check_uncoloured(), N*N):
        if idas(0, lim_dep)==1:

            list_vis_temp = []
            for c in list_vis:
                if not c in list_vis_temp:
                    list_vis_temp.append(c)
            list_vis = copy.deepcopy(list_vis_temp)

            result_str = 'The game board you input:'
            result_str += '\n'

            for count, q in enumerate(list_vis):
                if count == 0:
                    for i in range(N):
                        for k in range(N):
                            result_str += str(q[i][k]) + ' '
                        result_str += '\n'
                    result_str += '\n\n'

                    result_str += 'The minimal step : ' + str(lim_dep)
                    result_str += '\n\n'

                if count > 0:
                    result_str += 'Step ' + str(count) + '\n'
                    for i in range(N):
                        for k in range(N):
                            result_str = result_str + str(q[i][k]) + ' '
                        result_str += '\n'
                result_str += '\n'
            # print(result_str)
            return result_str


# main('3', '0 1 2 1 1 2 2 2 1')
# main('2', '0 1 2 0')








import copy
import sys

filename = 'vstup.txt'
file = open(filename, 'r')
filecontent = file.read().splitlines()

print(filecontent)

length = int(filecontent[0])

matrix = [[] for j in range(length)]

row = 0
for line in range(1, len(filecontent)):
    parsed_line = filecontent[line].split(' ')
    for i in parsed_line:
        matrix[row].append(int(i))
    row += 1

# print(matrix)

# testovaci vstup
# matrix = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
file.close()

data = []
for i in range(length):
    data.append(i + 1)

n = len(data)

all_sets = []
g = {}
p = []


def main():
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]

    get_minimum(1, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

    for key, value in g.items():
        print(key, value)
    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                break
    print('1}')
    return


def get_minimum(k, a):
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k - 1][j - 1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    main()
    sys.exit(0)

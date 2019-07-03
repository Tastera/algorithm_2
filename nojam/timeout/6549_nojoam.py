while True:
    graph = list(map(int, input().split()))
    if graph == [0]:
        break
    max_height = max(graph[1:])
    max_square = 0
    for height in range(max_height, 0, -1):
        check_square = 0
        width = 0
        row = graph[0]
        if height*graph[0] <= max_square:
            break

        while row > 0:
            # 백트래킹
            if row*height < max_square:
                break

            while graph[row] >= height and row > 0:
                width += 1
                row -= 1

            check_square = width * height
            if max_square < check_square :
                max_square = check_square
            row -= 1
            width = 0

    print(max_square)
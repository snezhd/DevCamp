def brick_validator(layer):
    """Counts how many bricks are used in
    the first layer and creates a dictionary
    """
    count = {}
    for row in layer:
        for b in row:
            if b in count:
                count[b] += 1
            else:
                count[b] = 1
    return count


def build(n, m, layer):
    """Builds a second layer using the input"""

    # Defines a valid area of less than 100 rows/columns
    if m >= 100 and n >= 100:
        return 'Not Allowed'

    # Calls the dictionary function and takes the keys and values
    d = brick_validator(layer)
    br = list(d.keys())
    halves = list(d.values())

    # Validates that there are no bricks spanning 3 rows/columns
    if list(filter(lambda x: x > 2, halves)):
        return 'Not Allowed'

    # Creates the second layer base
    layer2 = [[None for x in range(m)] for x in range(n)]

    # Creates a nested for loop for iterating through rows and columns
    # in order to fill the bricks in the second layer
    for row in range(n):
        for col in range(m):

            # Checks whether there are unused bricks
            if len(br) <= 0:
                break

            # Checks whether there is a brick or not
            if layer2[row][col] is not None:
                continue

            # Pops the used brick
            brick = br.pop()

            # Checks wheter the bricks in the first layer are on the same row
            # and lays the bricks on the second layer horizontally
            if col + 1 < m  and layer[0][col] != layer[0][col + 1]:
                layer2[row][col] = brick
                layer2[row][col + 1] = brick

            # If the first condition is not met then lays
            # the bricks on the second layer vertically
            else:
                layer2[row][col] = brick
                layer2[row + 1][col] = brick

    # The final result of the second layer is reversed because we want
    # the first row of first layer to be different from the last row in later2
    return list(reversed(layer2))


if __name__  == "__main__":
    # Asking about the numbers for rows and columns
    N, M = list(map(int, input('Enter two values: ').split(' ')))

    # Creates a list from the layer input
    layer = []
    for i in range(N):
        row = list(map(int, input().split(' ')))
        layer.append(row)

    # N = 2
    # M = 4
    # layer = [[1,1,2,2],[3,3,4,4]]

    print(build(N, M, layer))

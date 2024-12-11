data = "9694820 93 54276 1304 314 664481 0 4"

dict = {}

# def transform_stones(input):
#     output = []
#     stones = input
#     for stone in stones:
#         if stone == "0":
#             output.append("1")
#         elif len(stone) % 2 == 0:
#             output.append(str(int(stone[0:int(len(stone)/2)])))
#             output.append(str(int(stone[int(len(stone)/2):])))
#         else:
#             output.append(str(int(stone) * 2024))
#     return output

def rules(input, iterations, max_iterations):
    key = str(input) + "_" + str(iterations) + "_" + str(max_iterations)
    if key in dict:
        return dict[key]
    if iterations == max_iterations + 1:
        return len(input)

    score = 0
    for stone in input:
        if stone == "0":
            score += rules(["1"], iterations + 1, max_iterations)
        elif len(stone) % 2 == 0:
            score += rules([str(int(stone[0:int(len(stone)/2)]))], iterations + 1, max_iterations)
            score += rules([str(int(stone[int(len(stone)/2):]))], iterations + 1, max_iterations)
        else:
            score += rules([str(int(stone) * 2024)], iterations + 1, max_iterations)

    # print(key, score)
    dict[key] = score
    return score

def transform_stones2(input, iterations, max_iterations):
    score = 0
    for stone in input:
        score += rules([stone], iterations, max_iterations)
    return score

input = data.split(" ")


print(transform_stones2(input, 1, 25))
print(transform_stones2(input, 1, 75))


# print(input)
# for i in range(75):
#     input = transform_stones2(input)
#     print(i, len(input))
#     # print(input)



# print(input, len(input))
# print(len(input))
#
import math
default = [0, 0, 0]
temp = default.copy()
better_res = math.inf
tolerance = 1e-6
step_size = 1

def function(x):
    print(f"({x[0]} - 8) ** 2 + ({x[1]} - 6) ** 2 + ({x[2]} + 2) ** 4")
    return (x[0] - 8) ** 2 + (x[1] - 6) ** 2 + (x[2] + 2) ** 4

best_x = default.copy()
best_res = function(best_x)
while better_res>tolerance:
    for i in range(len(default)):
        for step in [step_size, -step_size]:
            x_new = default.copy()
            x_new[i] += step
            res = function(x_new)
            if res < best_res:
                best_res = res
                best_x = x_new.copy()
    if best_res < better_res:
        pattern_default = [2 * best_x[i] - default[i] for i in range(len(default))]
        pattern_res = function(pattern_default)
        if pattern_res < best_res:
            default = pattern_default
            better_res = pattern_res
        else:
            default = best_x
            better_res = best_res
    else:
        step_size /= 2

    print(f"better\n parameters: {default}, result: {better_res}")
print(f"best result: {better_res}\nbest parameters: {default}")

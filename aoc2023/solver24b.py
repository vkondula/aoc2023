import sympy


def solve(data_in: str):
    hailstorms = []
    for line in data_in.splitlines():
        p_raw, v_raw = line.split("@")
        p = tuple(int(x.strip(" ")) for x in p_raw.split(","))
        v = tuple(int(x.strip(" ")) for x in v_raw.split(","))
        hailstorms.append((p, v))
    variables = x, y, z, xv, yv, zv, t1, t2, t3 = sympy.symbols("x y z xv yv zv, t1, t2, t3")
    eqs = []
    for ((lpx, lpy, lpz), (lvx, lvy, lvz)), t in zip(hailstorms[:3], [t1, t2, t3]):
        eqs.append(x + xv * t - lpx + lvx * t)
        eqs.append(y + yv * t - lpy + lvy * t)
        eqs.append(z + zv * t - lpz + lvz * t)
    a = sympy.solve_poly_system(eqs, variables)
    total = sum(a[0][0:3])
    print(total)
    return total
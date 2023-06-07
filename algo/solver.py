import math
from typing import Tuple


def solve_task(a: float, h: float, r: float, m: float) -> Tuple[bool, bool]:
    cube_volume = a**3
    cylinder_volume = math.pi * h * r**2
    return cube_volume >= m, cylinder_volume >= m

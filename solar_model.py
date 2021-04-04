# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        """if body.x > obj.x:
            angle = - math.atan((body.y - obj.y) / (body.x - obj.x))
        elif body.x < obj.x:
            angle = math.pi - math.atan((body.y - obj.y) / (body.x - obj.x))
        else:
            if obj.y < body.y:
                angle = math.pi / 2
            else:
                angle = - math.pi / 2"""

        sin = - (body.y - obj.y) / r
        cos = - (body.x - obj.x) / r
        body.Fx += cos * gravitational_constant * body.m * obj.m / r ** 2
        body.Fy += sin * gravitational_constant * body.m * obj.m / r ** 2


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.
    Параметры:
    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.x += body.Vx * dt + ax * dt ** 2 / 2
    body.y += body.Vy * dt + ay * dt ** 2 / 2
    body.Vx += ax * dt
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.
    Параметры:
    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
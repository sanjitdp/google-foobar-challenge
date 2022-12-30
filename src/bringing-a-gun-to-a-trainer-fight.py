import math

# returns ceil(x / y)


def ceiling_divide(x, y):
    return -(x // (-y))

# computes Euclidean distance between 2D points x and y


def euclidean_distance(x, y):
    return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

# finds angle of y relative to x


def get_angle(x, y):
    return math.atan2(y[0] - x[0], y[1] - x[1])


def solution(dimensions, your_position, trainer_position, distance):
    x_dimension = dimensions[0]
    y_dimension = dimensions[1]

    # check how far we need to search left, right, up, and down
    # since the ell_2 ball is contained in the square
    horizontal_search = ceiling_divide(distance, x_dimension)
    vertical_search = ceiling_divide(distance, y_dimension)

    # keep track of closest distance object at any angle
    # and whether it's a trainer or you
    angle_to_distance = {}
    for i in range(-horizontal_search, horizontal_search + 1):
        for j in range(-vertical_search, vertical_search + 1):
            # suppose we have an infinite 2D grid of rooms
            # and check whether the room has flipped or not
            horizontal_swapped = i % 2
            vertical_swapped = j % 2

            # compute the bearing
            if horizontal_swapped == 1:
                your_new_x = x_dimension - your_position[0] + i * x_dimension
                trainer_new_x = x_dimension - \
                    trainer_position[0] + i * x_dimension
            else:
                your_new_x = your_position[0] + i * x_dimension
                trainer_new_x = trainer_position[0] + i * x_dimension
            if vertical_swapped == 1:
                your_new_y = y_dimension - your_position[1] + j * y_dimension
                trainer_new_y = y_dimension - \
                    trainer_position[1] + j * y_dimension
            else:
                your_new_y = your_position[1] + j * y_dimension
                trainer_new_y = trainer_position[1] + j * y_dimension

            # compute your position, angle, and distance
            # in the reflected room
            your_new_position = [your_new_x, your_new_y]
            your_angle = get_angle(your_position, your_new_position)
            your_distance = euclidean_distance(
                your_position, your_new_position)

            # compute the trainer's position, angle, and distance
            # in the reflected room
            trainer_new_position = [trainer_new_x, trainer_new_y]
            trainer_angle = get_angle(your_position, trainer_new_position)
            trainer_distance = euclidean_distance(
                your_position, trainer_new_position)

            # update the angle to closest point map
            # with your new position
            if your_distance != 0 and your_distance <= distance:
                if your_angle in angle_to_distance and your_distance < angle_to_distance[your_angle][0]:
                    angle_to_distance[your_angle] = (your_distance, False)
                elif your_angle not in angle_to_distance:
                    angle_to_distance[your_angle] = (your_distance, False)

            # update the angle to closest point map
            # with the trainer's new position
            if trainer_distance <= distance:
                if trainer_angle in angle_to_distance and trainer_distance < angle_to_distance[trainer_angle][0]:
                    angle_to_distance[trainer_angle] = (trainer_distance, True)
                elif trainer_angle not in angle_to_distance:
                    angle_to_distance[trainer_angle] = (trainer_distance, True)

    # count the total number of trainers in the
    # angle to closest point map
    count = 0
    for _, (_, is_trainer) in angle_to_distance.items():
        if is_trainer:
            count += 1

    return count

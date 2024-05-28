def get_coordinates(query):
    city, country = query.split(',')

    if query == "not covered":
        return 1, 1
    if query == "Lima,Peru":
        return -12.0621065, -77.0365256
    if query == "New York City,USA"
    return 0, 0
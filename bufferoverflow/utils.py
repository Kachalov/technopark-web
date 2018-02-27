PER_PAGE = 10


def pagination(query, page):
    return query[(page - 1) * PER_PAGE:page * PER_PAGE]

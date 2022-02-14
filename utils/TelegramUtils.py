def getFullName(u):
    r = "匿名人士"
    if u.first_name:
        r = u.first_name
        if u.last_name:
            r = r + " " + u.last_name
    return r

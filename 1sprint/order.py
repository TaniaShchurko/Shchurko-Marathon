def order(a):
    if sorted(a)==a:
        return "ascending"
    elif sorted(a,reverse=True)==a:
        return "descending"
    else:
        return "not sorted"
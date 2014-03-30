def slope_style_score(scores):
    av = 0
    min = scores[0]
    max = scores[0]
    for item in scores:
        if min > item:
            min = item
    for item in scores:
        if max < item:
            max = item
    scores.remove(min)
    scores.remove(max)
    for item in scores:
        av += item
    result = av / len(scores)
    return float("%.2f" % result)

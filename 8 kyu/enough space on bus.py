


def enough(cap, on, wait):
    canTake = cap - on
    cantTake = wait - canTake
    if wait == canTake or wait<canTake:
        return 0
    else:
        return cantTake
    # Your code here
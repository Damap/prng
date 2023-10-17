def is_in_interval(prng, interval):
    check = 1000

    while check != 0:
        check -= 1
        value = prng.next_int()

        if value < 0 or value >= interval:
            return False

    return True

def is_generates_all_numbers(prng, interval):
    check = 500
    values = set()

    while check != 0:
        check -= 1
        value = prng.next_int()
        values.add(value)

    return len(values) == interval

def is_prng_predictable(prng):
    check = 1000
    predictable = 3
    values = []

    for i in range(check):
        value = prng.next_int()
        values.append(value)

        if i >= predictable and value == values[i - predictable]:
            return True

    return False


def fifa(prng):
    fifa = []
    problem = 0
    for fif in rang(90):
        fifa.append(prng.next_int())

def is_correct(PRNG):
    seed = 3
    interval = 100

    prng = PRNG(seed, interval)

    if not is_in_interval(prng, interval):
        return False
    elif not is_generates_all_numbers(prng, interval):
        return False
    elif not is_prng_predictable(prng):
        return False
    elif not fifa(prng)
        return False 

    return True

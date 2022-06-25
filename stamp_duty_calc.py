ratesFirst = [[300000, 0],
              [200000, 0.05]]

ratesSecond = [[125000, 0],
         [125000, 0.02],
         [675000, 0.05],
         [575000, 0.10]]

def stamp_duty(number, first):
    if first and number <= 500000:
        rates = ratesFirst
    else:
        rates = ratesSecond
    remainder = number
    i = 0
    total = 0
    while remainder > 0:
        if i == 4:
            result = remainder
            total += 0.12 * remainder
        else:
            result = min(rates[i][0], remainder)
            total += result * rates[i][1]

        remainder -= result
        i +=1

    return total


if __name__ == '__main__':
    stamp_duty(499999, False)
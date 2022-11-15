import math


def loss(freq, hr, ht, d):
    freq_log = math.log10(freq)
    ht_log = math.log10(ht)
    return 45.5 + 35.46 * freq_log - (1.1*freq_log - 0.7) * hr + (44.9 - 6.55*ht_log) * math.log10(d) - 13.82 * ht_log


def rec_prob(theta, sigma, pr):
    inside = (theta - pr)/(math.sqrt(2)*sigma)
    return math.erfc(inside)/2


def simulate(d, sigma):
    hr = 5  # in meters
    ht = 100  # in meters
    freq = 2000  # in MHz
    theta = -116  # in dBW
    pt = 20  # in W
    pt = 10*math.log10(pt)  # in dB
    pr = pt - loss(freq, hr, ht, d)
    return rec_prob(theta, sigma, pr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # pt comes from data
    # theta from data
    # freq from data
    # vars: dist and sigma
    # hr, ht - arbitrary
    # pr ?
    dist = 2  # in km
    sigma = 3.65  # in dB

    simulate(dist, sigma)
    # put that in loop, for different dist ig, then plot



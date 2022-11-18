import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def loss(freq, hr, ht, d):
    freq_log = math.log10(freq)
    ht_log = math.log10(ht)
    return 45.5 + 35.46 * freq_log - (1.1*freq_log - 0.7) * hr + (44.9 - 6.55*ht_log) * math.log10(d) - 13.82 * ht_log


def rec_prob(theta, sigma, pr):
    inside = (theta - pr)/(math.sqrt(2)*sigma)
    return math.erfc(inside)/2


def simulate(d, sigma):
    hr = 2  # in meters
    ht = 50  # in meters
    freq = [*range(1500, 2000, 100)]
    # in MHz
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
    dist = [*range(100, 2100)]
    dist = [d/100.0 for d in dist]# in km
    sigma = 3.65  # in dB
    hr = 2  # in meters
    ht = 50  # in meters
    freq = [*range(1500, 2000, 100)]

    l_tmp = []
    for f in freq:
        for d in dist:
            l_tmp.append([f, d, loss(f, hr, ht, d)])

    # l = np.array(l_tmp)
    l_df = pd.DataFrame(l_tmp, columns=["freq", "dist", "loss"])

    print(l_df)

    sns.lineplot(data=l_df, x="dist", y="loss", hue="freq")
    plt.show()



    # simulate(dist, sigma)
    # put that in loop, for different dist ig, then plot



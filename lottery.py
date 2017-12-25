##
# Lombrozo lottery simulator
#
# Computes the histogram of which tweet slots are favored
##
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# calculate all possible 16-bit coprimes of n
def coprimes(n):
    for x in range(1, 65535):
        if gcd(n, x) == 1:
            yield x

def iscoprime(a, b):
    return gcd(a, b) == 1

class Histogram():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.hist = [0]*maxsize

    def mark(self, x, size):
        self.hist[(x-1) % size] += 1
        
    def dump(self):
        for i in range(0, self.maxsize):
            print i+1, self.hist[i]

def make_histogram():
    histo = Histogram(4000)
    for retweetcount in range(1000, 1200):
        for h in coprimes(retweetcount):
            for j in range(1, 11):
                histo.mark(h*j, retweetcount)
    histo.dump()

make_histogram()

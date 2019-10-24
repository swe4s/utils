import sys

def h_ascii_sum(key, N):
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_polynomial_rolling(key, N, p=53, m=2**64):
    '''  p a prime number roughly equal to the number of characters in the input alphabe
         m should be a large number, since the probability of two random strings colliding is
           about 1/m. Sometimes m=2^64 is chosen'''
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N

class ChainHashTable:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [ [] for i in range(N) ]
        self.M = 0

    def insert(self, key, value):
        hash_slot = self.hash(key, self.N)
        self.T[hash_slot].append((key,value))
        self.M += 1
        return True

    def find(self, key):
        hash_slot = self.hash(key, self.N)

        for k,v in self.T[hash_slot]:
            if key == k:
                return v
        return None


class LPHashTable:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [ None for i in range(N) ]
        self.M = 0

    def insert(self, key, value):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def find(self, key):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None

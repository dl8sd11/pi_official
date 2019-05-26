import math
from random import randint
class BurnSide:
    def __init__(self,n,k):
        self.n = n
        self.k = k
        self.neg = False
        self.prime_divs = []
        self.poly = []
        self.res = ""
    def solve(self):
        if self.n == 0:
            return "Result >> 0.0000000000\n"
        elif self.n < 0:
            self.n = -self.n
            self.neg = True
        self.result = 0
        self.factorize(self.n) # generate prime_divs
        self.len = len(self.prime_divs)

        self.res += "Prime Divisors: "
        for p in self.prime_divs:
            self.res += "{: 5x} ".format(p[0])
        self.res += "\n"
        
        self.res += "Prime Div expo: ";
        for p in self.prime_divs:
            self.res += "{: 5x} ".format(p[1])
        self.res += "\n\n"

        exponent = [0 for i in range(self.len)]
        self.rotate(exponent,0)
        self.polynomial()
        for pfirst,psecond in self.poly:
            self.result += psecond * math.pow(self.k,pfirst)
        self.result /= self.n * 2
        if self.neg and self.result != 0:
            self.result = - self.result

        if self.k == 0:
            self.res += "\n\nResult >> 0.0000000000\n"
        else:
            self.res += "\n\nResult >> {:.10}\n".format(self.result)
        
        self.prime_divs.clear()
        self.poly.clear()
        self.neg = False
        return self.res
        
    def miller_robin(self,m,primes):
        if m < 2:
            return False
        u = m - 1
        t = 0
        while u % 2 == 0:
            u = u // 2
            t += 1
        x = mypow(primes,u,m)
        if x == 1 or x == m - 1:
            return True
        for i in range(t-1):
            x = x * x % m
            if x == 1:
                return False
            if x == m - 1:
                return True

        return False
    
    def mypow(self,base,exp,mod):
        if exp == 1:
            return base % mod
        hlf = mypow(base,exp//2,mod)
        if exp % 2 == 1:
            return hlf * hlf % mod
        else:
            return hlf * hlf % mod

    def isprime(slef,m):
        primes = [2,3,5,7,11,13,17,19,23,29,31,37]
        if m < 1000:
            i = 2
            while i * i <= m:
                if m % i == 0:
                    return False
                i += 1
            return True
        ret = True
        for p in primes:
            if p != m:
                ret = ret and miller_robin(m,p)

    def f(self,x,c):
        return (x * x + c) % self.n

    def pollard_rho(self,m,c):
        if m < 1000:
            i = 2
            while i * i <= m:
                if m % i == 0:
                    return i
                i += 1
            return m
        a0 = randint(1,m-1)
        x = a0
        y = a0
        while True:
            x = self.f(x,c)
            y = self.f(self.f(x,c),c)
            if x == y:
                return m
            d = math.gcd(abs(x-y),m)
            if d > 1 and d < m:
                return d
        return -1

    def expo(self,m):
        ntp = self.n
        q = 0
        while ntp % m == 0:
            ntp /= m
            q += 1
        return q

    def factorize(self,m):
        if m == 1:
            return
        if self.isprime(m):
            for p in self.prime_divs:
                if m == p[0]:
                    return
            q = self.expo(m)
            self.prime_divs.append((m,q))
        else:
            d = m
            c = 0
            while d == m:
                d = self.pollard_rho(m,c)
                c += 1 
            self.factorize(d)
            self.factorize(m/d)
                

    def rotate(self,exponent,j):
        if j == self.len:
            d = 1
            for i in range(self.len):
                d *= math.pow(self.prime_divs[i][0],exponent[i])
            phi = self.n/d
            for i in range(self.len):
                if self.prime_divs[i][1] - exponent[i] != 0:
                    phi = phi * (self.prime_divs[i][0] - 1)/self.prime_divs[i][0]
            if self.neg:
                self.poly.append((-d,phi))
            else:
                self.poly.append((d,phi))
        else:
            for i in range(self.prime_divs[j][1]+1):
                exponent[j] = i
                self.rotate(exponent,j+1)
    def poly_expo(self,i):
        return -i[0]
    
    def polynomial(self):
        if self.neg:
            self.n = -self.n
        if self.n % 2 == 0:
            a = False
            b = False
            for i in range(len(self.poly)):
                first,second = self.poly[i]
                if first == self.n // 2:
                    self.poly[i] = (first,second+self.n//2)
                    a = True
                elif first == self.n // 2 + 1:
                    self.poly[i] = (first,second+self.n//2)
                    b = True
            if not a:
                self.poly.append((self.n/2,self.n/2))
            if not b:
                self.poly.append((self.n/2+1,self.n/2))
        else:
            a = False
            for i in range(len(self.poly)):
                first,second = self.poly[i]
                if first == (self.n+1)/2:
                    self.poly[i] = (first,second+self.n)
                    a = True
            if not a:
                self.poly.append(((self.n+1)/2,self.n))
        self.poly.sort(key=self.poly_expo)

        
        self.res += "["
        for i in range(len(self.poly)-1):
            self.res += "({} * k ^ {}) + ".format(self.poly[i][1],self.poly[i][0])
        self.res += "({} * k ^ {})] / ".format(self.poly[len(self.poly)-1][1],self.poly[len(self.poly)-1][0])

        if self.neg:
            self.res += "({})".format(self.n * 2)
        else:
            self.res += "{}".format(self.n * 2)

        if self.neg:
            self.n = -self.n

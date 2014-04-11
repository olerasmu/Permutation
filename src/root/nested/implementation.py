'''
Created on 4. apr. 2014

@author: olerasmu
'''

import math
class Permutation(object):
    
    def __init__(self, w=None, block_size=None, ts=None, tr=None, a=None, filepath=None):
        self.w = w
        self.filepath = filepath
        self.ts = ts
        self.tr = tr
        self.a = a
        self.block_size = block_size
    
    n = 0
    m = 0
    g = 0
    h = 0
    block_size = 0
    hg_tab = []
    block_tab = []
    symbol_tab = []
    
    
    
    def symbolifyFile(self):
        with open(self.filepath, 'rb') as newfile:
            symbol = newfile.read(self.w)
            while symbol:
                self.symbol_tab.append(symbol)
                symbol = newfile.read(self.w)
        
        self.m = self.block_size/self.w
        self.n = len(self.symbol_tab)/self.m
        return self.symbol_tab
    
    #===========================================================================
    # def symbolifyFile(self):
    #     with open(self.filepath, 'rb') as newfile:
    #         symbol = newfile.read(self.w)
    #         while symbol:
    #             self.symbol_tab.append(symbol)
    #             #print "New block: ", symbol
    #             symbol = newfile.read(self.w)
    #     self.m = self.block_size/self.w
    #     self.n = len(self.symbol_tab)/self.m
    #     self.block_tab = [[] for j in range(self.n)]
    #     #print self.block_tab
    #     print self.m
    #             
    # def blockifyFile(self):
    #     
    #     j = 0
    #     i = 0 
    #     for symbol in self.symbol_tab:
    #         if j < self.m:
    #             self.block_tab[i].append(symbol)
    #             j += 1
    #         elif j >= self.m:
    #             j = 0
    #             i += 1   
    #     #print self.block_tab
    #===========================================================================
                
                
        
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
    
    def computeGandH(self, a):
        print "n*m:", self.n*self.m, "n:", self.n, "m:", self.m
        self.g = math.ceil(self.ts/self.tr)*self.m + a 
        
        #h is the modular inverse of g
        self.h = self.modinv(self.g, self.n*self.m) #g % self.n*self.m
        
        print self.h
         
        
        print "g:", self.g, "h:", self.h
    
    def hourglass(self, i, h, n, m):
        h_i = self.symbol_tab[int((i*h) % (n*m))]
        return h_i
        #print "Index:", int((i*h) % (n*m)), "based on i:", i, "times h:", h
        #print "Symbol:", h_i
    
    def revHourglass(self, i, g, n, m):
        g_i = self.symbol_tab[i*g % n*m]
        print i*g % n*m
        print g_i

per = Permutation(w = 8, filepath = "C:\Users\olerasmu\Documents\\4mb_file.txt", block_size=4*1024, tr=0.0003125, ts=0.06)
per.symbolifyFile()
print "Length of symbol_tab:", len(per.symbol_tab)
#print len(per.block_tab)
#print per.block_tab[10]

#per.blockifyFile()

per.computeGandH(3)

testtab = []
#print per.modinv(98304, 1073741824)
for i in range(0,len(per.symbol_tab)):
    testtab.append(per.hourglass(i, per.h, per.n, per.m))
print len(testtab)

print testtab[524287]
#print "tab:", per.symbol_tab

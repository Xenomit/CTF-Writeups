#!/usr/bin/env python2

from z3 import *
from pwn import *

s = Solver()
fd = ELF("./re1")

x29 = 0x007f88d0

solution = []
for i in xrange(20):
    solution.append(BitVec('%d' % i, 8))
    s.add(solution[i] < 0x7f)
    s.add(solution[i] >= 0x20)


for i in xrange(7):
    for J in xrange(9):
        for K in xrange(3):
            for L in xrange(5):
                for M in xrange(2):
                    for N in xrange(4):

                        SUM = 0

                        for P in xrange(20):
                            x7 = P
                            x5 = M
                            x4 = N
                            x2 = K
                            x3 = L
                            x8 = i
                            x1 = J

                            x0 = (M*4 + M)*16;
                            x5 = x0 + (0x5460*i);
                            x1 = ( ((J*4 + J)*16) - (J*4 + J) ) * 32;
                            x1 = x5+x1;
                            x1 = ((N*4 + N)*4 ) + x1;
                            x1 = ((L*4 + L) * 32 ) + x1;
                            x0 = x1 + (((((K*2) + K) * 8) + K) * 32 ) + P;


                            x6 = 0x48d000+0x10    
                            w0 = ord(fd.read(x6 + x0*4, 1))

                            x1 = P
                            x2 = x29 + (6*4096);
                            x2 = x2 + 0x720
                            x1 = x1 + x2;

                            w1 = solution[P] # Load single byte

                            w0  = w0 * w1;
                            w1  = SUM;
                            w0  = w0 + w1;
                            SUM = w0;


                        # Second part

                        x5 = N;
                        x6 = L;
                        x0 = J;
                        x3 = K;
                        x2 = i;

                        x1 = J*16 - J;
                        x1 = x1 + ( ((i*16 + i)*8) - i );
                        x1 = (x1 + (K*4 + K) ) + L;
                        x1 = x1 * 2;
                        x0 = ( (M + x1)*4 ) + N;

                        value = u32(fd.read(0x520a90+ x0*4, 4))

                        s.add(SUM == value)




if s.check() == z3.sat:
    m = s.model()
    res = ''

    for i in xrange(len(solution)):
        res += chr(m[solution[i]].as_long())

    print "[*] FLAG: %s" % (res)
    
else:
    print s.check()

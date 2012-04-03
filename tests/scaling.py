
"""Scrcasest which makes plots of scaling. To use this, must copy in the
scaling times from profiling benchmark.py with cProfile."""

import numpy as N
import matplotlib.pyplot as PLT

class Scaling(object):
    def __init__(self):
        pass

def lin():
    """Scaling of lin_combine on lonestar, max procs/node (12)"""
    cases = []
    
    s = Scaling()
    s.total = 2711.155
    s.loads = 2616.031
    s.addmult = 0.
    s.sends = 0
    s.recvs = 0.
    s.barriers=0
    s.workers = 1
    cases.append(s)
       
    s = Scaling()
    s.total = 492.035
    s.loads = 249.827
    s.addmult = 0
    s.sends = 14.359
    s.recvs = 134.804
    s.barriers = 57.284
    s.workers = 6
    cases.append(s)
    
    s = Scaling()
    s.total = 183.618
    s.loads = 119.532
    s.addmult = 0
    s.sends = 12.215
    s.recvs = 16.438
    s.barriers = 12.973
    s.workers = 12
    cases.append(s)
    
    s = Scaling()
    s.total = 57.529
    s.loads = 24.666
    s.addmult = 0
    s.sends = 5.794
    s.recvs = 5.284
    s.barriers = 7.334
    s.workers = 24
    cases.append(s)
    
    s = Scaling()
    s.total = 30.213
    s.loads = 9.525
    s.addmult = 0
    s.sends = 3.859
    s.recvs = 5.831
    s.barriers = 4.921
    s.workers = 36
    cases.append(s)
    
    s = Scaling()
    s.total = 301.889
    s.loads = 70.511
    s.addmult = 0
    s.sends = 45.402
    s.recvs = 83.424
    s.barriers = 39.339
    s.workers = 48
    cases.append(s)
    
    s = Scaling()
    s.total = 18.126
    s.loads = 3.888
    s.addmult = 0
    s.sends = 2.201
    s.recvs =3.875
    s.barriers = 3.928
    s.workers = 60
    cases.append(s)
    
    s = Scaling()
    s.total = 245.177
    s.loads = 48.990
    s.addmult = 0
    s.sends = 35.351
    s.recvs = 68.313
    s.barriers = 45.808
    s.workers = 72
    cases.append(s)
    
    s = Scaling()
    s.total = 226.324
    s.loads = 42.373
    s.addmult = 0
    s.sends = 35.178
    s.recvs = 64.374
    s.barriers = 35.643
    s.workers = 84
    cases.append(s)
    
    s = Scaling()
    s.total = 20059.660
    s.loads = 28.007
    s.addmult = 0
    s.sends = 2749.347
    s.recvs = 4335.871
    s.barriers = 6554.987
    s.workers = 96
    cases.append(s)
    
    s = Scaling()
    s.total = 104.949
    s.loads = 12.439
    s.addmult = 0
    s.sends = 18.688
    s.recvs = 31.588
    s.barriers = 20.009
    s.workers = 144
    cases.append(s)
    
    s = Scaling()
    s.total = 82.448
    s.loads = 7.041
    s.addmult = 0
    s.sends = 14.170
    s.recvs = 26.106
    s.barriers = 17.349
    s.workers = 192
    cases.append(s)
    
    s = Scaling()
    s.total = 77.737
    s.loads = 4.519
    s.addmult = 0
    s.sends = 21.531
    s.recvs = 11.368
    s.barriers = 26.603
    s.workers = 240
    cases.append(s)
    
    
    workers = N.array([c.workers for c in cases])
    
    # Find the average for each processor, so now in Wall time instead of 
    # CPU time.
    for s in cases:
        s.total /= s.workers
        s.loads /= s.workers
        s.addmult /= s.workers
        s.sends /= s.workers
        s.recvs /= s.workers
        s.barriers /= s.workers
    
    # Speedup plot
    PLT.figure()
    width = .4
    PLT.hold(True)
    PLT.plot(workers, workers,'k-')
    PLT.plot(workers, [cases[0].total/c.total for c in cases],'ro-')
    PLT.xlabel('Workers')
    PLT.ylabel('Speedup')
    PLT.legend(['Linear','Measured'])
    #PLT.savefig('lin_combine_speedup_n1.eps')
    
    # Table of time spent in each operation for diff num of workers
    print 'Workers |   Total Wall   |        Loads       |' +\
        '      sends+recvs     |   barriers'
    for s in cases:
        print '  %d    |  %f   | %f (%f) | %f (%f) | %f (%f)'%(
            s.workers, s.total, s.loads, s.loads/s.total, (s.sends+s.recvs), 
            (s.sends+s.recvs)/s.total, s.barriers, s.barriers/s.total)
    
    
    # Time spent breakdown
    """
    PLT.figure()
    PLT.hold(True)
    PLT.plot(workers, cases[0].total/workers,'k-')
    PLT.plot(workers, [c.total for c in cases],'bx-')
    for c in cases:
        bottom = 0
        top = c.sends + c.recvs + c.barriers
        PLT.bar(c.workers-width/2, top-bottom, width=width,bottom=bottom,color='r')
        
        bottom = top
        top += c.loads
        PLT.bar(c.workers-width/2, top-bottom, width=width,bottom=bottom,color='g')
        
        bottom = top
        top = c.total
        PLT.bar(c.workers-width/2, top-bottom, width=width,bottom=bottom,color='k')
    PLT.legend(['Linear','Measured','Send/Recvs','Loads','Other'])
    PLT.xlabel('Workers')
    PLT.ylabel('Time [s]')
    PLT.savefig('lin_combine_time_n1.eps')
    """
    PLT.show()
    

    

def ips():
    """
    profiling data for IP mats
    """
    cases = []
    
    s = Scaling()
    s.total = 240.206
    s.loads = 164.500
    s.ips = 65.605
    s.sendrecvs = 0.
    s.workers = 1
    cases.append(s)
    
    s = Scaling()
    s.total = 96.103
    s.loads = 46.685
    s.ips = 34.112
    s.sendrecvs = 2.033+7.991
    s.workers = 2
    cases.append(s)
        
    s = Scaling()
    s.total = 61.961
    s.loads = 24.197
    s.ips = 25.325
    s.sendrecvs = 6.712+1.996
    s.workers = 3
    cases.append(s)
    
    s = Scaling()
    s.total = 44.644
    s.loads = 13.834
    s.ips = 17.896
    s.sendrecvs = 8.471 + 1.647
    s.workers = 4
    cases.append(s)
    
    s = Scaling()
    s.total = 29.408
    s.loads = 6.941
    s.ips = 12.147
    s.sendrecvs = 1.142 + 7.260
    s.workers = 6
    cases.append(s)
    
    s = Scaling()
    s.total = 24.200
    s.loads = 5.062
    s.ips = 8.619
    s.sendrecvs = 8.026+0.934
    s.workers = 8
    cases.append(s)
    
    s = Scaling()
    s.total = 20.427
    s.loads = 3.983
    s.ips = 6.931
    s.sendrecvs =7.376+0.769
    s.workers = 10
    cases.append(s)
    
    s = Scaling()
    s.total = 18.326
    s.loads = 3.180
    s.ips = 6.019
    s.sendrecvs = 7.242+0.668
    s.workers = 12
    cases.append(s)
    
    # Speedup plot
    PLT.figure()
    width = .4
    workers = N.array([c.workers for c in cases])
    PLT.hold(True)
    PLT.plot(workers, workers,'k-')
    PLT.plot(workers, [cases[0].total/c.total for c in cases],'ro-')
    PLT.xlabel('Workers')
    PLT.ylabel('Speedup')
    PLT.legend(['Linear','Measured'])
    PLT.savefig('IP_speedup_p1.eps')
    
    # Time spent breakdown
    PLT.figure()
    PLT.hold(True)
    PLT.grid(True)
    PLT.plot(workers, cases[0].total/workers,'k-')
    PLT.plot(workers, [c.total for c in cases],'ro-')
    
    for c in cases:
        bottom = 0
        top = c.sendrecvs
        PLT.bar(c.workers-width/2, top - bottom ,width=width,bottom=bottom,color='r')
        
        bottom = top
        top += c.loads       
        PLT.bar(c.workers-width/2, top-bottom,width=width,bottom=bottom,color='g')
        
        bottom = top
        top += c.ips
        PLT.bar(c.workers-width/2, top-bottom,width=width,bottom=bottom,color='k')
        
        bottom = top
        top = c.total
        PLT.bar(c.workers-width/2, top-bottom,width=width,bottom=bottom,color='k')

    PLT.legend(['Linear','Measured','Send/Recvs','Loads','IPs','Other'])
    PLT.xlabel('Workers')
    PLT.ylabel('Time [s]')
    PLT.savefig('IP_time_p1.eps')
    PLT.show()
    
    
    
    
if __name__=='__main__':
    #ips_n1p_rainier()
    #ips_np1_della()
    lin()
    
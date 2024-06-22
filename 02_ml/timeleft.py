import time

class TimeLeft:
    '''
    Return the amount of time left.
    
    timeleft = TimeLeft(N)
    
    N: maximum loop count
    
      for i in timeleft:
          : :

    or
       timeleft(i, extra)
      
    '''
    def __init__(self, N):
        self.N       = N        
        self.timenow = time.time
        self.start   = self.timenow()
        
    def __del__(self):
        pass
    
    def __timestr(self, ii):
        
        # elapsed time since start
        elapsed = self.timenow() - self.start
        s = elapsed
        h = int(s / 3600) 
        s = s - 3600*h
        m = int(s / 60)
        s = s - 60*m
        hh= h
        mm= m
        ss= s
        
        # time/loop
        count = ii+1
        t = elapsed / count
        f = 1/t
        
        # time left
        s = t * (self.N - count)
        h = int(s / 3600) 
        s = s - 3600*h
        m = int(s / 60)
        s =  s - 60*m
        percent = 100 * count / self.N

        return "%10d|%6.2f%s|%2.2d:%2.2d:%2.2d/%2.2d:%2.2d:%2.2d|%6.1f it/s" % \
            (count, percent, '%', hh, mm, ss, h, m, s, f)
        
    def __iter__(self):
        
        for ii in range(self.N):
            
            if ii < self.N-1:
                print(f'\r{self.__timestr(ii):s}', end='')
            else: 
                print(f'\r{self.__timestr(ii):s}')
                
            yield ii
            
    def __call__(self, ii, extra=''):
        
        if extra != '':
            extra = "\x1b[1;34;48m|%s\x1b[0m" % extra
           
        if ii < self.N-1:
            print(f'\r{self.__timestr(ii):s}{extra:s}', end='')
        else:
            print(f'\r{self.__timestr(ii):s}{extra:s}')

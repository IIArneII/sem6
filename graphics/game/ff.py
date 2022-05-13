s = """
a*m*s-b*m*s-m*s-a*n*s+c*n*s+n*s+a*k*t-c*k*t-k*t+m*t-a*k*w+b*k*w+k*w-n*w+m*s*x-n*s*x+k*t*x-m*t*x-k*w*x+n*w*x+b*s*y-c*s*y-a*t*y+c*t*y+a*w*y-b*w*y-b*k*z+c*k*z-a*m*z+b*m*z+a*n*z-c*n*z
"""
s = s.replace('a', 'p1[0]')
s = s.replace('b', 'p2[0]')
s = s.replace('c', 'p3[0]')
s = s.replace('k', 'p1[1]')
s = s.replace('n', 'p2[1]')
s = s.replace('m', 'p3[1]')
s = s.replace('s', 'p1[2]')
s = s.replace('t', 'p2[2]')
s = s.replace('w', 'p3[2]')
print(s)
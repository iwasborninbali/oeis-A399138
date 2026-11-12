import re
from itertools import combinations
from pathlib import Path
text = (Path(__file__).parent/'witnesses/a399138.txt').read_text()
blocks = re.split(r'(?m)^n = (\d+), (\d+) points[^\n]*\n', text)
expected = {1:1,2:8,3:16,4:28,5:40,6:64,7:73,8:94,9:116,10:138,11:164}
for i in range(1,len(blocks),3):
    n,m = map(int,blocks[i:i+2]); pts = [tuple(map(int,p)) for p in re.findall(r'\((\d+),(\d+),(\d+)\)',blocks[i+2])]
    assert m == expected[n] == len(pts) == len(set(pts))
    assert all(0<=v<n for p in pts for v in p)
    for a,b,c in combinations(pts,3):
        u=[b[k]-a[k] for k in range(3)]; v=[c[k]-a[k] for k in range(3)]
        assert (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]) != (0,0,0)
    print(f'n={n}: {m} points, no collinear triple')

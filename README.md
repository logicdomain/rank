# rank
通过秩宽，计算秩次，平均秩次

# How to use?
```
from logic.rank import Rank
r = Rank()
a = [1,2,3] # 已知秩宽
r.widths = a
print(a.rank) # 输出秩空间
```
will output:
```
[(1,1),(2,3),(4,6)]
```

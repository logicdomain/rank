# rank
通过秩宽，计算秩次，平均秩次

# How to use?
```
from logic.rank import Rank
r = Rank()
a = [1,2,3]
r.widths = a
print(a.rank)
```
will output:
```
[(1,1),(2,3),(4,6)]
```

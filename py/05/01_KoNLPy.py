#pip install konlpy
#pip install jpype1
from konlpy.tag import Kkma

kkma = Kkma()
malist=kkma.pos("아버지 가방에 들어가신다.")
print(malist)

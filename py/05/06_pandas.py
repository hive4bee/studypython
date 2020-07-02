import pandas as pd
#pip install xlrd
import xlrd
#Series생성자에 list를 전달해서 인스턴스를 생성한다.
s1=pd.Series([4,-2,5])
s1

#index속성으로 인덱스 배열을 추출할 수 있다.
list(s1.index)
list(s1.values)

#인덱스를 지정해서 시리즈를 생성할 수 있다.
s2=pd.Series([4,-2,5], index=["a","b","c"])
s2

#인덱스의 값을 키로 dict처럼 값을 추출/설정할 수 있다.
s2["c"]=2
s2

#DataFrame
df=pd.DataFrame({
    "math":[78,64,53],
    "english":[45,87,67]},
    index=["001","002","003"],
    columns=["math","english"]
)

df

#dict처럼 []내부에 레이블 이름을 지정해서 열을 나타내는 시리즈를 추출할 수 있다.
df["math"]

#레이블 이름을 속성처럼 사용할 수도 있다.
df.math

#ix 속성으로 인덱스 레이블을 지정하면 행을 추출할 수 있다.
df.ix["001"] #deprecated....
df.loc["001"]
df.loc["001","math"]

#ix 속성에 행 번호를 지정해도 행을 추출할 수 있다.
df.ix[0]
df.iloc[0]

#열은 시리즈이므로 []를 사용해 내부의 값을 추출할 수 있다.
df.english["001"]

#describe()메서드로 개수, 평균, 표준편차, 최소값, 백분위수, 최대값 등의 통계를 출력할 수 있다.
df.describe()

#csv파일 읽어 들이기
pd.read_csv("/mnt/hgfs/share/DEXKOUS.csv")

#read_excel
df_jobs=pd.read_excel("/mnt/hgfs/share/gugik.xlsx")
df_jobs
import matplotlib

#렌더링 백엔드로 데스크톱 환경이 필요없는 Agg를 사용한다.
matplotlib.use("Agg")

#한국어를 렌더링할 수 있게 폰트를 지정한다.
#macOS와 우분투 모두 정상적으로 출력하도록 2개의 폰트를 지정했다.
#기본 상태에서는 한국어가 깨진다.
matplotlib.rcParams["font.sans-serif"]="NanumGothic,AppleGothic"

import matplotlib.pyplot as plt

#plot()의 세 번째 매개변수로 계열 스타일을 나타내는 문자열을 지정한다.
#"b"는 파란색, "x"는 x표시마커, "-"는 마커를 실선으로 연결하라는 의미이다.
#키워드 매개변수 label로 지정한 계열의 이름은 범례로 사용된다.
plt.plot([1,2,3,4,5],[1,2,3,4,5],"bx-",label="첫 번째 함수")

#"r"은 붉은색,"o"는 O표시마커, "--"는 점선을 의미한다.
plt.plot([1,2,3,4,5],[1,4,9,16,25],"ro--", label="두 번째 함수")

#xlabel()함수로 X축의 레이블을 지정한다.
plt.xlabel("X값")
#ylabel()함수로 Y축의 레이블을 지정한다.
plt.ylabel("Y값")
#title()함수로 그래프의 제목을 지정한다.
plt.title("matplotlib 샘플")
#legend()함수로 범례를 출력한다. loc="best"는 적당한 위치에 출력하라는 의미이다.
plt.legend(loc="best")

#X축 범위를 0~6으로 지정한다. ylim() 함수를 사용하면 Y축 범위를 지정할 수 있다.
plt.xlim(0,6)

#그래프를 그리고 파일로 저장한다.
plt.savefig("advanced_graph.png", dpi=300)
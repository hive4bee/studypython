#apt-get build-dep -y python3-matplotlib
#apt-get install -y fonts-migmix
#pip install matplotlib
import matplotlib.pyplot as plt
#plot()함수로 x축과 y축의 값을 리스트로 지정해서 그래프를 그린다.
plt.plot([1,2,3,4,5],[1,4,9,16,25])

#show()함수로 그래프를 출력한다.
plt.show()
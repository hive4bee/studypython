from django.views.generic.base import TemplateView
from django.apps import apps

# TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['app_list'] = ['polls', 'books'] # 이 라인 대신 아래 5라인 추가한다.
        dictVerbose = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        return context
'''
1.장고가 제공하는 apps 객체의 get_app_configs() 메서드를 호출하면 settings.py 파일의
INSTALLED_APPS에 등록된 각 앱의 클래스들을 담은 리스트를 반환한다. for를 이용하여 각 설정 클래스들을 순회
2.app은 각 앱의 설정 클래스를 의미하므로, app.path는 각 설정 클래스의 path 속성으로,
애플리케이션 디렉토리의 물리적 경로를 뜻한다. 예를 들어 books앱의 물리적 경로는 
redbook/ch5/books/이다. 물리적 경로에 site-packages문자열이 들어있으면 외부 라이브러리 앱을
의미하므로, if 문에서 이런 앱을 제외한다.
3.설정 클래스의 label 속성값을 키(key)로 verbose_name 속성값을 값(value)으로 해서,
dictVerbose 사전에 담는다. books 앱의 경우, label은 books이고 verbose_name은
Book-Author_Publisher App 이다.
4.for 문이 오나료된 후에, verbose_dict 컨텍스트 변수에 dictVerbose사전을 대입한다.
'''
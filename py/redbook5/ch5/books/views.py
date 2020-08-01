from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher

# Create your views here.
# TemplateView, 필수적으로 template_name 클래스 변수를 오버라이딩해서 지정해줘야 함
# 템플릿 시스템으로 넘겨줄 컨텍스트 변수가 있는 경우에는 get_context_data()메서드를 오버라이딩해서 정의해준다.
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ["Book", "Author", "Publisher"]
        return context


# ListView, ListView를 상속받는 경우는 객체가 들어있는 리스트를 구성해서 이를 컨텍스트 변수로 템플릿 시스템에 넘겨준다.
#만일 이런 리스트를 테이블에 있는 모든 레코드를 가져와 구성하는 경우에는 테이블명, 즉 모델 클래스 명만 지정해준다.
#그리고 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성이 2가지 있다.
#첫 번째는 컨텍스트 변수로 object_list를 사용하는 것이고, 두 번째는 템플릿 파일을 모델명 소문자_list.html형식의
#이름으로 지정하는 것이다. 예) books/book_list.html, books/author_list.html, books/publisher_list.html
class BookList(ListView):
    model = Book

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher



#DetailView, DetailView를 상속받는 경우는 특정 객체 하나를 컨텍스트 변수에 담아서 템플릿 시스템에 넘겨주면 된다.
#만일 테이블에서 Primary Key로 조회해서 특정 객체를 가져오는 경우에는 테이블명 즉, 모델 클래스명만 지정해주면 된다.
#조회 시 사용할 Primary Key값은 URLconf에서 추출하여 뷰로 넘어온 파라미터를 사용한다.
#그리고 명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성이 2 가지 있다.
#첫 번째는 컨텍스트 변수로 object를 사용하는 것이고, 두 번째는 템플릿 파일을 모델명 소문자_detail.html형식의
#이름을 지정한다. 예) books/book_detail.html, books/author_detail.html, books/publisher_detail.hhtml
class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher



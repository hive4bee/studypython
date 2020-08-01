from django.contrib import admin
#from polls.models import Question, Choice
from polls.models import Question, Choice

# Register your models here.
#노말
'''
admin.site.register(Question)
admin.site.register(Choice)
'''
#필드 순서 변경하기, ModelAdmin클래스를 상속받아
#새로운 QuestionAdmin 클래스를 정의하여 admin.site.register()의 두 번째 인자로 등록한다.
'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']#필드 순서 변경
'''

#field를 분리해서 보여준다.
'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Statement", {"fields":['question_text']}),
        ("Date Information", {"fields":["pub_date"]}),
    ]
'''

#field를 접는다.
'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Statement", {"fields":['question_text']}),
        ("Date Information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
'''

#외래키 관계 화면
"""
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
"""

#테이블 형식으로 보여주기
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
"""

#레코드 리스트 컬럼 지정하기
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
    list_display = ("question_text", "pub_date") #레코드 리스트 컬럼 지정"""

#list_filter 필터
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
    list_display = ("question_text", "pub_date") #레코드 리스트 컬럼 지정
    list_filter = ["pub_date"] #필터 사이드 바 추가"""

#search_fields
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이 보기
    list_display = ("question_text", "pub_date") #레코드 리스트 컬럼 지정
    list_filter = ["pub_date"] #필터 사이드 바 추가
    search_fields = ["question_text"] #검색 박스 추가
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
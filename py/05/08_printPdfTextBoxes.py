import sys
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

def find_textboxes_recursively(layout_obj):
    """
    재귀적으로 텍스트 박스(LTTextBox)를 찾고
    텍스트 박스들을 리스트로 반화한다.
    """
    #LTTextBox를 상속받은 객체의 경우 리스트에서 곧바로 넣어서 반환한다.
    if isinstance(layout_obj, LTTextBox):
        return [layout_obj]
    #LTContainer를 상속받은 객체의 경우 자식 요소를 포함하는 있다는 의미이므로
    #재귀적으로 자식 요소를 계속 찾는다.
    if isinstance(layout_obj,LTContainer):
        boxes=[]
        for child in layout_obj:
            boxes.extend(find_textboxes_recursively(child))
        return boxes
    #아무것도 없다면 빈 리스트를 반환한다.
    return []

#공유 리소스를 관리하는 리소스 매니저를 생성한다.
laparams=LAParams()
resource_manager=PDFResourceManager()
#페이지를 모으는 PageAggregator객체를 생성한다.
device=PDFPageAggregator(resource_manager, laparams=laparams)
#Interpreter객체를 생성한다.
interpreter=PDFPageInterpreter(resource_manager,device)
#파일을 바이너리 형식으로 읽어 들인다.
with open(sys.argv[1], "rb") as f:
    #PDFPage.get_pages()로 파일 객체를 지정한다.
    #LTPage객체를 추출한다.
    #키워드 매개변수인 pagenos로 처리할 페이지 번호(0-index)를 리스트 형식으로 지정할 수도 있다.
    for page in PDFPage.get_pages(f):
        #페이지를 처리한다.
        interpreter.process_page(page)
        #LTPage객체를 추출한다.
        layout=device.get_result()
        #페이지 내부의 텍스트 박스를 리스트로 추출한다.
        boxes=find_textboxes_recursively(layout)
        #텍스트 박스를 왼쪽 위의 좌표부터 차례대로 정렬한다.
        #y1(Y좌표)는 위에 있을수록 크므로 음수로 변환하게 해서 비교한다.
        boxes.sort(key=lambda b: (-b.y1,b.x0))
        for box in boxes:
            #읽기 쉽게 선을 출력한다.
            print("-"*10)
            #텍스트 박스의 내용을 출력한다.
            print(box.get_text().strip())
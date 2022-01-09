#라이브러리 불러오기
import youtube_dl
from tkinter import*                #라이브러리에 포함된 모든 모듈을 임포트 할 때 * 사용 (tkinter에 포함된 모든 모듈을 사용)

#main 라는 변수에 TK()생성자로 윈도우 객체(첫글자는 대문자로 써야함)를 저장
main = Tk()

main.title("음원착즙기")             #제목 설정
main.resizable(False, False)        #창 크기 고정
main.configure(background='pink')   #배경색
main.geometry("400x110")            #창 크기 설정

def Extract():                      #Extract 라는 함수를 정의
    
    result=url.get()                #result라는 변수에 url로 입력받은 값 입력
    
    #유튜브 영상을  추출            
    ydl_opts = {                                    #youtube_dl 라이브러리 설정
    'format': 'bestaudio/best',                     #최고 품질로 추출
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',                #영상을 오디오 파일로 추출
        'preferredcodec': 'mp3',                    #오디오 파일 포맷을 mp3파일로 설정
        'preferredquality': '192',                  #오디오 품질 설정 192K
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([result])                      #result에 입력받은 주소의 영상을 다운로드


#텍스트 설정
label = Label(main, text="주소를 입력해주세요.", font=('NanumGothic', '20', 'bold'), background='pink')
label.pack()

#입력칸 설정
url = Entry(main, width=50)         #값을 입력받는 창을 url이라는 변수로 지정.
url.bind("<Return>", Extract)       #bind는 특정 이벤트가 발생하면 지정된 기능이 실행되도록 해줌. <Return>은 '엔터' 치는 이벤트를 인식
url.pack()                          #해당 위젯을 상위 위젯에 모두 패킹하여 불필요한 공간을 없앰

#버튼 클릭시 함수가 실행되도록 설정
button = Button(main, text="추출하기", font=('NanumGothic', '15', 'bold'), command=Extract)      #버튼 설정
button.pack()

#윈도우 창 유지(계속 갱신시킴)
main.mainloop()
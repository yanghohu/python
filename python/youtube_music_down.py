#라이브러리 불러오기
import youtube_dl
from tkinter import*                #라이브러리에 포함된 모든 모듈을 임포트 할 때 * 사용 (tkinter에 포함된 모든 모듈을 사용)

#main 라는 변수에 TK()생성자로 윈도우 객체(첫글자는 대문자로 써야함)를 저장
main = Tk()

main.title("음원착즙기")             #제목 설정
main.resizable(False, False)        #창 크기 고정
main.configure(background='pink')   #배경색
main.geometry("400x110")            #창 크기 설정

def Extract(bat_n):                      #Extract 라는 함수를 정의
    
    #result=url.get()                #result라는 변수에 url로 입력받은 값 입력
    
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
        ydl.download(bat_n)                      #result에 입력받은 주소의 영상을 다운로드

f=open('music.txt','r')
lines = f.readlines()
bat_n = []
for num in lines:
    bat_n.append(num)
    
print(bat_n)    
Extract(bat_n)
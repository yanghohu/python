﻿# -*- coding: utf-8 -*-
import os
import youtube_dl
import sys                           
#from os import rename, listdir

VIDEO_DOWNLOAD_PATH = './'  # 다운로드 경로

def download_video_and_subtitle(output_dir, youtube_video_list):

    download_path = os.path.join(output_dir, '%(id)s-%(title)s.%(ext)s')

    for video_url in youtube_video_list:

        # youtube_dl options
        ydl_opts = {
            'ignoreerrors': True,    # 오류무시
            'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 드 가능)
            'outtmpl': download_path, # 다운로드 경로 설정
            #'writesubtitles': 'best', # 자막 다운로드(자막이 없는 경우 다운로드 X)
            #'writethumbnail': 'best',  # 영상 thumbnail 다운로드
            #'writeautomaticsub': True, # 자동 생성된 자막 다운로드
            #'subtitleslangs': 'ko'  # 자막 언어가 영어인 경우(다른 언어로 변경 가능)
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            print('error', e)

def filerename():
    for root, dirs, files in os.walk("."):
        for filename in files:
            try:
                relativepath = os.path.join(root,filename) # 상대경로
                abspath = os.path.abspath(relativepath) # 절대경로
                name, ext = os.path.splitext(filename) #  파일명과 확장자 분리
                if(ext[0:4] == '.mp4'):
                    print(filename + " ==> " + filename[12:len(filename)])
                    os.rename(filename,filename[12:len(filename)])  
                else:
                    pass  
            except Exception as ex:
                continue

if __name__ == '__main__': 
    f=open('down.txt','r')
    lines = f.readlines()
    bat_n = []
    for num in lines:
        bat_n.append(num)
        
    print(bat_n)    
        
    download_video_and_subtitle(VIDEO_DOWNLOAD_PATH, bat_n)
    print('Complete download!')
    
    f.close()    
    
    # 파일 rename        
    filerename()
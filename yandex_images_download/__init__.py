# from __future__ import absolute_import
import sys,os
p = os.getcwd()[:-16] # n 是当前文件的文件夹名字字母个数+1
sys.path.append(p) # 通过在代码里面把包路径给拼上去

def run_main():
    from yandex_download.yandex_images_download import main
    main()

if __name__ == '__main__':
    run_main()
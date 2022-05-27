# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import numpy as np

def feature_process(name):

    txt_list=os.listdir(output_path)
    features_list=[]
    for txt in txt_list:
        if txt[-4:]=='.txt':
            this_path=os.path.join(output_path,txt)
            f=open(this_path)
            last_line=f.readlines()[-1]
            f.close()
            features=last_line.split(',')
            features=features[1:-1]
            np.save(output_path + '/'+name+'.npy',features)
            #features_list.append(features)
    #features_array=np.array(features_list)
    #print(features_array)
    
    
def main():
                
    audio_list=os.listdir(audio_path)
    for audio in audio_list:
        if audio[-4:]=='.wav':
            this_path_input=os.path.join(audio_path,audio)
            this_path_output=os.path.join(output_path,audio[:-4]+'.txt')
            cmd='cd /d ' + opensilme_path + 'bin/Win32 && SMILExtract_Release -C ' + config_path + ' -I ' + this_path_input + ' -O ' + this_path_output
        os.system(cmd)
        feature_process(audio[:-4])
if __name__ == "__main__":
    
    """
    路徑設定
    opensilme_path  : opensmile 根目錄
    audio_path      : 聲音檔路徑
    output_path     : 特徵輸出路徑
    config_path     : 設定檔路徑
    """
    opensilme_path = 'D:/桌面/opensmile-2.3.0/'
    audio_path = opensilme_path + 'example-audio' 
    output_path = opensilme_path + 'out'          
    config_path = opensilme_path + 'config/gemaps/eGeMAPSv01a.conf'
    
    main()
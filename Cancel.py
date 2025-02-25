import os
import pandas as pd
import numpy as np
import scipy
import librosa
from pydub import AudioSegment
from pydub.playback import play
import matplotlib
import numpy
from pydub.utils import which
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import audioread
# import file
from scipy.io.wavfile import write
from scipy.signal import butter,filtfilt

def cancel(pathn,paths): 
   
    noi = AudioSegment.from_file(pathn, format="wav")
    
    sig=AudioSegment.from_file(paths, format="wav")
   

    AudioSegment.converter = which("ffmpeg")
    

    def duration_detector(file):
        totalsec=0
        with audioread.audio_open(file) as f:

            # totalsec contains the length in float
            totalsec = f.duration
        length=int(totalsec)
        hours = length // 3600  # calculate in hours
        length %= 3600
        mins = length // 60  # calculate in minutes
        length %= 60
        seconds = length  # calculate in seconds

        return hours, mins, seconds

  
    x,y,z=duration_detector(paths)
    a,b,c=duration_detector(pathn)
    
    
    while x>a or y>b or z>c:
        
        noi+=noi
        if x<a or (x==a and y<b) or (x==a and y==b and z<c):
            break
        if c>=60:
            b+=1
        elif b>=0:
            a+=1
        else:
            a+=a
            b+=b
            c+=c
       
    noi+=noi

    
    invertednoise = noi.invert_phase()
    combined = sig.overlay(invertednoise,position=0)
    name="output.wav"
    combined.export(name, format="wav")
    return name


    

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
    

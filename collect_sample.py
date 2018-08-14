import pyaudio
import wave
import sys
import os
from scipy.io.wavfile import read
import python_speech_features as mfcc
import numpy 
from sklearn import preprocessing
import librosa

def write(features,X):
    #path to saved models
   
    modelpath  = "D:\\sdvrs\\csvfilesmfcc\\" 
    f=open(modelpath+X+'.csv','w')
    numpy.savetxt(f,features,newline=",")
    f.write(X)
    f.write('\n')
    f.close()
    print("n")

##def extract_feature(file_name):
##    X, sample_rate = librosa.load(file_name)
##    stft = numpy.abs(librosa.stft(X))
##    mfccs = numpy.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
##    chroma = numpy.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
##    mel = numpy.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
##    contrast = numpy.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
##    tonnetz = numpy.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
##    feat = numpy.hstack([mfccs,chroma,mel,contrast,tonnetz])
##
##    return feat




##CHUNK = 1024
##FORMAT = pyaudio.paInt16
##CHANNELS = 2
##RATE = 44100
##RECORD_SECONDS = 3
##for j in range(1,11):
##    
##    WAVE_OUTPUT_FILENAME = "D:\\sdvrs\\samples\\nikhello"+str(j)+".wav"
##    if sys.platform == 'darwin':
##        CHANNELS = 1
##
##    p = pyaudio.PyAudio()
##
##    stream = p.open(format=FORMAT,
##                            channels=CHANNELS,
##                            rate=RATE,
##                            input=True,
##                            frames_per_buffer=CHUNK)
##
##    print("* recording")
##
##    frames = []
##
##    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
##        data = stream.read(CHUNK)
##        frames.append(data)
##
##    print("* done recording")
##
##    stream.stop_stream()
##    stream.close()
##    p.terminate()
##
##    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
##    wf.setnchannels(CHANNELS)	
##    wf.setsampwidth(p.get_sample_size(FORMAT))
##    wf.setframerate(RATE)
##    wf.writeframes(b''.join(frames))
##    wf.close()

##    sourcepath=WAVE_OUTPUT_FILENAME
##    csv=[sourcepath.split("\\")[-1].split(".wav")[0]]
##    features=extract_feature(sourcepath)
##    print(csv[0])
##    write(features,csv[0])


    #path to testing data
sourcepath = "D:\\sdvrs\\samples\\"

files     = [os.path.join(sourcepath,f) for f in os.listdir(sourcepath) 
                      if f.endswith(".wav")] 
csv=[f.split("\\")[-1].split(".wav")[0]for f in files]
   
i=-1
for f in files:
          i=i+1
          features=extract_feature(f)
          print(csv[i])
          write(features,csv[i])

    

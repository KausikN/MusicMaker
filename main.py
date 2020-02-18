'''
Summary
Main Script for MusicMaker App
'''
from PianoAudioGenerator import PianoAudioGenerator as pa
from scipy.io import wavfile
import os
import pygame

# Driver Code
# Paths
mainpath = 'E:\Github Codes and Projects\Projects\MediaTor-Project\PianoAudioGenerator'
# TransposedSounds_file_path = os.path.join(mainpath, 'GeneratedSounds.p')
# RefSound_file_path = os.path.join(mainpath, 'bowl.wav')
# KeyConfig_file_path = os.path.join(mainpath, 'KeyConfig.kc')
TransposedSounds_file_path = input("Transposed Sounds File Path: ")
RefSound_file_path = input("Reference Sound File Path: ")
KeyConfig_file_path = input("KeyConfigs File Path: ")

# Controls
GenSounds = (input("Do you want to generate sounds? ") in ['y', 'yes']) # False
SaveSounds = (input("Do you want to save sounds? ") in ['y', 'yes']) # True
RuntimeRefreshingMode = 'Loop' # If Loop Sequence gets refreshed from file every loop, If All - Sequence gets refreshed in every iteration of playing sequence

# Create / Load Piano Sounds
# If Available load precreated sounds
KeySoundDict = None
if not GenSounds and os.path.exists(TransposedSounds_file_path):
    # Load Generated Sounds
    keys, sounds = pa.LoadKeySounds(TransposedSounds_file_path, KeyConfig_file_path)
    # Get Reference Audio File
    fps, sound = wavfile.read(RefSound_file_path)
    # Init Pygame
    pygame.mixer.init(fps, -16, 1, 2048)
    screen = pygame.display.set_mode((150, 150))
    KeySoundDict = dict(zip(keys, sounds))
else:
    # Generate Sounds
    KeySoundDict = pa.CreatePianoSounds(RefSound_file_path, KeyConfig_file_path, TransposedSounds_file_path=TransposedSounds_file_path, SaveSounds=SaveSounds)

        

# Get Piano Sequence
# seqPath = os.path.join(mainpath, 'DeathNote.piseq')
seqPath = input("Piano Sequence File Path: ")
MainSeq, SubSeqs = pa.ParsePianoSequenceFile(seqPath)
print(MainSeq)
print(SubSeqs)
Seq = pa.GetFullMainSeq(MainSeq, SubSeqs)
print("Audio Seq:")
print(Seq)



# Play Piano Sequence
pa.LoopPianoSequence(Seq, KeySoundDict, RuntimeRefreshingMode)

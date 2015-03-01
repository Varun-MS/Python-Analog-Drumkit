import pygame

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.init()
pygame.mixer.set_num_channels(8)

def PlayDrum1Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum1 = pygame.mixer.Channel(0)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum1.play(sound)

def PlayDrum2Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum2 = pygame.mixer.Channel(1)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum2.play(sound)

def PlayDrum3Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum3 = pygame.mixer.Channel(2)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum3.play(sound)

def PlayDrum4Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum4 = pygame.mixer.Channel(3)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum4.play(sound)

def PlayDrum5Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum5 = pygame.mixer.Channel(4)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum5.play(sound)

def PlayDrum6Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum6 = pygame.mixer.Channel(5)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum6.play(sound)

def PlayDrum7Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum7 = pygame.mixer.Channel(6)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum7.play(sound)

def PlayDrum8Sound(drumIndex, force):
    #Channel On Which This Sound Plays
    Drum8 = pygame.mixer.Channel(7)

    #Stores The Type Of Drum Being Struck 
    currentDrum = drums[drumIndex]

    #Stores The Number Of Audio Samples Associated With Current Drum Being Struck
    currentDrumForceLevels = forceLevels[currentDrum]

    #Calculates The Sample That Needs To Be Played Based On Force With Which Drum Is Struck
    loudnessIndex = int(round(force*currentDrumForceLevels));

    #Determines Filename Of Drum Sample
    audioSample = currentDrum + " (" + str(loudnessIndex) + ").ogg"

    sound = pygame.mixer.Sound(audioSample)
    Drum8.play(sound)

screen = pygame.display.set_mode((320,240))
running = 1

#Index Of The Drum Being Struck
drumIndex = 0

#Force With Which The Drum Is Struck. A Floating Point Value Between 0 and 1 Returned By Accelerometer
force = 0.5

#Dictionary Which Stores The Number Of Audio Samples Associated With Each Drum
forceLevels = {'ClHat' : 9, 'Flam' : 5, 'Kick' : 8, 'OpHat' : 7, 'PdHat' : 4, 'Rim' : 7, 'SdSt' : 7, 'Snr' : 5}

#Dictionary Which Helps Associate drumIndex With Its Corresponding Drum
drums = {1 : 'ClHat', 2 : 'Flam', 3 : 'Kick', 4 : 'OpHat', 5 : 'PdHat', 6 : 'Rim', 7 : 'SdSt', 8 : 'Snr'}

keystates={'1':False, '2':False, '3':False, '4':False, '5':False, '6':False, '7':False, '8':False}

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check for key down events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                keystates['1']=True
            if event.key == pygame.K_2:
                keystates['2']=True
            if event.key == pygame.K_3:
                keystates['3']=True
            if event.key == pygame.K_4:
                keystates['4']=True
            if event.key == pygame.K_5:
                keystates['5']=True
            if event.key == pygame.K_6:
                keystates['6']=True
            if event.key == pygame.K_7:
                keystates['7']=True
            if event.key == pygame.K_8:
                keystates['8']=True

        #check for key up events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                keystates['1']=False
            if event.key == pygame.K_2:
                keystates['2']=False
            if event.key == pygame.K_3:
                keystates['3']=False
            if event.key == pygame.K_4:
                keystates['4']=False
            if event.key == pygame.K_5:
                keystates['5']=False
            if event.key == pygame.K_6:
                keystates['6']=False
            if event.key == pygame.K_7:
                keystates['7']=False
            if event.key == pygame.K_8:
                keystates['8']=False

    if keystates['1']:
        drumIndex = 1
        PlayDrum1Sound(drumIndex,force)
        keystates['1']=False
    if keystates['2']:
        drumIndex = 2
        PlayDrum2Sound(drumIndex,force)
        keystates['2']=False
    if keystates['3']:
        drumIndex = 3
        PlayDrum3Sound(drumIndex,force)
        keystates['3']=False
    if keystates['4']:
        drumIndex = 4
        PlayDrum4Sound(drumIndex,force)
        keystates['4']=False
    if keystates['5']:
        drumIndex = 5
        PlayDrum5Sound(drumIndex,force)
        keystates['5']=False
    if keystates['6']:
        drumIndex = 6
        PlayDrum6Sound(drumIndex,force)
        keystates['6']=False
    if keystates['7']:
        drumIndex = 7
        PlayDrum7Sound(drumIndex,force)
        keystates['7']=False
    if keystates['8']:
        drumIndex = 8
        PlayDrum8Sound(drumIndex,force)
        keystates['8']=False





        



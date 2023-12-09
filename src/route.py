import os, sys, time
from functools import cache
from sys import stdin 
#import numpy as pd
#import matplotlib

import matplotlib.pyplot as plt
import pandas as pd

from pydub import AudioSegment
import numpy as np





@cache



def magic_headers(stakerr):
    print(f"-> {stakerr}")

    # Assuming 'staker' is an mp3 file
    audio = AudioSegment.from_mp3(stakerr)

    # Convert audio to numpy array
    audio_arr = np.array(audio.get_array_of_samples())

    # Convert numpy array to pandas DataFrame
    audio_df = pd.DataFrame(audio_arr)

    # Create a scatter plot
    plt.figure(figsize=(10, 4))

    plt.scatter(range(len(audio_df)), audio_df, c='blue', alpha=0.5)
    plt.legend(['Audio Data'])
    plt.show()


    #plt.scatter(range(len(audio_arr)), audio_arr)
    #plt.plot(audio_arr)
    #plt.show()

    # Save the plot to the 'docs' folder
    i = 0
    while os.path.exists("doc/plot%s.png" % i):
        i += 1

    plt.savefig("doc/plot%s.png" % i)

    # Display the plot

def myrunner_pro():
    staker = str(input("[Ingresa el directorio Raiz]: > "))

    if not os.path.exists(staker):
        print("El directorio dado no existe !!!.")
        sys.exit(1)

    else:
        print("[+] Listando ...")
        time.sleep(1)

        try:
            for root, dirs, files in os.walk(staker):
                for name in files:
                    if name.endswith(('.mp3', '.ogg', '.m4a')):
                        #print(os.path.join(root, name))
                        captured_path = os.path.join(root, name)
                        magic_headers(captured_path)
                for name in dirs:
                    if name.endswith(('.mp3', '.ogg', '.m4a')):
                        print(os.path.join(root, name))


        except ValueError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    myrunner_pro()
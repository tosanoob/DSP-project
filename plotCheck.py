import os
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write 

signal_path = "trimmed_signals\\KiemThu-16k\\"

count = 0

for file in sorted(os.listdir(signal_path)):    
        sub_path = os.path.join(signal_path,file)
        for sub_file in sorted(os.listdir(sub_path)):
            exact_input_path = os.path.join(sub_path,sub_file)
            sr, data = read(exact_input_path)
            count += 1
            plt.subplot(5,21,count)
            plt.plot(data)

# for file in sorted(os.listdir(signal_path)):
#     sr, data = read(os.path.join(signal_path,file))
#     count+=1
#     plt.subplot(5,1,count)
#     plt.plot(data)
#     plt.title(file)

plt.show()
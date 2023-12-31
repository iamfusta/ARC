
import numpy as np
from gnuradio import gr

class activity_reporter(gr.sync_block):
    def __init__(self, threshold):
        gr.sync_block.__init__(
            self,
            name="activity_reporter",
            in_sig=[np.float32],  # FFT sonrası sinyal tipi
            out_sig=None          # Çıkış sinyali yok
        )
        self.threshold = threshold

    def work(self, input_items, output_items):
        fft_data = input_items[0]
        max_energy = np.amax(fft_data)

        if max_energy > self.threshold:
            current_time = np.datetime64('now')
            print(f"Activity detected at {current_time} with energy {max_energy}")
            # Burada dosya kaydı veya başka bir raporlama işlemi yapılabilir.

        return len(input_items[0])

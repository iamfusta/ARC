import numpy as np
from gnuradio import gr

class activity_reporter(gr.sync_block):
    def __init__(self, threshold=1.0):
        gr.sync_block.__init__(
            self,
            name="activity_reporter",
            in_sig=[(np.complex64, 1)],  # Karmaşık 32-bit kayan nokta türü için güncellenmiş imza
            out_sig=None
        )
        self.threshold = threshold

    def work(self, input_items, output_items):
        fft_data = input_items[0]
        # Karmaşık veri olduğundan gücü hesaplayarak gerçek bir değere dönüştürüyoruz.
        power = np.abs(fft_data)**2
        max_power = np.amax(power)

        if max_power > self.threshold:
            current_time = np.datetime64('now')
            print(f"Activity detected at {current_time} with power {max_power}")

        return len(input_items[0])

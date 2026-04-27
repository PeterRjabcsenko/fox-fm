import logging
from time import time

import numpy as np
import sounddevice as sd
from openwakeword.model import Model

from fox_ears.config.config import Config


class WakeUpService:
    def __init__(self, cfg: Config):
        self.logger = logging.getLogger("Wake Up Service")
        self.info = self.logger.isEnabledFor(logging.INFO)

        if self.info:
            time_init = time()

        self.cfg = cfg

        # Load model (you’ll plug in your custom model later)
        self.model = Model(wakeword_models=["path/to/your_model.tflite"])

        self.SAMPLE_RATE = 16000
        self.CHUNK_SIZE = 512

        if self.info:
            self.logger.info(f"initialized ({time() - time_init:.2f}s)")

    def __call__(self):
        self._listen()


    def _listen(self):
        if self.info:
            self.logger.info(f"Listening for wake word...")

        with sd.InputStream(samplerate=self.SAMPLE_RATE, channels=1, dtype="int16") as stream:
            while True:
                audio, _ = stream.read(self.CHUNK_SIZE)
                audio = audio.flatten().astype(np.float32)

                scores = self.model.predict(audio)

                for name, score in scores.items():
                    if score > 0.5: 
                        if self.info:
                            self.logger.info(f"Wake word detected: {name} ({score:.2f})")

                        return  # trigger event

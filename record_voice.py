import speech_recognition as sr
import numpy as np
import librosa
import librosa.util
import os

OWNER_VOICE_FILE = "owner_voice.npy"
SAMPLE_RATE = 16000
MFCC_FEATURES = 20

def record_voice():
    """Records and extracts MFCC features from the user's voice."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        audio_data = np.frombuffer(audio.get_wav_data(convert_rate=SAMPLE_RATE, convert_width=2), dtype=np.int16).astype(np.float32)

        # Normalize and trim silence
        audio_data = librosa.util.normalize(audio_data)
        audio_data, _ = librosa.effects.trim(audio_data)

        mfcc = librosa.feature.mfcc(y=audio_data, sr=SAMPLE_RATE, n_mfcc=MFCC_FEATURES)
        return mfcc

    except Exception as e:
        print(f"❌ Error capturing voice: {e}")
        return None

def register_voice():
    """Registers and saves the owner's voice features."""
    print("📝 Registering your voice...")
    owner_mfcc = record_voice()
    if owner_mfcc is not None:
        np.save(OWNER_VOICE_FILE, owner_mfcc)
        print("✅ Voice registered successfully!")
    else:
        print("❌ Voice registration failed.")

if __name__ == "__main__":
    register_voice()

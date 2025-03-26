import numpy as np
import librosa
import os
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from record_voice import record_voice  # Import the function directly

OWNER_VOICE_FILE = "owner_voice.npy"

def verify_voice():
    """Verifies the user's voice against the registered sample."""
    if not os.path.exists(OWNER_VOICE_FILE):
        print("⚠️ No registered voice found! Please run `register_voice.py` first.")
        return False

    recorded_mfcc = record_voice()
    if recorded_mfcc is None:
        return False

    try:
        saved_mfcc = np.load(OWNER_VOICE_FILE, allow_pickle=True)

        # Normalize MFCCs before comparison
        recorded_mfcc = librosa.util.normalize(recorded_mfcc)
        saved_mfcc = librosa.util.normalize(saved_mfcc)

        # Use Euclidean distance instead of DTW for better consistency
        distance, _ = fastdtw(recorded_mfcc.T, saved_mfcc.T, dist=euclidean)

        # Dynamically adjust threshold based on saved voice
        dynamic_threshold = max(5000, np.mean(saved_mfcc) * 300)

        if distance < dynamic_threshold:
            print(f"✅ Voice Matched! Distance: {distance:.2f} (Threshold: {dynamic_threshold:.2f})")
            return True
        else:
            print(f"❌ Voice Does Not Match! Distance: {distance:.2f} (Threshold: {dynamic_threshold:.2f})")
            return False

    except Exception as e:
        print(f"❌ Voice verification error: {e}")
        return False

if __name__ == "__main__":
    verify_voice()

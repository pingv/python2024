import os
import torch
import torchaudio

from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

# Initialize the model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


def load_audio(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found at path: {file_path}")
        raise FileNotFoundError(f"The file path is incorrect or the file does not exist.")
    
    try:
        waveform, sample_rate = torchaudio.load(file_path)
        if sample_rate != 16000:
            waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)
        # Ensure the waveform is mono (single channel)
        if waveform.shape[0] > 1:
            waveform = torch.mean(waveform, dim=0, keepdim=True)
        return waveform.squeeze()
    except RuntimeError as e:
        print(f"Audio loading error: {e}")
        print("Error loading audio file. Please check the file format is supported.")
        raise


# Provide the correct path to your audio file here
# file_path = "./harvard.wav"  # Make sure this points to your actual file

file_path = "/Users/vishnuparandhaman/code/python2024/python-exercise/harvard.wav"

# Print file path for confirmation
print(f"Using audio file at: {file_path}")

# Check file existence and load
waveform = load_audio(file_path)
inputs = processor(waveform, sampling_rate=16000, return_tensors="pt", padding=True)

# Run inference
with torch.no_grad():
    logits = model(inputs.input_values).logits

# Decode the output
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)[0]

print("Transcription:", transcription)

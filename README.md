# MVP ASR Architecture
The goal is to find the best architecture for the best ASR!

We want to reach: **Efficiency**, **Quickness** and **Frugality**!

Here's are our architecture idea:

<p align="center">
  <img src="img/model_router_architecture.png" alt="architecture" style="border-radius:8px">
</p>

## Standardisation for each model

For each model, there is a `model_type_name.py` in the folder "models" (either an API or a local processing) that creates the standardised JSON as output.
For each model, make a function **"infer"** to compute the model and to create the output.

## Standardisation for the **JSON** output of an STT model

```bash
- Batch ID (or the path + name)
- Info on the batch (language, total duration of the original audio, context, …)
- Text transcription of the batch
- Timestamp for the start and the end of the batch

- ASR Model Name
- Diarisation or not (bool) ==> Deleting or not "Speaker 0" for the WER test
- Compute duration
- Output: Text transcription of the model
```


<details>
<summary>See what it looks like</summary>

```bash
{
  "batch": {
    "batch_id": "batch_00123",
    "source": {
      "path": "/data/audio/",
      "filename": "meeting_audio.wav"
    },
    "metadata": {
      "language": "en-US",
      "context": "Business meeting about quarterly results",
      "original_audio_duration_sec": 842.5
    },
    "timestamps": {
      "start_sec": 0.0,
      "end_sec": 842.5
    }
  },

  "asr_configuration": {
    "model_name": "Whisper-large-v3",
    "diarization_enabled": true,
    "remove_speaker_0_for_wer": false
  },

  "processing": {
    "compute_duration_sec": 37.8
  },

  "transcription": {
    "full_text": "Good morning everyone. Today we will review the quarterly financial results...",
    "segments": [
      {
        "segment_id": 1,
        "speaker": "Speaker 1",
        "start_sec": 0.0,
        "end_sec": 12.4,
        "text": "Good morning everyone."
      },
      {
        "segment_id": 2,
        "speaker": "Speaker 2",
        "start_sec": 12.5,
        "end_sec": 28.9,
        "text": "Today we will review the quarterly financial results."
      }
    ]
  }
}

```

</details>

## Optimisation of the architecture (after)

- Word Boosting
- MoE
- FlashAttention
- vLLM
- Distillation
- Quantization
- Zipformer
- Pruning
- Merging
- Steering
- Parallelisation of the batch, frequency...

# MVP ASR Architecture
The goal is to find the best architecture for the best ASR!

We want to reach: **Efficiency**, **Quickness** and **Frugality**!

Here are our ideas for the architecture:

<p align="center">
  <img src="img/model_router_architecture.png" alt="Idea for the architecture">
</p>

## Standardisation for each model:
For each model, there is a `model_type_name.py` in the folder "models" (either an API or a local processing) that creates the standardised JSON as output.  
For each model, make a function **"infer"** to compute the model and to create the output.

## Standardisation for the **JSON** output of an STT model:
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



## Optimisation of the architecture (after) :
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

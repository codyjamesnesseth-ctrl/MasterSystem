import torch
from diffusers import StableDiffusionPipeline
import os, sys

MODEL_ID = "runwayml/stable-diffusion-v1-5"
OUTPUT_DIR = os.path.expanduser("~/MasterSystem/Security-Vault/Generated-Images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_visual(prompt):
    print(f"Synthesizing: {prompt}")
    try:
        pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float32)
        pipe.to("cpu") 
        image = pipe(prompt).images[0]
        path = os.path.join(OUTPUT_DIR, f"render_{len(os.listdir(OUTPUT_DIR))}.png")
        image.save(path)
        print(f"Saved to {path}")
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1: generate_visual(" ".join(sys.argv[1:]))

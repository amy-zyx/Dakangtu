"""Quick end-to-end test: submit a simple 'load checkpoint + empty latent + save image' workflow to cloud ComfyUI."""
import json
import sys

# Add tools dir to path
sys.path.insert(0, r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\tools")
from workflow_to_api import submit

CRED = "XT11TL:bCu5w26jSI"
BASE = "https://wp08.unicorn.org.cn:11274"

# Minimal v0 API format (ComfyUI 0.20.1) — uses direct primitive inputs
prompt = {
    "1": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {"ckpt_name": "xl/animaPencilXL_v500.safetensors"},
    },
    "2": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": "a beautiful girl with long black hair, anime style, masterpiece",
            "clip": ["1", 1],
        },
    },
    "3": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "text": "bad quality, blurry, lowres",
            "clip": ["1", 1],
        },
    },
    "4": {
        "class_type": "EmptyLatentImage",
        "inputs": {"width": 512, "height": 768, "batch_size": 1},
    },
    "5": {
        "class_type": "KSampler",
        "inputs": {
            "model": ["1", 0],
            "positive": ["2", 0],
            "negative": ["3", 0],
            "latent_image": ["4", 0],
            "seed": 42,
            "steps": 20,
            "cfg": 7,
            "sampler_name": "euler",
            "scheduler": "normal",
            "denoise": 1.0,
        },
    },
    "6": {
        "class_type": "VAEDecode",
        "inputs": {"samples": ["5", 0], "vae": ["1", 2]},
    },
    "7": {
        "class_type": "SaveImage",
        "inputs": {"images": ["6", 0], "filename_prefix": "cloud_test"},
    },
}

print("Submitting to cloud...")
result = submit(prompt, BASE, CRED)
print(json.dumps(result, indent=2, ensure_ascii=False))

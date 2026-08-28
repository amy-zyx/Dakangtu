---
name: "indextts-remote-api"
description: "Calls a remote Gradio-based IndexTTS HTTP API for voice cloning and TTS. Invoke when user needs to generate speech audio for Ren'Py dialogue using a remote IndexTTS server (e.g. AutoDL-hosted seetacloud instance). Uses gradio_client to bypass brittle raw-requests workaround."
---

# IndexTTS Remote API (Gradio 5.x)

## When to Use

- User has a remote IndexTTS Gradio app (e.g. AutoDL/seetacloud, custom Docker)
- Need to generate speech audio for character dialogue (Ren'Py `.ogg` voice files)
- Reference audio (voice sample) is on user's local machine
- Server URL pattern: `https://u{user_id}-{container_id}.bjb1.seetacloud.com:8443`

## 🚀 Quick Start

```powershell
# 1. Install gradio_client (one time)
python -m pip install gradio_client

# 2. Use the working script
python tools/generate_ami_voices_gradio_client.py --start 1 --end 1
python tools/generate_ami_voices_gradio_client.py  # all 11 lines
```

## 🔑 Critical Learnings (from real failures)

### ✅ DO use `gradio_client`, NOT raw `requests`

Raw requests is **extremely brittle** for Gradio 5.x. Use `gradio_client.Client.predict()`. It auto-handles:
- File upload
- SSE stream listening
- Spec parameter validation
- Error propagation

### ⚠️ Spec parameter names are `param_18` ~ `param_25`, NOT real names

The Gradio 5.x spec for `gen_single` returns 26 parameters, but the **last 8 have placeholder names**:

| Index | Actual Name in Spec | Real Parameter (from IndexTTS source) |
|-------|--------------------|---------------------------------------|
| 18 | `param_18` | `do_sample` |
| 19 | `param_19` | `top_p` |
| 20 | `param_20` | `top_k` |
| 21 | `param_21` | `temperature` |
| 22 | `param_22` | `length_penalty` |
| 23 | `param_23` | `num_beams` |
| 24 | `param_24` | `repetition_penalty` |
| 25 | `param_25` | `max_mel_tokens` |

**You MUST pass them as `param_18=True`, `param_19=0.8`, etc.** — real names like `do_sample=True` will fail with `TypeError: Parameter 'do_sample' is not a valid key-word argument`.

### ⚠️ Result is `{'value': '/path/to/file.wav', '__type__': 'update'}`, NOT `{'path': ...}`

The `gradio_client.predict()` returns an **"update" dict**, not a file-info dict:

```python
# ✅ Correct parsing
result = client.predict(...)
audio_path = result.get("value")  # /tmp/gradio/.../spk_xxx.wav

# ❌ Wrong (returns None)
audio_path = result.get("path") or result.get("url")
```

The path is on the **server's local disk** (e.g. `C:\\Users\\jwu40\\AppData\\Local\\Temp\\gradio\\...` for Windows server, or `/tmp/gradio/...` for Linux). Use `shutil.copy()` to save locally.

## 📋 Full Parameter List (26 total)

| # | Name | Type | Default | Notes |
|---|------|------|---------|-------|
| 0 | `emo_control_method` | Radio | "与音色参考音频相同" | Enum: 同上/情感参考/情感向量/情感描述 |
| 1 | `prompt` | File | (required) | Voice reference audio (use `handle_file(path)`) |
| 2 | `text` | String | (required) | Target text to synthesize |
| 3 | `lang_choice` | String | "ZH" | v2.5 only: ZH/EN/JA/AR/ES |
| 4 | `emo_ref_path` | File | None | Emotion reference audio |
| 5 | `emo_weight` | Float | 0.65 | 0.0 ~ 1.0 |
| 6-13 | `vec1` ~ `vec8` | Float | 0.0 | Emotion vector (喜/怒/哀/惧/厌恶/低落/惊喜/平静) |
| 14 | `emo_text` | String | "" | Emotion description (method=3) |
| 15 | `emo_random` | Bool | False | Random emotion sampling |
| 16 | `max_text_tokens_per_segment` | Int | 120 | 80-200 recommended |
| 17 | `duration_factor` | Float | 1.0 | 0.5=fast, 2.0=slow |
| 18-25 | `param_18` ~ `param_25` | mixed | various | See table above |

## 🛠️ Working Code Template

```python
from gradio_client import Client, handle_file
import shutil

client = Client("https://your-server:8443/")

result = client.predict(
    emo_control_method="与音色参考音频相同",
    prompt=handle_file("input/ref.wav"),
    text="你好世界",
    lang_choice="ZH",
    emo_ref_path=None,
    emo_weight=0.65,
    vec1=0.0, vec2=0.0, vec3=0.0, vec4=0.0,
    vec5=0.0, vec6=0.0, vec7=0.0, vec8=0.0,
    emo_text="",
    emo_random=False,
    max_text_tokens_per_segment=120,
    duration_factor=1.0,
    param_18=True,           # do_sample
    param_19=0.8,            # top_p
    param_20=30,             # top_k
    param_21=0.8,            # temperature
    param_22=0.0,            # length_penalty
    param_23=3,              # num_beams
    param_24=10.0,           # repetition_penalty
    param_25=1500,           # max_mel_tokens
    api_name="/gen_single",
)

audio_path = result.get("value")
shutil.copy(audio_path, "output.wav")
```

## 🐛 Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: Parameter 'do_sample' is not a valid key-word argument` | Used real name instead of `param_18` | Change all 8 to `param_18`~`param_25` |
| `'str' object has no attribute 'api_name'` | Tried to iterate `view_api(return_format='dict')` as list | Use `view_api()` without args, or skip API listing |
| Result returned but `audio_path is None` | Used `result.get("path")` | Use `result.get("value")` instead |
| `success: false, output: {error: null}` (raw requests) | Gradio 5.x swallows errors | Switch to `gradio_client` for proper error propagation |
| `404: Not Found` on `/queue/join` | Used `/call/{api_name}` wrong | Use POST `/gradio_api/queue/join` + GET `/gradio_api/queue/data?session_hash=xxx` |
| m4a not processed by IndexTTS | IndexTTS only handles WAV | Convert to WAV with ffmpeg first |

## 📁 Reference Files in This Project

- [tools/generate_ami_voices_gradio_client.py](file:///c:/Users/jwu40/Documents/trae_projects/Dakangtu/tools/generate_ami_voices_gradio_client.py) — Working production script
- [tools/generate_ami_voices_remote.py](file:///c:/Users/jwu40/Documents/trae_projects/Dakangtu/tools/generate_ami_voices_remote.py) — Raw requests version (DO NOT USE, kept for reference)
- [downloads/Agent调用说明.md](file:///c:/Users/jwu40/Documents/trae_projects/Dakangtu/downloads/Agent调用说明.md) — Original Gradio 3.x API doc (now obsolete, but useful for parameter semantics)

## 🔄 Pipeline for Ren'Py Voice Files

```
1. Reference audio (e.g. references/ami.m4a)
   ↓ ffmpeg
2. Convert to WAV (input/ami_ref.wav, 24kHz mono PCM16)
   ↓ gradio_client
3. Generate 11 voice files (game/audio/voice/ami_01.wav ~ ami_11.wav)
   ↓ ffmpeg libvorbis
4. Convert to OGG (ami_01.ogg ~ ami_11.ogg)
   ↓ Python script
5. Insert `voice "audio/voice/ami_NN.ogg"` into act2.rpy before each ami dialogue
```

## ⚙️ Reference Audio Requirements

- Format: **WAV** (not m4a, not mp3)
- Sample rate: **24kHz** (or 16kHz, 44.1kHz — IndexTTS will resample)
- Channels: **Mono** (stereo works but mono is better)
- Codec: **PCM 16-bit**
- Duration: **10-30 seconds** (longer = better voice quality, but slower)
- Content: Single speaker, clean recording, no background music

Convert m4a → wav:
```powershell
ffmpeg -i "references/ami.m4a" -ar 24000 -ac 1 -c:a pcm_s16le "input/ami_ref.wav"
```

## 📡 Server Connection Pattern (AutoDL / Seetacloud)

```
https://u{user_id}-{container_short_id}.{region}.seetacloud.com:{port}
                  │          │                    │            │
                  │          │                    │            └─ 8443 (HTTPS)
                  │          │                    └─ bjb1 (Beijing region 1)
                  │          └─ 7-8 char container hash
                  └─ User's AutoDL uid
```

Auth: None required for the Gradio app itself (the HTTPS is the security layer).

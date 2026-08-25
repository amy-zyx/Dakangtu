"""wav -> ogg vorbis 转码 (PyAV / ComfyUI venv)"""
import sys
from pathlib import Path
import av
import numpy as np

voice_dir = Path(r"C:\Users\jwu40\Documents\trae_projects\Dakangtu\game\audio\voice")
files = sorted(voice_dir.glob("voice_*.wav"))
print(f"Found {len(files)} wav files: {[f.name for f in files]}")

for f in files:
    # 读 wav
    in_container = av.open(str(f))
    in_stream = in_container.streams.audio[0]
    sr = in_stream.codec_context.sample_rate
    n_channels = in_stream.codec_context.channels
    print(f"\n  {f.name}: {sr}Hz, {n_channels}ch")

    # 收集所有 frame 的 audio samples
    frames = []
    for frame in in_container.decode(in_stream):
        frames.append(frame.to_ndarray())
    in_container.close()
    if not frames:
        print(f"    WARN: no audio frames in {f.name}")
        continue
    audio = np.concatenate(frames, axis=1)  # (channels, samples) - PyAV planar 格式
    # int16 -> float32 (PyAV vorbis requires fltp)
    if audio.dtype == np.int16:
        audio = audio.astype(np.float32) / 32768.0

    # 输出 ogg
    out_name = f.stem.replace("voice_", "lx") + ".ogg"
    out_path = voice_dir / out_name

    out_container = av.open(str(out_path), mode='w')
    out_stream = out_container.add_stream('flac', rate=sr)
    out_stream.layout = 'stereo' if n_channels == 2 else 'mono'

    frame = av.AudioFrame.from_ndarray(audio, format='fltp', layout=out_stream.layout)
    frame.sample_rate = sr
    frame.pts = 0
    for packet in out_stream.encode(frame):
        out_container.mux(packet)
    for packet in out_stream.encode(None):  # flush
        out_container.mux(packet)
    out_container.close()

    size_in = f.stat().st_size
    size_out = out_path.stat().st_size
    print(f"    -> {out_name}  ({size_in//1024}KB -> {size_out//1024}KB, {100*size_out//size_in}% size)")

print("\n=== Final state of voice/ ===")
for f in sorted(voice_dir.iterdir()):
    print(f"  {f.name}  ({f.stat().st_size//1024} KB)")

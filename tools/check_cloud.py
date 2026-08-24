import json
with open(r'C:\Users\jwu40\Documents\trae_projects\Dakangtu\cloud_oi.json', encoding='utf-8') as f:
    d = json.load(f)
print(f"Total node classes: {len(d)}")
print()
print("--- VNCCS / SAM3 / Anima ---")
for k in sorted(d.keys()):
    if any(x in k for x in ('VNCCS', 'CharacterCreator', 'SAM', 'sam3', 'Sam3',
                            'ClothesGenerator', 'ClothesDesigner',
                            'PoseStudio', 'ControlCenter',
                            'Anima', 'anima')):
        print(f"  {k}")
print()
print("--- Loaders / Samplers (sample) ---")
for k in sorted(d.keys()):
    if any(x in k for x in ('KSampler', 'CheckpointLoader', 'UNETLoader', 'LoraLoader', 'VAELoader', 'CLIPLoader')):
        print(f"  {k}")
print()
print("--- First 20 node names ---")
for k in sorted(d.keys())[:20]:
    print(f"  {k}")

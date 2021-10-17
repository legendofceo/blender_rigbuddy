import bpy
from pathlib import Path

destination_folder = "y:/repo/blender_rigbuddy/blender_docs"
df = Path(destination_folder)

#create if doesn't exist
if not df.exists():
    df.mkdir(parents=True, exist_ok=True)

for text in bpy.data.texts:
    p = df / text.name
    #if p.suffix == ".py":
    p.write_text(text.as_string())
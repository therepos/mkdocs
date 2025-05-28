import os
import hashlib
import shutil
import yaml

# === Config ===
target_dirs = {
    'css': 'docs/css' 
    # 'js': 'docs/js' 
}
mkdocs_yml = 'mkdocs.yml'

# === Helper: Generate hash and rename ===
def process_files(extension, folder):
    hashed_files = []

    for file in os.listdir(folder):
        if file.endswith(f".{extension}") and not any(char.isdigit() for char in file):
            original_path = os.path.join(folder, file)

            # Generate hash
            with open(original_path, 'rb') as f:
                hash_id = hashlib.md5(f.read()).hexdigest()[:8]

            new_name = f"{file.rsplit('.', 1)[0]}.{hash_id}.{extension}"
            new_path = os.path.join(folder, new_name)

            shutil.copyfile(original_path, new_path)
            print(f"[✔] {extension.upper()} file hashed: {new_name}")

            hashed_files.append(f"{extension}/{new_name}")
    
    return hashed_files

# === Run ===
extra_css = []
extra_javascript = []

if os.path.exists(mkdocs_yml):
    with open(mkdocs_yml, 'r') as f:
        config = yaml.safe_load(f)

for ext, folder in target_dirs.items():
    if ext == 'css':
        extra_css.extend(process_files(ext, folder))
    elif ext == 'js':
        extra_javascript.extend(process_files(ext, folder))

# === Update mkdocs.yml ===
if os.path.exists(mkdocs_yml):
    config['extra_css'] = extra_css
    config['extra_javascript'] = extra_javascript

    with open(mkdocs_yml, 'w') as f:
        yaml.dump(config, f, sort_keys=False)

    print("[✔] mkdocs.yml updated.")
else:
    print("[!] mkdocs.yml not found.")

import json
import re

# Read raw file and remove BOM if present
with open('questions.json', 'rb') as f:
    raw_data = f.read()

# Remove BOM (UTF-8 BOM is EF BB BF)
if raw_data[:3] == b'\xef\xbb\xbf':
    raw_data = raw_data[3:]
    
# Decode to string
text = raw_data.decode('utf-8')

# Remove all [cite: XXX] references
text = re.sub(r'\s*\[cite:\s*\d+\]', '', text)

# Parse and validate JSON
try:
    data = json.loads(text)
    print(f"✓ JSON valid with {len(data)} questions")
    
    # Write back without BOM
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✓ File cleaned and saved successfully")
except json.JSONDecodeError as e:
    print(f"✗ JSON Error: {e}")

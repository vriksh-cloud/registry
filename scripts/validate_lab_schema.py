import sys
import yaml
import os

def validate_lab(filepath):
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
        
    with open(filepath, 'r') as f:
        try:
            spec = yaml.safe_load(f)
        except Exception as e:
            print(f"ERROR: Invalid YAML format. {e}")
            sys.exit(1)
            
    required_fields = ["id", "name", "description", "credits_cost", "estimated_duration_minutes", "image", "target_port", "tasks"]
    for field in required_fields:
        if field not in spec:
            print(f"ERROR: Missing required field '{field}' in lab spec.")
            sys.exit(1)
            
    print(f"Validating Tasks for Lab '{spec['id']}'...")
    for t in spec['tasks']:
        if not all(k in t for k in ["id", "title", "description", "points", "validation"]):
            print(f"ERROR: Task '{t.get('id', 'UNKNOWN')}' is missing required fields.")
            sys.exit(1)
            
        val = t['validation']
        if 'command' not in val:
            print(f"ERROR: Task '{t['id']}' validation missing 'command'. Vriksh Engine requires an execution command.")
            sys.exit(1)
            
        print(f"  - Task '{t['id']}' looks good.")
        
    print(f"SUCCESS: Lab '{spec['id']}' schema is valid.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 validate_lab_schema.py <path_to_yaml>")
        sys.exit(1)
    validate_lab(sys.argv[1])
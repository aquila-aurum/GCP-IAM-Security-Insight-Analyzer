import json

def load_iam_policy(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def analyze_bindings(policy):
    risky_roles = ['roles/owner', 'roles/editor', 'roles/iam.securityAdmin']
    for binding in policy.get('bindings', []):
        if binding['role'] in risky_roles:
            print(f"[!] Risky Role Assigned: {binding['role']} -> {binding['members']}")

if __name__ == '__main__':
    policy = load_iam_policy('sample_iam_policy.json')
    analyze_bindings(policy)

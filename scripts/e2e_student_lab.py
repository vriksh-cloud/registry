import sys, time, subprocess, json
sys.path.append('.')
from database import get_session
from models import User
import lab_engine

username = "pam.e2e.student"

with get_session() as session:
    user = session.query(User).filter(User.username == username).first()
    if not user:
        user = User(username=username, credits=1000)
        session.add(user)
        session.commit()

print("Provisioning lab 'git-101'...")
res = lab_engine.provision_lab(username, "vriksh-git-101", "acme")
if not res['ok']:
    print("Provision failed:", res)
    sys.exit(1)

session_id = res['session_id']
container_name = f"lab-{session_id}-{username.replace('.', '-')}"

print(f"Waiting 15 seconds for Gitea container {container_name} to boot and setup script to finish...")
time.sleep(15)

def run_gitea_api(method, endpoint, data=None):
    cmd = ["docker", "exec", container_name, "curl", "-s", "-X", method, "-u", "student:vriksh", "-H", "Content-Type: application/json"]
    if data:
        cmd.extend(["-d", json.dumps(data)])
    cmd.append(f"http://localhost:3000{endpoint}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout

print("\n--- TASK 1: Create Repo ---")
out = run_gitea_api("POST", "/api/v1/user/repos", {"name": "hello-world", "private": False, "auto_init": True})
print("API Out:", out[:150])
chk1 = lab_engine.check_task(session_id, "create_repo")
print("Check Result:", chk1)

print("\n--- TASK 2: Create Branch ---")
out = run_gitea_api("POST", "/api/v1/repos/student/hello-world/branches", {"new_branch_name": "feature-auth", "old_branch_name": "main"})
print("API Out:", out[:150])
chk2 = lab_engine.check_task(session_id, "create_branch")
print("Check Result:", chk2)

print("\n--- TASK 3: Open PR ---")
file_data = {
    "content": "SGVsbG8gV29ybGQ=",
    "message": "Add feature file",
    "branch": "feature-auth"
}
run_gitea_api("POST", "/api/v1/repos/student/hello-world/contents/auth.txt", file_data)
pr_data = {
    "title": "Add feature auth",
    "head": "feature-auth",
    "base": "main"
}
out = run_gitea_api("POST", "/api/v1/repos/student/hello-world/pulls", pr_data)
print("API Out:", out[:150])
chk3 = lab_engine.check_task(session_id, "open_pr")
print("Check Result:", chk3)

print("\n--- Cleanup ---")
lab_engine.stop_lab(session_id)
print("Done.")

import sys
sys.path.append('mcp-servers/vriksh-lab-creator-mcp')
from vriksh_lab_creator_mcp import create_or_update_lab

print("Creating Git 102: Branching and Merging")
res1 = create_or_update_lab(
    lab_id="vriksh-git-102",
    name="Git 102: Branching and Merging",
    description="Learn how to create, push, and merge branches efficiently using Gitea.",
    credits_cost=10,
    duration_minutes=60,
    image="gitea/gitea:1.21.6",
    environment=[
        "USER_UID=1000",
        "USER_GID=1000",
        "GITEA__database__DB_TYPE=sqlite3",
        "GITEA__database__PATH=/data/gitea/gitea.db",
        "GITEA__security__INSTALL_LOCK=true",
        "GITEA__service__REQUIRE_SIGNIN_VIEW=true",
        "GITEA__admin__DISABLE_REGULAR_ORG_CREATION=true",
        "GITEA__security__ENABLE_X_FRAME_OPTIONS=false",
        "GITEA__cors__ENABLED=true",
        "GITEA__cors__ALLOW_DOMAIN=*",
        "GITEA__server__DOMAIN={lab_url}",
        "GITEA__server__ROOT_URL=https://{lab_url}/",
        "GITEA__server__SSH_PORT=2222",
        "GITEA__service__DISABLE_REGISTRATION=true"
    ],
    tasks=[
        {
            "id": "create_repo_102",
            "title": "Create a new repository",
            "description": "Create a public repository named `branching-lab`.",
            "points": 20,
            "validation": {
                "type": "gitea_api",
                "endpoint": "/api/v1/repos/student/branching-lab",
                "expected_status": 200
            }
        },
        {
            "id": "create_dev_branch",
            "title": "Create the dev branch",
            "description": "Create a new branch named `dev` from the main branch.",
            "points": 40,
            "validation": {
                "type": "gitea_api",
                "endpoint": "/api/v1/repos/student/branching-lab/branches/dev",
                "expected_status": 200
            }
        },
        {
            "id": "merge_dev_branch",
            "title": "Merge a Pull Request",
            "description": "Open a Pull Request from `dev` to `main` and merge it.",
            "points": 40,
            "validation": {
                "type": "gitea_api",
                "endpoint": "/api/v1/repos/student/branching-lab/pulls?state=closed",
                "expected_status": 200,
                "expected_json_array_length": 1
            }
        }
    ]
)
print("Git 102 Result:", res1)

print("Creating Git 103: Resolving Conflicts")
res2 = create_or_update_lab(
    lab_id="vriksh-git-103",
    name="Git 103: Resolving Conflicts",
    description="Simulate and resolve a git merge conflict within Gitea.",
    credits_cost=15,
    duration_minutes=90,
    image="gitea/gitea:1.21.6",
    environment=[
        "USER_UID=1000",
        "USER_GID=1000",
        "GITEA__database__DB_TYPE=sqlite3",
        "GITEA__database__PATH=/data/gitea/gitea.db",
        "GITEA__security__INSTALL_LOCK=true",
        "GITEA__service__REQUIRE_SIGNIN_VIEW=true",
        "GITEA__admin__DISABLE_REGULAR_ORG_CREATION=true",
        "GITEA__security__ENABLE_X_FRAME_OPTIONS=false",
        "GITEA__cors__ENABLED=true",
        "GITEA__cors__ALLOW_DOMAIN=*",
        "GITEA__server__DOMAIN={lab_url}",
        "GITEA__server__ROOT_URL=https://{lab_url}/",
        "GITEA__server__SSH_PORT=2222",
        "GITEA__service__DISABLE_REGISTRATION=true"
    ],
    tasks=[
        {
            "id": "create_repo_103",
            "title": "Create a new repository",
            "description": "Create a public repository named `conflict-lab`.",
            "points": 20,
            "validation": {
                "type": "gitea_api",
                "endpoint": "/api/v1/repos/student/conflict-lab",
                "expected_status": 200
            }
        },
        {
            "id": "open_conflict_pr",
            "title": "Create a conflicting Pull Request",
            "description": "Create two branches modifying the same file differently, and open a PR that is in a conflicting state.",
            "points": 40,
            "validation": {
                "type": "gitea_api",
                "endpoint": "/api/v1/repos/student/conflict-lab/pulls",
                "expected_status": 200,
                "expected_json_array_length": 1
            }
        },
        {
            "id": "resolve_and_merge",
            "title": "Resolve Conflict and Merge",
            "description": "Resolve the conflict using the Web UI or locally, and merge the PR.",
            "points": 40,
            "validation": {
                "type": "gitea_api",
                "endpoint": "/api/v1/repos/student/conflict-lab/pulls?state=closed",
                "expected_status": 200,
                "expected_json_array_length": 1
            }
        }
    ]
)
print("Git 103 Result:", res2)


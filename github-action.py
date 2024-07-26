import requests

# Replace these variables with your own information
GITHUB_TOKEN = 'token'
REPO_OWNER = 'mononsoft'
REPO_NAME = 'jerp-frontend'
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def get_workflow_runs():
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/59170304/runs'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['workflow_runs']


def delete_workflow_run(run_id):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs/{run_id}'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Successfully deleted run {run_id}')
    else:
        print(f'Failed to delete run {run_id}: {response.status_code}')


runs = get_workflow_runs()
for run in runs:
    print(run)
    # delete_workflow_run(run['id'])
#
# while len(runs) > 0:
#     runs = get_workflow_runs()
#     for run in runs:
#         print(run)
#         delete_workflow_run(run['id'])

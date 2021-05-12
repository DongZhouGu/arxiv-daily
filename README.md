# get-daily-arxiv-noti

This repository is build based on [here](github.com/kobiso/get-daily-arxiv-noti)

- Subject: computer science (cs)
- Keywords: "human object interaction", "visual relation detection", "object detection", "transformer","scene understanding", "visual reasoning"

## Usage( github actions)

#### 0. ⭐Star⭐

#### 1.Clone this Repo and Create a Repo

- Create a repository to get notification in your github.
-  **click "Settings"->"Secrets"->"New repository secret"** 

```python
Name: GITHUB
# Authentication for user filing issue (must have read/write access to repository to add issue to)
Value: your_github_username,your_github_token
```

#### 2. Set Config

**update`config.py` as your perferences.**

```python

# The repository to add this issue to
REPO_OWNER = 'changeme'
REPO_NAME = 'changeme'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = ["changeme"]
```

#### 3.  workflow

To test the functionality, you can click " Run Workflow button" for an immediate run.


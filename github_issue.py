# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import requests
from config import REPO_OWNER, REPO_NAME


def make_github_issue(title, body=None, assignee=None, TOKEN=None, closed=False, labels=[]):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/import/issues' % (REPO_OWNER, REPO_NAME)

    # Headers
    headers = {
        "Authorization": "token %s" % TOKEN,
        "Accept": "application/vnd.github.golden-comet-preview+json"
    }

    # Create our issue
    data = {'issue': {'title': title,
                      'body': body,
                      'assignee': assignee,
                      'closed': closed,
                      'labels': labels}}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 202:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', response.content)


if __name__ == '__main__':
    title = 'Pretty title'
    body = 'Beautiful body'
    assignee = ''
    TOKEN = ''
    closed = False
    labels = ["bug"]
    make_github_issue(title, body, assignee, TOKEN, closed, labels)

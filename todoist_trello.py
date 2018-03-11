import requests
import uuid
# import json
from keybox import keybox
# from todoist.api    import TodoistAPI
# from trello         import TrelloClient

# class TodoistREST():


def td_get_labels():
    labels = td_request(endpoint='labels', method='GET').json()
    return {k['name']: k['id'] for k in labels}


def td_get_tasks(project=None, label=None):
    params = {'project_id': project, 'label_id': label}
    tasks = td_request(endpoint='tasks', method='GET', params=params)
    return tasks.json()


def td_find_task(name, prefix=True, cache_tasks=None):
    tasks = cache_tasks or td_get_tasks()
    matches = [i['id'] for i in tasks if i['content'].startswith(name)]
    return matches[0]


def td_request(endpoint='', method='POST', **kwargs):
    url = 'https://beta.todoist.com/API/v8/' + endpoint.strip('/')
    kwargs.setdefault('headers', {}).update({
        'Authorization': 'Bearer {}'.format(keybox.todoist.key)
    }).update({
        'Content-Type':  'application/json',
        'X-Request-Id':  str(uuid.uuid4())
    } if method == 'POST' or 'data' in kwargs or 'json' in kwargs else {})
    return requests.request(method, url, **kwargs)


def trello_request(method='POST', endpoint='', **kwargs):
    url = 'https://api.trello.com/1/' + endpoint.strip('/') + '/'
    kwargs.setdefault('query', {}).update(keybox.trello.dict)
    return requests.request(method, url, **kwargs)


# ==============================================================================
# if __name__ == '__main__':
#     main()

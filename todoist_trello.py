import requests
# import uuid
# import json
from keybox import keybox
# from todoist.api    import TodoistAPI
# from trello         import TrelloClient

cache_tasks = []

def main():
    todoist_test()


# class TodoistTrelloSync


def td_get_labels():
    labels = td_rest(endpoint='labels', method='GET').json()
    return {k['name']: k['id'] for k in labels}


def td_get_tasks(project=None, label=None):
    params = {'project_id': project, 'label_id': label}
    tasks = td_rest(endpoint='tasks', method='GET', params=params)
    return tasks.json()


def td_find_task(name, prefix=True, cache_tasks=None):
    tasks = cache_tasks or td_get_tasks()
    matches = [i['id'] for i in tasks if i['content'].startswith(name)]
    return matches[0]


def td_rest(endpoint='', method='POST', **kwargs):
    url = 'https://beta.todoist.com/API/v8/' + endpoint.strip('/')
    kwargs.setdefault('headers', {}).update({
        'Authorization': 'Bearer {}'.format(keybox.todoist.key)
        # , 'Content-Type':  'application/json'
        # , 'X-Request-Id':  str(uuid.uuid4())
    })
    response = requests.request(method, url, **kwargs)
    return response


def trello_request(method='POST', endpoint='', **kwargs):
    url = 'https://api.trello.com/1/' + endpoint.strip('/') + '/'
    kwargs.setdefault('query', {}).update(keybox.trello.dict)
    response = requests.request(method, url, **kwargs)
    return response


# def trello_test():
    # response = requests.request('GET', url, params=api_keys['trello'])
    # print(response.text)

# ==============================================================================
if __name__ == '__main__':
    main()

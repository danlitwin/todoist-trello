import uuid
import json
import requests
# import re

from keybox import keybox
# from todoist.api    import TodoistAPI
# from trello         import TrelloClient



def td_add_comment(task, content, attachment=None):
    comment = td_request('comments', 'POST', task_id=td_get_task_id(task), attachment=attachment)
    return comment


def td_get_task(name, create_if_not_found=True, **new_params):
    tasks = td_get_tasks()
    task = td_find_task_id(name, all_matches=False)
    if create_if_not_found and not task:
        task = td_add_task(name, **new_params)
    return task


def td_add_task(name, **kwargs):
    params = kwargs or {}
    params['content'] = name
    return td_request('tasks', 'POST', data=kwargs)


def td_get_task(name, prefix=True, all_matches=False, cache_tasks=None):
    if isinstance(name, int):
        # option 1:  get task by id
        if cache_tasks:
            return next((i for i in cache_tasks if i['id'] == name), None)
        else:
            task = td_request('tasks/{}'.format(name), 'GET')
    else:
        # option 2:  get task by name
        tasks = cache_tasks or td_get_all_tasks()
        matches = [i for i in tasks if
                   (i['content'].startswith(name)
                    if prefix else i['content'] == name)]
        if all_matches and len(matches) > 1:
            return matches
        return matches[0] if matches else None


def td_get_all_tasks(project=None, label=None):
    params = {'project_id': project, 'label_id': label}
    tasks = td_request('tasks', 'GET', params=params)
    return tasks.json()


def td_get_label_ids():
    labels = td_request(endpoint='labels', method='GET').json()
    return {k['name']: k['id'] for k in labels}


def td_request(endpoint='', method='post', **kwargs):
    # ============================================================================
    #   From https://developer.todoist.com/rest/v8/
    # ============================================================================
    #
    #  API endpoints accept arguments either as url-encoded values for non-POST
    #    requests or as json-encoded objects encoded in POST request body with
    #    application/json Content-Type.
    #
    #  Each modification request may provide additional X-Request-Id HTTP header
    #    that could be used as an unique string to ensure modifications are applied
    #    once — request having the same id as previously seen would be discarded.
    #
    #  The API relies on standard HTTP response codes to indicate operation result.
    #  The table below is a simple reference about the most used status codes:
    #
    #  Status	Description
    #  200	    The request was processed successfully.
    #  204	    The request was processed successfully without any data to return.
    #  4xx	    The request was processed with an error and should not be retried
    #            unmodified as they won’t be processed any different by an API.
    #  5xx     The request failed due to a server error, it’s safe to retry later.
    #
    #   All 200 OK responses have the Content-type: application/json and contain a
    #    JSON-encoded representation of one or more objects.
    #
    #   Payload of POST requests has to be JSON-encoded and accompanied with
    #    application/json Content-Type header.
    #
    # ============================================================================
    url = 'https://beta.todoist.com/API/v8/' + endpoint.strip('/')
    if method.lower() == 'get':
        response = requests.get(url, params=kwargs, headers=td_headers(method))
    else:  # elif method.lower() == 'post':
        response = requests.post(url, json=kwargs, headers=td_headers(method))
    if not response.ok:
        response.raise_for_status()
    return response.json() if response.ok else None


def td_raw_request(endpoint='', method='POST', **kwargs):
    url = 'https://beta.todoist.com/API/v8/' + endpoint.strip('/')
    newheaders = kwargs['headers'] if kwargs and 'headers' in kwargs else {}
    newheaders['Authorization'] = 'Bearer {}'.format(keybox.todoist.key)
    if method.upper() == 'POST' or 'data' in kwargs or 'json' in kwargs:
        newheaders['Content-Type'] = 'application/json'
        newheaders['X-Request-Id'] = str(uuid.uuid4())
    kwargs['headers'] = newheaders
    if 'data' in kwargs and isinstance(kwargs['data'], dict):
        kwargs['data'] = json.dumps(kwargs['data'])
    response = requests.request(method, url, **kwargs)
    return response.json() if response.ok else None


def td_headers(method='post'):
    headers = {'Authorization': 'Bearer {}'.format(keybox.todoist.key)}
    if method.lower() == 'post':
        headers['Content-Type'] = 'application/json'
        headers['X-Request-Id'] = str(uuid.uuid4())
    return headers


def trello_request(method='POST', endpoint='', **kwargs):
    url = 'https://api.trello.com/1/' + endpoint.strip('/') + '/'
    kwargs.setdefault('query', {}).update(keybox.trello.dict)
    return requests.request(method, url, **kwargs)
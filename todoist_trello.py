import requests
# import uuid
# import json
from keybox import keybox
# from todoist.api    import TodoistAPI
# from trello         import TrelloClient


def main():
    todoist_test()


# class TodoistTrelloSync


def todoist_test():
    return td_rest(endpoint='labels', method='GET').json()
    # td = TodoistAPI(api_keys['todoist']['key'])
    # td.sync()
    # for project in td.projects:
    #     if sync_td_projects.count(project.name) = 0:
    #         ':'.join('Home:Office:Molding'.split(':')[:-1])
    # plist = [[p['name'], p['item_order'], p['indent'],
    #     p['id']] for p in td['projects']]


def td_rest(endpoint='', method='POST', **kwargs):
<<<<<<< HEAD
    url = 'https://beta.todoist.com/API/v8/' + endpoint.strip('/')
=======
    url = 'https://beta.todoist.com/API/v8/' + endpoint.strip('/') + '/'
>>>>>>> e1954760a1aeb7a42183d258a5ff5f3274f17291
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

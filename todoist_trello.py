import requests
# import pickle
from todoist.api    import TodoistAPI
from trello         import TrelloClient

td_projects_to_sync = ['Home']


def main():
    trello_test()


# class TodoistTrelloSync


def todoist_test():
    url = lambda t: 'https://beta.todoist.com/API/v8/{}'.format(t)
    requests.get('https://beta.todoist.com/API/v8/projects', headers={'Authorization': 'Bearer {}}'.format()}).json()
    #td = TodoistAPI(api_keys['todoist']['key'])
    #td.sync()
    # for project in td.projects:
    #     if sync_td_projects.count(project.name) = 0:
    #         ':'.join('Home:Office:Molding'.split(':')[:-1])
    # plist = [[p['name'], p['item_order'], p['indent'], p['id']] for p in td['projects']]


def trello_request(method='POST', endpoint='', **kwargs):
    url = 'https://api.trello.com/1/' + endpoint.strip(chars='/') + '/'
    if 'query' in kwargs.keys():
        kwargs['query'].update(API_KEYS.trello.dict)
    else:
        kwargs['query'] = API_KEYS.trello.dict
    response = requests.request(method, url, **kwargs)
    return response


def trello_test():
    response = requests.request('GET', url, params=api_keys['trello'])
    print(response.text)

# ==============================================================================
if __name__ == '__main__':
    main()

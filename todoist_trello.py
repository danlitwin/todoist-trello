import requests
import pickle
from todoist.api    import TodoistAPI
from trello         import TrelloClient
import api_keys

td_projects_to_sync = ['Home']


def main():
    trello_test()


# class TodoistTrelloSync



def todoist_test():
    td = TodoistAPI(api_keys['todoist']['key'])
    td.sync()
    # for project in td.projects:
    #     if sync_td_projects.count(project.name) = 0:
    #         ':'.join('Home:Office:Molding'.split(':')[:-1])
    # plist = [[p['name'], p['item_order'], p['indent'], p['id']] for p in td['projects']]


def trello_test():
    tr = TrelloClient(
        api_key =       api_keys['trello']['key'],
        token =         api_keys['trello']['token']
    )
    all_boards = tr.list_boards()
    url = 'https://api.trello.com/1/members/me/boards'
    response = requests.request('GET', url, params=api_keys['trello'])
    print(response.text)

#===============================================================================
if __name__=='__main__':
    main()

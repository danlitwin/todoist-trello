#!/usr/bin/python3.6

import requests
import pickle
from todoist.api    import TodoistAPI
from trello         import TrelloClient

td_projects_to_sync = ['Home']

api_keys = {
'todoist': {
    'key':   '18c31701631652e1d742f5ba2de7ad8603ebee6b'},
'trello': {
    'key':   'c44c1ecbbc116c60827000c419e5cb1d',
    'token': 'aafd625924a8a03cc5028894cd59cf836fa23352416f66a3f9f806b9cc783e23'}
}

def main():
    trello_test()


class TodoistTrelloSync



def todoist_test():
    td = TodoistAPI(api_keys['todoist']['key'])
    td.sync()
    for project in td.projects:
        if sync_td_projects.count(project.name) = 0:
    ':'.join('Home:Office:Molding'.split(':')[:-1])
    plist = [[p['name'], p['item_order'], p['indent'], p['id']] for p in td['projects']]


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
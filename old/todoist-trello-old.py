#!/usr/bin/python3.6

import requests
import pickle
from todoist.api    import TodoistAPI
from trello         import TrelloClient
from attrdict       import AttrDict

tr_user = 'danlitwin'
tr_board = 'Home Improvement'
tr_board_id = '55a52be0ad77ec45a1a2defa'
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

# def todoist_test():
#     td = TodoistAPI(api_keys['todoist']['key'])
#     td.sync()
#     for project in td.projects:
#         if sync_td_projects.count(project.name) = 0:
#     ':'.join('Home:Office:Molding'.split(':')[:-1])
#     plist = [[p['name'], p['item_order'], p['indent'], p['id']] for p in td['projects']]

def trello_get_board_list(user, api_key_data):
    url = 'https://api.trello.com/1/members/' + user + '/boards'
    querystring = {
        'filter':       'open',
        'fields':       'name,id',
        'lists':        'none',
        'memberships':  'none',
        **api_key_data
    }
    response = requests.request('GET', url, params=querystring).json()
    return {b['name']: b['id'] for b in response}

def trello_get_board_id(board_name, user, api_key_data):
    board_list = trello_get_board_list(user, api_key_data)
    return [b['id'] for b in board_list if b['name']==board_name][0]

def trello_add_webhook(callback_url, object_id):
    tr = TrelloClient(
        api_key =       api_keys['trello']['key'],
        token =         api_keys['trello']['token']
    )
    tr.create_hook(callback_url, object_id, 'Trello-Todoist Sync')

#===============================================================================
if __name__=='__main__':
    main()

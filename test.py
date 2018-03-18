import todoist_trello as tdtr


def main():
    r = tdtr.td_request('labels', 'GET')
    print(r.json())



# ==============================================================================
if __name__ == '__main__':
    main()

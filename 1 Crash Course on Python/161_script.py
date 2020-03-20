def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    for e in events:
        print('{} {} {} @{}'.format(e.date, e.user.upper(), e.type, e.machine))
    machines = {}
    for event in events:
        # add machines
        if event.machine not in machines:
            machines[event.machine] = set()
        
        #add remove user 
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout' and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ', '.join(users)
            t = '{m}: {u}'.format(m=machine, u=user_list.upper())
            print(t)
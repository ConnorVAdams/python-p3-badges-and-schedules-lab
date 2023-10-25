def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    messages = []
    i = 1
    for name in names:
        messages.append(f'Hello, {name}! You\'ll be assigned to room {i}!')
        i += 1
    return messages

def printer(names):
    for name in names:
        print(f'Hello, my name is {name}.')
    i = 1
    for name in names:
        print(f'Hello, {name}! You\'ll be assigned to room {i}!')
        i += 1

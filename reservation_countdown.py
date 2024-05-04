from time import sleep

mins = 10
while mins >= 0:
    if mins == 5:
        print('Place your reservation soon! 5 minutes remaining.')
    elif mins == 2:
        print('Don\'t lose your seats! 2 minutes remainig.')
    elif mins == 0:
        print('User timed out.')
    else:
        print(mins)
    mins -= 1
    sleep(1)
import os

# Runs bash command based on specified input parameter
# 1 prints memory
# 2 prints current networks
# 3 prints file space
def run_bash_cmd(user_choice: int):
    print('-' * 80, '\n')
    print('You entered #', user_choice)

    if user_choice == 1:
        print('The available memory is ')
        os.system('free -tmh')

    elif user_choice == 2:
        print('The current network connections include: ')
        os.system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk \'{print $2}\' | grep [0-9] | uniq')
    
    elif user_choice == 3:
        print('Available file space is: ')
        os.system('df -h | grep \"Filesystem\\|root\"')
    
    return
import click
from cofin.find import find_w_dist
from cofin.find import find_w_pin
from cofin.find import find_ben


def find():
    selection = ''
    while selection != 'q':
        print("\nSelect Options:")
        print("\n[1] Find Vaccine with District")
        print("[2] Find vaccine with Pincode")
        print("[3] Find your Beneficiaries")
        print("[q] Quit")
        selection = str(input("\n> Enter the option: "))
        if selection == '1':
            find_w_dist()
            return
        if selection == '2':
            find_w_pin()
            return
        if selection == '3':
            find_ben()
        elif selection == 'q':
            return
        else:
            print('\n' + "Invalid input. Please try again.")

@click.command('find')
def starApp():
    find()
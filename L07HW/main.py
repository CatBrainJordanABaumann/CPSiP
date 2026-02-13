from run_bash_cmd_function import run_bash_cmd
from menu import Menu

main_menu = Menu()
main_menu.addOption("Check available memory")
main_menu.addOption("View network connections")
main_menu.addOption("Display free ram and swap")
main_menu.addOption("Quit")

run_bash_cmd(main_menu.getInput())
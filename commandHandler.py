import os
import subprocess


# TODO: user authorization (check user id)
# TODO: logging
# TODO: system events notifications


def change_dir(args):
    if len(args) < 2:
        return 'Error: directory name argument required.'
    if not args[1]:
        return 'Error: directory name can\'t be empty.'
    try:
        os.chdir(args[1])
        return f'{args[1]}>'
    except FileNotFoundError as e:
        return f'Error #{e.errno} [FileNotFoundError]: \n{e.strerror}'


def get_file(args):
    pass


def put_file(args):
    pass


def take_screenshot(args):
    try:
        import pyautogui
    except:
        return "Can't take screenshot without user interface"
    return pyautogui.screenshot()


def print_help(args):
    # TODO: write help text
    return 'help text'


command_map = {
    'cd': change_dir,
    'get': get_file,
    'put': put_file,
    'screenshot': take_screenshot,
    'help': print_help
}


def handle_command(command):
    if not command:
        return 'Error: empty command text.'
    command_parts = command.split()
    command_name = command_parts[0]
    if command_name in command_map:
        return command_map[command_name](command_parts)
    return run_generic_command(command)


def run_generic_command(command):
    process = subprocess.Popen(command.split(),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = None
    error = None

    try:
        output = stdout.decode('utf-8')
        error = stderr.decode('utf-8')
    except UnicodeDecodeError:
        output = stdout.decode('CP866')
        error = stderr.decode('CP866')

    return_code = process.poll()

    if return_code != 0:
        return f'RETURN CODE {return_code} \nerror: {error} \n {output}'

    return f'RETURN CODE {return_code} \n{output}'


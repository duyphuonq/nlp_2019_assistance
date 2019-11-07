import os
import psutil


commands = {
    'firefox': 'firefox',
    'chrome': 'google-chrome',
    'pinta': 'pinta',
    'terminal': 'gnome-terminal'
}

execute_name = {
    'firefox': 'firefox',
    'chrome': 'chrome',
    'pinta': 'pinta',
    'terminal': 'gnome-terminal'
}


def open_program(name):
    import os
    os.system(commands[name])


def close_program(name):
    executed = execute_name[name]
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid

            if executed in processName:
                # print(processName, ' ::: ', processID)
                os.system("kill {}".format(processID))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


# close_program("terminal")

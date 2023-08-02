import os
import sys

# ANSI escape codes for colors
COLOR_RED = "\033[0;31m"
COLOR_RESET = "\033[0m"
COLOR_CYAN = "\033[36m"

def main():
    app_name = sys.argv[1]
    settings_file = os.path.join(os.environ.get('BASE_DIR', ''), 'config/settings.py')
    if not os.path.exists(settings_file):
        print(f"{COLOR_RED}[Error]: Settings file not found.{COLOR_RESET}")
        return

    with open(settings_file, 'r') as f:
        lines = f.readlines()

    new_line = f'    "apps.{app_name}",\n'
    in_installed_apps = False

    with open(settings_file, 'w') as f:
        for line in lines:
            if 'INSTALLED_APPS' in line:
                in_installed_apps = True
            if in_installed_apps and line.strip() == ']':
                in_installed_apps = False
                f.write(new_line)
            f.write(line)

if __name__ == "__main__":
    main()
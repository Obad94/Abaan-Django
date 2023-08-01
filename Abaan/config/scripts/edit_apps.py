import sys
import os

def edit_apps_py(apps_dir, app_name):
    apps_py_path = os.path.join(apps_dir, "apps.py")

    # Read the existing content of apps.py
    with open(apps_py_path, "r") as f:
        content = f.read()
        # print("content: ", content)

    # Check if the pattern to be replaced exists in the file
    if f'name = "{app_name}"' in content:
        # Modify the content as needed (e.g., update the 'name' attribute)
        new_content = content.replace(f'name = "{app_name}"', f'name = "apps.{app_name}"')
        # print("new_content: ", new_content)

        # Write the modified content back to apps.py
        with open(apps_py_path, "w") as f:
            f.write(new_content)
    else:
        print("Pattern not found in apps.py. Failed to append directory name thus no changes were made.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python edit_apps.py <apps_dir> <app_name>")
        sys.exit(1)

    apps_dir = sys.argv[1]
    app_name = sys.argv[2]
    print("apps_dir: ", apps_dir)
    print("app_name: ", app_name)

    edit_apps_py(apps_dir, app_name)

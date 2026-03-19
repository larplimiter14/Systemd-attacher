#!/usr/bin/env python3
import os, stat

# needs ROOT

script_name = "tec4lf.py"

st = os.stat(script_name)
os.chmod(script_name, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

f_path = os.path.join(os.getcwd(), script_name)

service_file = "/etc/systemd/system/tec4lf.service"
service_content = f"""[Unit]
Description=opsec
After=network.target

[Service]
ExecStart={f_path}
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""

with open(service_file, "w") as f:
    f.write(service_content)

os.system("systemctl daemon-reexec")
os.system("systemctl daemon-reload")
os.system("systemctl enable tec4lf")
os.system("systemctl start tec4lf")
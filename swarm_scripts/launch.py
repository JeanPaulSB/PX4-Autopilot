# Launches multiple sitl vehicules in a PX4 SITL simulation
import subprocess
import os
from jinja2 import Template

# Template string to launch the vehicle
template_str = """PX4_SYS_AUTOSTART={{ autostart }} PX4_GZ_MODEL={{ modelo }} ./build/px4_sitl_default/bin/px4 -i {{ instancia }}"""
template = Template(template_str)
template_result = template.render({"autostart": 4001, "modelo": "x500", "instancia": 1})

subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', template_result])


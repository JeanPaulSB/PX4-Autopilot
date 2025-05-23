# Launches multiple sitl vehicules in a PX4 SITL simulation
import subprocess
import os
from jinja2 import Template

DRONE_COUNT = 2

# Template string to launch the vehicle
template_str = """PX4_SYS_AUTOSTART={{ autostart }} PX4_GZ_MODEL={{ model }} ./build/px4_sitl_default/bin/px4 -i {{ instance }}"""
template = Template(template_str)
template_result = template.render({
        "autostart": 4001,
	"model": "x500",
	"instance": 1,

    })
# Launching the first vehicle
subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', template_result])

template_str = """PX4_GZ_STANDALONE={{standalone}} PX4_SYS_AUTOSTART={{ autostart }} PX4_GZ_MODEL={{ model }} ./build/px4_sitl_default/bin/px4 -i {{ instance }}"""
template = Template(template_str)

for index,_ in enumerate(range(DRONE_COUNT)):
    args = {
        "standalone": 1,
        "autostart": 4001,
	"model": "x500",
	"instance": index + 1
    }
    template_result = template.render(**args)
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', template_result])


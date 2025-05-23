# Launches multiple sitl vehicules in a PX4 SITL simulation
import subprocess
import os
from jinja2 import Template

positions = [
    {"x": 0, "y": 0, "id": 0},
    {"x": 10, "y": 0, "id": 1},
    {"x": 20, "y": 0, "id": 2},
    {"x": 0, "y": 10, "id": 3},
    {"x": 10, "y": 10, "id": 4},
    {"x": 20, "y": 10, "id": 5},
    {"x": 0, "y": 20, "id": 6},
    {"x": 10, "y": 20, "id": 7},
    {"x": 20, "y": 20, "id": 8},
]

# Template string to launch the vehicle
template_str = """PX4_SYS_AUTOSTART={{ autostart }} PX4_GZ_MODEL={{ model }} ./build/px4_sitl_default/bin/px4 -i {{ instance }}"""
template = Template(template_str)
template_result = template.render({
        "autostart": 4001,
	"model": "x500",
	"instance": 1,

    })
# Launching the first vehicle
#subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', template_result])

template_str = """PX4_GZ_STANDALONE={{standalone}} PX4_SYS_AUTOSTART={{ autostart }} PX4_GZ_MODEL={{ model }} PX4_GZ_MODEL_POSE="{{x}},{{y}}" ./build/px4_sitl_default/bin/px4 -i {{ instance }}"""
template = Template(template_str)

for index,_ in enumerate(len(positions[1::])):
    x = positions[index + 1]["x"]
    y = positions[index + 1]["y"]
    args = {
        "standalone": 1,
        "autostart": 4001,
	    "model": "x500",
	    "instance": index + 1,
        "x": x,
        "y": y
    }
    template_result = template.render(**args)
    #subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', template_result])


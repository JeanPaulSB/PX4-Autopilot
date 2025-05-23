# Launches multiple sitl vehicules in a PX4 SITL simulation
import subprocess

DRONE_COUNT = 5

# Starts the PX4 SITL simulation
subprocess.Popen(["PX4_SYS_AUTOSTART=4001", "PX4_SIM_MODEL=gz_x500", "./build/px4_sitl_default/bin/px4","-i","1"])

# Loop to launch multiple drones
for i in range(2, DRONE_COUNT + 1):
	env = {
		'PX4_SYS_AUTOSTART': '4001',
		'PX4_SIM_MODEL': 'gz_x500'
	}
	subprocess.Popen(
		["./build/px4_sitl_default/bin/px4", "-i", str(i)],
		env=env,
		cwd="/Users/jeansierraboom/Downloads/PX4-Autopilot"
	)

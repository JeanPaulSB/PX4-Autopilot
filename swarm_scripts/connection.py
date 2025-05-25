import asyncio
from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)
async def run():
    """ Does Offboard control using position NED coordinates. """

    drone = System()
    print()
    await drone.connect(system_address="udp://0.0.0.0:14540")
    print("connected")

asyncio.run(run())

import streamlit as st
from pyparrot.Minidrone import Mambo

st.title("Mambo control")

mamboAddr = "d0:3a:aa:30:e6:5a"
st.text("Mambo address: "+mamboAddr)

i = st.empty()

takeoff = st.button("Takeoff")

duration=0.5

mambo = Mambo(mamboAddr, use_wifi=False)
i.write("trying to connect")
success = mambo.connect(num_retries=3)
i.write("connected: %s" % success)
if (success):
    # get the state information
    i.write("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

if takeoff:
    i.write("taking off!")
    mambo.safe_takeoff(5)
    
forward = st.button("forward")
if forward:
    i.write("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=duration)

backward = st.button("backward")
if backward:
    i.write("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=duration)


left = st.button("left")
if left:
    i.write("Flying direct: roll left")
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=duration)

right = st.button("right")
if right:
    i.write("Flying direct: roll right")
    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=duration)

up = st.button("Up")
if up:
    i.write("Flying direct: going up")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

down = st.button("Down")
if down:
    i.write("Flying direct: going down")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=1)


landing = st.button("land")
if landing:
    i.write("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    i.write("disconnect")
    mambo.disconnect()

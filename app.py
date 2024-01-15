import streamlit as st
from pyparrot.Minidrone import Mambo
from session import _get_state

st.title("Mambo control")

mamboAddr = "d0:3a:aa:30:e6:5a"
st.text("Mambo address: "+mamboAddr)

state = _get_state()

if state.mambo ==None:
    state.mambo = 0

i = st.empty()
duration=0.5

connect = st.button("Connect")

if connect:
    state.mambo = Mambo(mamboAddr, use_wifi=False)
    i.write("trying to connect")
    success = state.mambo.connect(num_retries=3)
    i.write("connected: %s" % success)
    if (success):
        # get the state information
        i.write("sleeping")
        state.mambo.smart_sleep(2)
        state.mambo.ask_for_state_update()
        state.mambo.smart_sleep(2)

takeoff = st.button("Takeoff")
if takeoff:
    i.write("taking off!")
    state.mambo.safe_takeoff(5)
    
forward = st.button("forward")
if forward:
    i.write("Flying direct: going forward (positive pitch)")
    state.mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=duration)

backward = st.button("backward")
if backward:
    i.write("Flying direct: going backwards (negative pitch)")
    state.mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=duration)


left = st.button("left")
if left:
    i.write("Flying direct: roll left")
    state.mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=duration)

right = st.button("right")
if right:
    i.write("Flying direct: roll right")
    state.mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=duration)

up = st.button("Up")
if up:
    i.write("Flying direct: going up")
    state.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

down = st.button("Down")
if down:
    i.write("Flying direct: going down")
    state.mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=1)


landing = st.button("land")
if landing:
    i.write("landing")
    state.mambo.safe_land(5)
    state.mambo.smart_sleep(5)

    i.write("disconnect")
    state.mambo.disconnect()

import streamlit as st
from pyparrot.Minidrone import Mambo

st.title("Mambo control")

mamboAddr = "d0:3a:aa:30:e6:5a"
st.text("Mambo address: "+mamboAddr)

button = st.button("Connect")

duration=0.5

if button:
    mambo = Mambo(mamboAddr, use_wifi=False)
    st.write("trying to connect")
    success = mambo.connect(num_retries=3)
    st.write("connected: %s" % success)

    if (success):
        # get the state information
        st.write("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)
    
        st.write("taking off!")
        mambo.safe_takeoff(5)
    
        forward = st.button("forward")
        backward = st.button("backward")
        left = st.button("left")
        right = st.button("right")

        if forward:
            st.write("Flying direct: going forward (positive pitch)")
            mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=duration)
    
        if backward:
            st.write("Flying direct: going backwards (negative pitch)")
            mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=duration)

        if left:
            st.write("Flying direct: roll left")
            mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=duration)

        if right:
            st.write("Flying direct: roll right")
            mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=duration)


        #print("Showing turning (in place) using turn_degrees")
        #mambo.turn_degrees(90)
        #mambo.smart_sleep(2)
        #mambo.turn_degrees(-90)
        #mambo.smart_sleep(2)
    
        #print("Flying direct: yaw")
        #mambo.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0, duration=1)
    
        up = st.button("Up")
        if up:
            st.write("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

        down = st.button("Down")
        if down:
            st.write("Flying direct: going down")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=1)

    
        #print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
        #mambo.fly_direct(roll=25, pitch=0, yaw=50, vertical_movement=0, duration=3)
    
        landing = st.button("land")

        if landing:
            print("landing")
            mambo.safe_land(5)
            mambo.smart_sleep(5)
    
            print("disconnect")
            mambo.disconnect()

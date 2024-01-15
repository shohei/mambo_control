import streamlit as st

st.title("Mambo control")

mamboAddr = "d0:3a:aa:30:e6:5a"
st.text("Mambo address: "+mamboAddr)

i = st.empty()

duration=0.5
connect = st.button("Connect")

if connect:
    # get the state information
    i.write("sleeping")
    i.write("taking off!")

forward = st.button("forward")
if forward:
    i.write("Flying direct: going forward (positive pitch)")

backward = st.button("backward")
left = st.button("left")
right = st.button("right")
up = st.button("Up")
down = st.button("Down")

if backward:
    st.write("Flying direct: going backwards (negative pitch)")

if left:
    st.write("Flying direct: roll left")

if right:
    st.write("Flying direct: roll right")

if up:
    st.write("Flying direct: going up")

if down:
    st.write("Flying direct: going down")

#print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
#mambo.fly_direct(roll=25, pitch=0, yaw=50, vertical_movement=0, duration=3)

landing = st.button("land")

if landing:
    print("landing")

    print("disconnect")

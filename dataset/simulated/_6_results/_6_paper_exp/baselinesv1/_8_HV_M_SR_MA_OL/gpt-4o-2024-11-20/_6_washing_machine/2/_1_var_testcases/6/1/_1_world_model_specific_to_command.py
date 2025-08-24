# The current code correctly models the following relevant appliance features: 
# - Power on/off feature: feature_list["power_on_off"]
# - Selecting washing program: feature_list["select_program"]
# - Adjusting load size: feature_list["adjust_load_size"]
# - Adjusting wash time: feature_list["adjust_wash_time"]
# - Adjusting rinse times: feature_list["adjust_rinse_times"]
# - Adjusting spin time: feature_list["adjust_spin_time"]
# - Starting the cycle: feature_list["start_pause_cycle"]

# Sequence of features needed to achieve the user command:
# 1. Power up the washer:
#    Raw Manual Text: "Step 1: Power on your washer. Press the ON/OFF button to power your wash on."
#    Feature List Name: "power_on_off"
# 2. Select 'Heavy' program:
#    Raw Manual Text: "Press this button to select your desired washing program."
#    Feature List Name: "select_program"
# 3. Set load size to small:
#    Raw Manual Text: "Press this button to set your washing load size. Your water level throughout all steps in the cycle."
#    Feature List Name: "adjust_load_size"
# 4. Set wash time to 5 minutes:
#    Raw Manual Text: "Continuously pressing the washing button to select washing time."
#    Feature List Name: "adjust_wash_time"
# 5. Rinse once:
#    Raw Manual Text: "Press the button to select the times of rinse. (1-3 times, or no rinse process)"
#    Feature List Name: "adjust_rinse_times"
# 6. Spin for 8 minutes:
#    Raw Manual Text: "Press the button to select the time of spin. (3-9 minutes or no spin process)"
#    Feature List Name: "adjust_spin_time"
# 7. Start the washing:
#    Raw Manual Text: "Press the START/PAUSE button to start the washing cycle."
#    Feature List Name: "start_pause_cycle"

# The goal variable values to achieve this command:
# - variable_power_on_off: "on"
# - variable_program: "Heavy"
# - variable_load_size: "1---small"
# - variable_wash_time: 5
# - variable_rinse_times: 1
# - variable_spin_time: 8
# - variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass
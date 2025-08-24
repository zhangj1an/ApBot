# The current code has accurately modeled the features to achieve the user command based on the user manual. 
# Below is the sequence of features required to achieve the command:

# Sequence of Features:
# 1. "power_on_off" to turn the washing machine on.
# 2. "adjust_program" to set it to Soak mode.
# 3. "adjust_wash_time" to set washing time to 18 minutes.
# 4. "adjust_water_level" to set water level to 30 L.
# 5. "adjust_spin_time" to set spin time to 3 minutes.
# 6. "adjust_rinse_type" to set rinse type to "Normal Rinse 2 times".
# 7. "start_pause" to start the washing machine.

# Quoted User Manual Text:
# 1. **Power button**: "Press this button to switch power on and off."
# 2. **Program button**: "Selects programs. The program changes each time the button is pressed."
# 3. **Wash button**: "Changes the washing time. The washing time can be set between 3 and 18 minutes."
# 4. **Water Level button**: "Changes the water level. You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
# 5. **Spin button**: "Changes the spin time. The spin time can be set between 1 and 9 minutes."
# 6. **Rinse button**: "Changes the number and type of rinses. Each time you press the Rinse button the setting changes in sequence, from Normal Rinse 2 times, Water-Injection Rinse 2 times, no rinsing, Normal Rinse 1 time, Water-Injection Rinse 1 time."
# 7. **Start/Pause button**: "Starts and pauses operation."

# Feature List Names in the Given Code:
# - "power_on_off"
# - "adjust_program"
# - "adjust_wash_time"
# - "adjust_water_level"
# - "adjust_spin_time"
# - "adjust_rinse_type"
# - "start_pause"

# Goal Variable Values to Achieve the Command:
# 1. Set variable_power_on_off to "on".
# 2. Set variable_program to "P5 (Soak)".
# 3. Set variable_washing_time to 18.
# 4. Set variable_water_level to 30.
# 5. Set variable_spin_time to 3.
# 6. Set variable_rinse_type to "Normal Rinse 2 times".
# 7. Set variable_start_running to "start".

class ExtendedSimulator(Simulator): 
    pass
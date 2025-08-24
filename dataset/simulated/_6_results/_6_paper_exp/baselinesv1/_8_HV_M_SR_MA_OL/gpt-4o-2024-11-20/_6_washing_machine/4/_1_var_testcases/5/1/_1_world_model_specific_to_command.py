# User command: Turn on the machine and choose the Tub Clean program for a maximum water level with rinse setting to be 'Normal Rinse 1 time' and a wash time of 3 minutes, then start the machine running.

# Based on the user manual and current implementation:
# 1. The feature_list correctly models the function to toggle power (feature_list["power_on_off"]).
# 2. The feature_list correctly models the program selection (feature_list["adjust_program"]), rinse setting (feature_list["adjust_rinse_type"]), washing time (feature_list["adjust_wash_time"]), and starting the machine ("start_pause").
# 3. The water level adjustment (feature_list["adjust_water_level"]) allows setting the water level to the maximum.
# 4. All relevant variables are present, and no missing features are identified in the user manual.

# Features sequence to achieve the task:
# 1. Use `power_on_off` to turn on the machine.
# 2. Use `adjust_program` to set the program to "P6 (Tub Clean)".
# 3. Use `adjust_water_level` to set water level to maximum (59 L).
# 4. Use `adjust_rinse_type` to set rinse type to "Normal Rinse 1 time".
# 5. Use `adjust_wash_time` to set wash time to 3 minutes.
# 6. Use `start_pause` to start the machine running.

# Relevant user manual text:
# - "**Power on/off**: Press this button to switch power on and off. The washing machine automatically switches off when operations are finished." (for power toggle).
# - "**Program button**: Selects programs. The program changes each time the button is pressed." (for program selection).
# - "**Water Level button**: Changes the water level." (for water level adjustment).
# - "**Rinse button**: Changes the number and type of rinses." (for rinse settings).
# - "**Wash button**: Changes the washing time. The washing time can be set between 3 and 18 minutes." (for wash time).
# - "**Start/Pause button**: Starts and pauses operation." (for starting the machine).

# Goal variable states:
# - `variable_power_on_off` = "on"
# - `variable_program` = "P6 (Tub Clean)"
# - `variable_water_level` = 59
# - `variable_rinse_type` = "Normal Rinse 1 time"
# - `variable_washing_time` = 3
# - `variable_start_running` = "start"

class ExtendedSimulator(Simulator):
    pass
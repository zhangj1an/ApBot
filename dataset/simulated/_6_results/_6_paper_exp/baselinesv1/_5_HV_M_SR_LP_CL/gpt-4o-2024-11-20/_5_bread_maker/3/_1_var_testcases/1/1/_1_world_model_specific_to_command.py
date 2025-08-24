# The user command is to bake Basic White Bread. Adjusting the settings according to the command includes:
# 1. Setting the cycle to 'Basic'.
# 2. Choosing 'Light' crust color.
# 3. Choosing the loaf size '2-lb'.
# 4. Setting the delay timer to 2 hours.
# 5. Starting the bread maker.

# Raw user manual text describing the required features:
# 1. "Press CYCLE button until desired program number appears on the digital display." Relevant feature: "select_cycle".
# 2. "Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust." Relevant feature: "adjust_crust_color".
# 3. "Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size." Relevant feature: "adjust_loaf_size".
# 4. "Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display." Relevant feature: "adjust_delay_timer".
# 5. "Press START/STOP. The digital display will show the time remaining in the cycle." Relevant feature: "start_or_stop_operation".

# Verification of the current code correctness:
# The current code models all the required features accurately. Each feature is represented with necessary steps, actions, and variable mappings:
# - "select_cycle" allows cycling through program options.
# - "adjust_crust_color" allows selecting the crust color.
# - "adjust_loaf_size" allows selecting the size of the loaf.
# - "adjust_delay_timer" allows modifying the delay timer via + and - buttons.
# - "start_or_stop_operation" toggles whether the bread maker starts running (on/off).

# Goal variable values to achieve the user command:
# - Set `variable_cycle` to "Basic".
# - Set `variable_crust_color` to "Light".
# - Set `variable_loaf_size` to "2.0lb".
# - Set `variable_delay_timer` to 120 minutes (2 hours).
# - Set `variable_start_running` to "on" to start the bread maker.

class ExtendedSimulator(Simulator):
    pass
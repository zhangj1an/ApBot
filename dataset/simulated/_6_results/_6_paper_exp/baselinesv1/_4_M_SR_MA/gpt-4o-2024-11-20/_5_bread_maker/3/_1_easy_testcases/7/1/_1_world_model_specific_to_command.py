# The given code correctly models the user manual's features relevant to the user command. 
# The sequence of features needed to achieve the command "Bake Whole Grain Bread. Set the cycle to 'Whole Grain'. Choose 'Dark' crust color. Choose loaf size '2-lb'. Set the delay timer to 4 hours. Start the bread maker." is as follows:

# 1. select_cycle: To set the cycle to "Whole Grain."
# Raw user manual text: "Press CYCLE button to select your desired cycle. The corresponding cycle number is shown on the display."
# Feature: feature_list["select_cycle"]

# 2. adjust_crust_color: To set the crust color to "Dark."
# Raw user manual text: "Press CRUST button to move the arrow to desired setting: Light, Medium, or Dark crust. (Crust is not adjustable in Cycles 6, 7, 8, 9, and 10)."
# Feature: feature_list["adjust_crust_color"]

# 3. adjust_loaf_size: To choose the loaf size "2-lb."
# Raw user manual text: "Press the LOAF SIZE button to move the arrow to 1.5- or 2-lb. loaf size. (Loaf size is not an option in Cycles 6, 7, 8, 9, 10, and 11)."
# Feature: feature_list["adjust_loaf_size"]

# 4. adjust_delay_timer: To set the delay timer to 4 hours (240 minutes).
# Raw user manual text: "Use the Delay Timer feature to start the breadmaker at a later time. Press the + and – buttons to increase the cycle time shown on the display. Add up to 13 hours including the delay time and breadmaking cycle."
# Feature: feature_list["adjust_delay_timer"]

# 5. start_or_stop_operation: To start the bread maker.
# Raw user manual text: "Press START/STOP. The digital display will show the time remaining in the cycle."
# Feature: feature_list["start_or_stop_operation"]

# Goal variable values to achieve the command:
# set variable_cycle to "Whole Grain"
# set variable_crust_color to "Dark"
# set variable_loaf_size to "2.0lb"
# set variable_delay_timer to 240
# set variable_start_running to "on"

class ExtendedSimulator(Simulator): 
    pass
# Python comments below to verify correctness against the user manual:
# The user manual provides the following steps for the user command:
# 1. Select the Ultra Fast-2 program: The user manual specifies using the "Menu Selector" button to select the desired program.
#    Relevant feature: "set_menu"
#    Relevant feature list section: feature_list["set_menu"]
# 2. Choose a loaf size of 900g: The user manual specifies pressing the "Loaf Size Selector" button to select the desired loaf size.
#    Relevant feature: "set_loaf_size"
#    Relevant feature list section: feature_list["set_loaf_size"]
# 3. Set the crust color to Dark: The user manual specifies pressing the "Colour Button" to select the crust color.
#    Relevant feature: "set_crust_color"
#    Relevant feature list section: feature_list["set_crust_color"]
# 4. Set the delay timer to 5 hours: The user manual specifies adjusting the delay timer using time "+" and "-" buttons.
#    Relevant feature: "set_delay_timer"
#    Relevant feature list section: feature_list["set_delay_timer"]
# 5. Power on and start the bread maker operation: The user manual specifies pressing the "Start/Stop" button to toggle between starting and stopping the program.
#    Relevant feature: "start_stop_program"
#    Relevant feature list section: feature_list["start_stop_program"]

# Sequence of features to achieve user command:
# - Feature 1: "set_menu" - Set program to "Ultra Fast-2" (program 7).
# - Feature 2: "set_loaf_size" - Set loaf size to "900g".
# - Feature 3: "set_crust_color" - Set crust color to "Dark".
# - Feature 4: "set_delay_timer" - Set delay timer to 5 hours.
# - Feature 5: "start_stop_program" - Start the bread maker.

# Goal variable values:
# variable_menu_index = "7"
# variable_loaf_size = "900g"
# variable_crust_color = "Dark"
# variable_delay_timer = 300 (5 hours expressed in minutes)
# variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass
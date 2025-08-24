# Python comment: The current code correctly models the relevant appliance features to achieve the command. 
# Below is the sequence of features, the corresponding user manual text, and assigned feature_list names:
# 
# 1. **Make soup** -> Select soup mode using the "Menu" option.
#    User manual text: "_Press the 'Menu' button to select the desired function._"
#    Feature_list name: `select_menu_option`
#
# 2. **Set preset timer to 4 hours** -> Adjust the preset timer on the device.
#    User manual text: "_Press the 'Preset timer' button. Press the 'Hr.' and 'Min.' buttons to set the desired time._"
#    Feature_list name: `set_preset_timer`
#
# 3. **Start cooking** -> Start the cooking process.
#    User manual text: "_Press the 'Start' button._"
#    Feature_list name: `start_cooking`
#
# Goal variable values:
# - `variable_menu_index`: "Soup"
# - `variable_preset_timer_hours`: 4
# - `variable_preset_timer_minutes`: 0
# - `variable_start_cooking`: "on"

class ExtendedSimulator(Simulator):
    pass
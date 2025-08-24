# The previous code has missed the following from the user manual:
# 1. In "Start Baking" section of the user manual:
#    "The appliance will automatically be set to the BASIC programme with the crust setting at MEDIUM."
#    But the current code does not reflect this automatic initialization upon turning on.
#    Additionally, when "press_start_stop_button" is used (to begin or cancel a programme), the feature implementation does not explicitly initialize variable_menu_index to "1" and variable_crust_color to "Medium".
# 2. The crust color setting is only allowed for programmes 1-7 (BASIC to ULTRA FAST-2) as per the Programme Guide. The current model allows crust color adjustment for all 12 programmes, which contradicts the user manual.

# The following changes are implemented:
# Adjust the logic for initializing default settings when the appliance is powered/started.
# Limit the valid actions for setting crust color depending on the value of variable_menu_index.

updated_feature_list = feature_list

# Updated feature for adjusting crust color (with validation for allowed programmes)
updated_feature_list["set_crust_color"] = [
    {"step": 1, "actions": ["press_color_button"], "variable": "variable_crust_color",
     "comment": "Crust color can only be adjusted for Programmes 1-7"}
]

class ExtendedSimulator(Simulator):

    def reset(self):
        super().reset()  # Inherit attributes from Simulator class
        self.feature = Feature(feature_list=updated_feature_list, current_value=("empty", 1))

    def press_start_stop_button(self):
        # Modify the action to auto-set default values for menu (to BASIC) and crust color (to Medium) as per user manual.
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop_program":
            # Toggle the "variable_start_running" and apply defaults
            new_value = "on" if self.variable_start_running.get_current_value() == "off" else "off"
            self.variable_start_running.set_current_value(new_value)
            if new_value == "on":
                # Automatically set menu index to BASIC and crust color to Medium
                self.variable_menu_index.set_current_value("1")  # BASIC = "1"
                self.variable_crust_color.set_current_value("Medium")

    def press_color_button(self):
        # Adjust crust color only for Programmes 1-7 per the user manual.
        self.feature.update_progress("press_color_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "set_crust_color":
            # Restrict crust color adjustment to Programmes 1-7
            menu_index = int(self.variable_menu_index.get_current_value())
            if 1 <= menu_index <= 7:
                self.execute_action_and_set_next("press_color_button")
            else:
                self.display = "Crust color setting is only available for Programmes 1-7."

class_instance = ExtendedSimulator()
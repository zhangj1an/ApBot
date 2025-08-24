class Simulator(Appliance):

    def reset(self):
        # Initialize feature and variables
        self.feature = simulator_feature
        self.variable_start_running = variable_start_running
        self.variable_power = variable_power
        self.variable_clock = variable_clock
        self.variable_timer = variable_timer
        self.variable_time_cook_time = variable_time_cook_time
        self.variable_weight_defrost = variable_weight_defrost
        self.variable_time_defrost = variable_time_defrost
        self.variable_menu_index = variable_menu_index
        self.variable_menu_setting = variable_menu_setting
        self.variable_menu_setting_popcorn = variable_menu_setting_popcorn
        self.variable_menu_setting_potato = variable_menu_setting_potato
        self.variable_menu_setting_frozen_vegetable = variable_menu_setting_frozen_vegetable
        self.variable_menu_setting_beverage = variable_menu_setting_beverage
        self.variable_menu_setting_dinner_plate = variable_menu_setting_dinner_plate
        self.variable_menu_setting_pizza = variable_menu_setting_pizza
        self.menu_setting_dict = menu_setting_dict
        self.variable_child_lock = variable_child_lock
        self.variable_input_string = InputString()
        self.meta_actions_dict = meta_actions_dict
        self.meta_actions_on_number = meta_actions_on_number

    def process_input_string(self, intended_feature, variable_name):
        # Convert input string to variable value based on feature and variable
        raw_input = self.variable_input_string.input_string
        value = int(raw_input) if raw_input.isdigit() else 0

        if variable_name == "variable_clock" and intended_feature == "set_clock":
            # Adjust HH:MM format for clock setting
            time_string = str(value).zfill(4) + "00"
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_timer" and intended_feature == "set_kitchen_timer":
            # Adjust MM:SS format for kitchen timer
            time_string = "00" + str(value).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_time_cook_time" and intended_feature in ["microwave_cook", "speedy_cooking", "add_30_seconds"]:
            # Adjust MM:SS format for cooking time
            time_string = "00" + str(value).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_time_defrost" and intended_feature == "time_defrost":
            # Adjust MM:SS format for time defrost
            time_string = "00" + str(value).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_weight_defrost" and intended_feature == "weight_defrost":
            # Weight defrost input directly corresponds to weight
            return min(max(value, 4), 100)
        elif variable_name == "variable_menu_setting" and intended_feature == "adjust_menu_settings":
            # Menu settings directly correspond to input
            return str(value)
        elif variable_name == "variable_power" and intended_feature in ["microwave_cook", "time_defrost"]:
            # Power level input directly corresponds to PLx
            return f"PL{value}"
        return value

    def get_original_input(self, goal_string, intended_feature, variable_name):
        # Convert variable value back to input string based on feature and variable
        digits_only = ''.join(char for char in str(goal_string) if char.isdigit())

        if variable_name == "variable_clock" and intended_feature == "set_clock":
            # Extract HH:MM from HH:MM:SS
            result = digits_only[:-2].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_timer" and intended_feature == "set_kitchen_timer":
            # Extract MM:SS from HH:MM:SS
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_time_cook_time" and intended_feature in ["microwave_cook", "speedy_cooking", "add_30_seconds"]:
            # Extract MM:SS from HH:MM:SS
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_time_defrost" and intended_feature == "time_defrost":
            # Extract MM:SS from HH:MM:SS
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_weight_defrost" and intended_feature == "weight_defrost":
            # Weight defrost input directly corresponds to weight
            return str(int(goal_string))
        elif variable_name == "variable_menu_setting" and intended_feature == "adjust_menu_settings":
            # Menu settings directly correspond to input
            return str(int(goal_string))
        elif variable_name == "variable_power" and intended_feature in ["microwave_cook", "time_defrost"]:
            # Extract power level from PLx
            return goal_string.replace("PL", "")
        return digits_only

    def press_clock_button(self):
        # Adjust clock setting feature
        self.feature.update_progress("press_clock_button")

    def press_timer_button(self):
        # Adjust kitchen timer feature
        self.feature.update_progress("press_timer_button")

    def press_time_cook_button(self):
        # Adjust microwave cooking time
        self.feature.update_progress("press_time_cook_button")

    def press_power_button(self):
        # Adjust power level
        self.feature.update_progress("press_power_button")

    def press_weight_defrost_button(self):
        # Adjust weight defrost feature
        self.feature.update_progress("press_weight_defrost_button")

    def press_time_defrost_button(self):
        # Adjust time defrost feature
        self.feature.update_progress("press_time_defrost_button")

    def press_popcorn_button(self):
        # Adjust popcorn menu
        self.feature.update_progress("press_popcorn_button")
        self.variable_menu_index.set_current_value("popcorn")
        self.variable_menu_setting = self.menu_setting_dict["popcorn"]

    def press_potato_button(self):
        # Adjust potato menu
        self.feature.update_progress("press_potato_button")
        self.variable_menu_index.set_current_value("potato")
        self.variable_menu_setting = self.menu_setting_dict["potato"]

    def press_frozen_vegetable_button(self):
        # Adjust frozen vegetable menu
        self.feature.update_progress("press_frozen_vegetable_button")
        self.variable_menu_index.set_current_value("frozen_vegetable")
        self.variable_menu_setting = self.menu_setting_dict["frozen_vegetable"]

    def press_beverage_button(self):
        # Adjust beverage menu
        self.feature.update_progress("press_beverage_button")
        self.variable_menu_index.set_current_value("beverage")
        self.variable_menu_setting = self.menu_setting_dict["beverage"]

    def press_dinner_plate_button(self):
        # Adjust dinner plate menu
        self.feature.update_progress("press_dinner_plate_button")
        self.variable_menu_index.set_current_value("dinner_plate")
        self.variable_menu_setting = self.menu_setting_dict["dinner_plate"]

    def press_pizza_button(self):
        # Adjust pizza menu
        self.feature.update_progress("press_pizza_button")
        self.variable_menu_index.set_current_value("pizza")
        self.variable_menu_setting = self.menu_setting_dict["pizza"]

    def press_start_plus_30sec_button(self):
        # Add 30 seconds or start cooking
        self.feature.update_progress("press_start_plus_30sec_button")
        current_feature = self.feature.current_value[0]
        if current_feature in ["set_kitchen_timer", "microwave_cook", "speedy_cooking", "add_30_seconds"]:
            self.variable_time_cook_time.set_current_value(
                self.variable_time_cook_time.get_current_value() + "00:00:30"
            )
        elif current_feature == "memory_function":
            self.variable_start_running.set_current_value("on")

    def press_stop_cancel_button(self):
        # Stop or cancel operation
        self.feature.update_progress("press_stop_cancel_button")
        self.variable_start_running.set_current_value("off")

    def press_and_hold_stop_cancel_button(self, duration=3):
        # Toggle child lock
        self.feature.update_progress("press_and_hold_stop_cancel_button")
        if duration >= 3:
            if self.variable_child_lock.get_current_value() == "unlocked":
                self.variable_child_lock.set_current_value("locked")
            else:
                self.variable_child_lock.set_current_value("unlocked")

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Clear input string if action is not a number button
        if action_name not in meta_actions_dict.values():
            self.variable_input_string.input_string = ""

        # Check for child lock
        if self.variable_child_lock.get_current_value() == "locked" and action_name not in ["press_stop_cancel_button", "press_and_hold_stop_cancel_button"]:
            self.display = "child lock: locked"
            return self.display

        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)
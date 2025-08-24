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
        if variable_name == "variable_clock" and intended_feature == "set_clock":
            # Time variable HH:MM:SS, only modify HH:MM
            time_string = str(raw_input).zfill(4) + "00"
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_timer" and intended_feature == "set_kitchen_timer":
            # Time variable HH:MM:SS, only modify MM:SS
            time_string = "00" + str(raw_input).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_time_cook_time" and intended_feature in ["set_microwave_cook_time_power", "speedy_cooking", "add_cook_time_plus_30sec"]:
            # Time variable HH:MM:SS, only modify MM:SS
            time_string = "00" + str(raw_input).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_weight_defrost" and intended_feature == "set_weight_defrost":
            # Continuous variable, directly parse input as weight
            return min(max(int(raw_input), 4), 100)
        elif variable_name == "variable_time_defrost" and intended_feature == "set_time_defrost":
            # Time variable HH:MM:SS, only modify MM:SS
            time_string = "00" + str(raw_input).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif variable_name == "variable_menu_setting" and intended_feature == "set_menu":
            # Menu setting, directly parse input
            return str(raw_input)
        elif variable_name == "variable_power" and intended_feature in ["set_microwave_cook_time_power", "set_time_defrost"]:
            # Power level, directly parse input
            return f"PL{int(raw_input)}"
        return raw_input

    def get_original_input(self, goal_string, intended_feature, variable_name):
        # Convert variable value back to input string based on feature and variable
        digits_only = ''.join(char for char in str(goal_string) if char.isdigit())
        if variable_name == "variable_clock" and intended_feature == "set_clock":
            # The required input is HH:MM, remove the last two digits
            result = digits_only[:-2].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_timer" and intended_feature == "set_kitchen_timer":
            # The required input is MM:SS, remove the first two digits
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_time_cook_time" and intended_feature in ["set_microwave_cook_time_power", "speedy_cooking", "add_cook_time_plus_30sec"]:
            # The required input is MM:SS, remove the first two digits
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_weight_defrost" and intended_feature == "set_weight_defrost":
            # Continuous variable, directly return the weight
            return str(int(goal_string))
        elif variable_name == "variable_time_defrost" and intended_feature == "set_time_defrost":
            # The required input is MM:SS, remove the first two digits
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif variable_name == "variable_menu_setting" and intended_feature == "set_menu":
            # Menu setting, directly return the value
            return str(goal_string)
        elif variable_name == "variable_power" and intended_feature in ["set_microwave_cook_time_power", "set_time_defrost"]:
            # Power level, extract the last digit
            return goal_string[-1]
        return digits_only

    def press_clock_button(self):
        # Adjust clock setting
        self.feature.update_progress("press_clock_button")

    def press_timer_button(self):
        # Adjust kitchen timer
        self.feature.update_progress("press_timer_button")

    def press_time_cook_button(self):
        # Adjust microwave cooking time and power
        self.feature.update_progress("press_time_cook_button")

    def press_power_button(self):
        # Adjust power level
        self.feature.update_progress("press_power_button")

    def press_start_plus_30sec_button(self):
        # Start cooking or add 30 seconds to cooking time
        self.feature.update_progress("press_start_plus_30sec_button")
        current_feature = self.feature.current_value[0]
        if current_feature in ["set_microwave_cook_time_power", "speedy_cooking", "add_cook_time_plus_30sec"]:
            self.variable_start_running.set_current_value("on")
        elif current_feature in ["set_kitchen_timer"]:
            self.variable_timer.set_current_value("00:00:00")

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

    def press_weight_defrost_button(self):
        # Adjust weight defrost
        self.feature.update_progress("press_weight_defrost_button")

    def press_time_defrost_button(self):
        # Adjust time defrost
        self.feature.update_progress("press_time_defrost_button")

    def press_popcorn_button(self):
        # Set popcorn menu
        self.feature.update_progress("press_popcorn_button")
        self.variable_menu_index.set_current_value("popcorn")
        self.variable_menu_setting = self.menu_setting_dict["popcorn"]

    def press_potato_button(self):
        # Set potato menu
        self.feature.update_progress("press_potato_button")
        self.variable_menu_index.set_current_value("potato")
        self.variable_menu_setting = self.menu_setting_dict["potato"]

    def press_frozen_vegetable_button(self):
        # Set frozen vegetable menu
        self.feature.update_progress("press_frozen_vegetable_button")
        self.variable_menu_index.set_current_value("frozen_vegetable")
        self.variable_menu_setting = self.menu_setting_dict["frozen_vegetable"]

    def press_beverage_button(self):
        # Set beverage menu
        self.feature.update_progress("press_beverage_button")
        self.variable_menu_index.set_current_value("beverage")
        self.variable_menu_setting = self.menu_setting_dict["beverage"]

    def press_dinner_plate_button(self):
        # Set dinner plate menu
        self.feature.update_progress("press_dinner_plate_button")
        self.variable_menu_index.set_current_value("dinner_plate")
        self.variable_menu_setting = self.menu_setting_dict["dinner_plate"]

    def press_pizza_button(self):
        # Set pizza menu
        self.feature.update_progress("press_pizza_button")
        self.variable_menu_index.set_current_value("pizza")
        self.variable_menu_setting = self.menu_setting_dict["pizza"]

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Reset input string if the action is not a number button
        if action_name not in meta_actions_dict.values():
            self.variable_input_string.input_string = ""

        # Check for child lock
        if self.variable_child_lock.get_current_value() == "locked" and action_name not in ["press_stop_cancel_button", "press_and_hold_stop_cancel_button"]:
            self.display = "child lock: locked"
            return self.display

        # Execute the action
        return super().run_action(action_name, execution_times, **kwargs)
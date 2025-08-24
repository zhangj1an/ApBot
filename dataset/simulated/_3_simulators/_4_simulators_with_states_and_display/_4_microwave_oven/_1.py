# 15 variables

# Variable for clock setting
variable_clock = TimeVariable(value_ranges_steps=[("00:00:00", "12:59:00", 60)], current_value="00:00:00")

# Variable for kitchen timer
variable_kitchen_timer = TimeVariable(value_ranges_steps=[("00:00:00", "99:99:00", 1)], current_value="00:00:00")

# Variable for microwave cooking time
variable_microwave_cooking_time = TimeVariable(value_ranges_steps=[("00:00:00", "99:99:00", 1)], current_value="00:00:00")

# Variable for microwave power level
variable_microwave_power_level = DiscreteVariable(value_range=["PL0", "PL1", "PL2", "PL3", "PL4", "PL5", "PL6", "PL7", "PL8", "PL9", "PL10"], current_value="PL10")

# Variable for weight defrost
variable_weight_defrost = ContinuousVariable(value_ranges_steps=[(0, 4, 4), (4, 100, 1)], current_value=0)

# Variable for time defrost
variable_time_defrost = TimeVariable(value_ranges_steps=[("00:00:00", "99:99:00", 1)], current_value="00:00:00")

# Variable for popcorn setting
variable_popcorn_setting = DiscreteVariable(value_range=["1.75", "3.0", "3.5"], current_value="1.75")

# Variable for potato setting
variable_potato_setting = DiscreteVariable(value_range=["1", "2", "3"], current_value="1")

# Variable for frozen vegetable setting
variable_frozen_vegetable_setting = DiscreteVariable(value_range=["4.0", "8.0", "16.0"], current_value="4.0")

# Variable for beverage setting
variable_beverage_setting = DiscreteVariable(value_range=["1", "2", "3"], current_value="1")

# Variable for dinner plate setting
variable_dinner_plate_setting = DiscreteVariable(value_range=["9.0", "12.0", "18.0"], current_value="9.0")

# Variable for pizza setting
variable_pizza_setting = DiscreteVariable(value_range=["4.0", "8.0", "14.0"], current_value="4.0")

# Variable for child lock
variable_child_lock = DiscreteVariable(value_range=["locked", "unlocked"], current_value="unlocked")

# Variable for start running
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Input string for number pads
variable_input_string = InputString()

feature_list = {}

feature_list["clock_setting"] = [
    {"step": 1, "actions": ["press_clock_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_clock"},  # requires parsing from variable_input_string
    {"step": 3, "actions": ["press_clock_button"]}
]

feature_list["kitchen_timer"] = [
    {"step": 1, "actions": ["press_timer_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_kitchen_timer"},  # requires parsing from variable_input_string
    {"step": 3, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["microwave_cook"] = [
    {"step": 1, "actions": ["press_time_cook_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_microwave_cooking_time"},  # requires parsing from variable_input_string
    {"step": 3, "actions": ["press_power_button"]},
    {"step": 4, "actions": meta_actions_on_number, "variable": "variable_microwave_power_level"},
    {"step": 5, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["speedy_cooking"] = [
    {"step": 1, "actions": meta_actions_on_number, "variable": "variable_microwave_cooking_time"},  # requires parsing from variable_input_string
    {"step": 2, "actions": ["press_start_plus_30sec_button"],  "variable": "variable_start_running", "comment": "variable_start_running: set to on", "step_size": 2}
]

feature_list["weight_defrost"] = [
    {"step": 1, "actions": ["press_weight_defrost_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_weight_defrost"},  # requires parsing from variable_input_string
    {"step": 3, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["time_defrost"] = [
    {"step": 1, "actions": ["press_time_defrost_button"]},
    {"step": 2, "actions": meta_actions_on_number, "variable": "variable_time_defrost"},  # requires parsing from variable_input_string
    {"step": 3, "actions": ["press_power_button"]},
    {"step": 4, "actions": meta_actions_on_number, "variable": "variable_microwave_power_level"},
    {"step": 5, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["popcorn"] = [
    {"step": 1, "actions": ["press_popcorn_button"], "variable": "variable_popcorn_setting", "step_size": 3},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["potato"] = [
    {"step": 1, "actions": ["press_potato_button"], "variable": "variable_potato_setting", "step_size": 3},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["frozen_vegetable"] = [
    {"step": 1, "actions": ["press_frozen_vegetable_button"], "variable": "variable_frozen_vegetable_setting", "step_size": 3},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["beverage"] = [
    {"step": 1, "actions": ["press_beverage_button"], "variable": "variable_beverage_setting", "step_size": 3},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["dinner_plate"] = [
    {"step": 1, "actions": ["press_dinner_plate_button"], "variable": "variable_dinner_plate_setting", "step_size": 3},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["pizza"] = [
    {"step": 1, "actions": ["press_pizza_button"], "variable": "variable_pizza_setting", "step_size": 3},
    {"step": 2, "actions": ["press_start_plus_30sec_button"], "variable": "variable_start_running", "step_size": 2}
]

feature_list["child_lock"] = [
    {"step": 1, "actions": ["press_and_hold_stop_cancel_button"], "variable": "variable_child_lock", "step_size": 2}
]

feature_list["stop_cancel"] = [
    {"step": 1, "actions": ["press_stop_cancel_button"]}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_clock = variable_clock
        self.variable_kitchen_timer = variable_kitchen_timer
        self.variable_microwave_cooking_time = variable_microwave_cooking_time
        self.variable_microwave_power_level = variable_microwave_power_level
        self.variable_weight_defrost = variable_weight_defrost
        self.variable_time_defrost = variable_time_defrost
        self.variable_popcorn_setting = variable_popcorn_setting
        self.variable_potato_setting = variable_potato_setting
        self.variable_frozen_vegetable_setting = variable_frozen_vegetable_setting
        self.variable_beverage_setting = variable_beverage_setting
        self.variable_dinner_plate_setting = variable_dinner_plate_setting
        self.variable_pizza_setting = variable_pizza_setting
        self.variable_child_lock = variable_child_lock
        self.variable_start_running = variable_start_running
        self.variable_input_string = variable_input_string
        self.meta_actions_dict = meta_actions_dict
        self.meta_actions_on_number = meta_actions_on_number

    def press_clock_button(self):
        # Update feature progress and set clock time
        self.feature.update_progress("press_clock_button")

    def press_timer_button(self):
        # Update feature progress and set kitchen timer
        self.feature.update_progress("press_timer_button")

    def press_time_cook_button(self):
        # Update feature progress and set microwave cooking time
        self.feature.update_progress("press_time_cook_button")

    def press_power_button(self):
        # Update feature progress and set microwave power level
        self.feature.update_progress("press_power_button")

    def press_weight_defrost_button(self):
        # Update feature progress and set weight defrost
        self.feature.update_progress("press_weight_defrost_button")

    def press_time_defrost_button(self):
        # Update feature progress and set time defrost
        self.feature.update_progress("press_time_defrost_button")

    def press_popcorn_button(self):
        # Update feature progress and set popcorn setting
        self.feature.update_progress("press_popcorn_button")

    def press_potato_button(self):
        # Update feature progress and set potato setting
        self.feature.update_progress("press_potato_button")

    def press_frozen_vegetable_button(self):
        # Update feature progress and set frozen vegetable setting
        self.feature.update_progress("press_frozen_vegetable_button")

    def press_beverage_button(self):
        # Update feature progress and set beverage setting
        self.feature.update_progress("press_beverage_button")

    def press_dinner_plate_button(self):
        # Update feature progress and set dinner plate setting
        self.feature.update_progress("press_dinner_plate_button")

    def press_pizza_button(self):
        # Update feature progress and set pizza setting
        self.feature.update_progress("press_pizza_button")

    def press_start_plus_30sec_button(self):
        # Update feature progress and start cooking
        self.feature.update_progress("press_start_plus_30sec_button")
        self.variable_start_running.set_current_value("on")

    def press_stop_cancel_button(self):
        # Update feature progress and stop/cancel operation
        self.feature.update_progress("press_stop_cancel_button")

    def press_and_hold_stop_cancel_button(self, duration=3):
        # Update feature progress and toggle child lock
        self.feature.update_progress("press_and_hold_stop_cancel_button")
        if duration >= 3:
            if self.variable_child_lock.get_current_value() == "unlocked":
                self.variable_child_lock.set_current_value("locked")
            else:
                self.variable_child_lock.set_current_value("unlocked")

    def process_input_string(self, intended_feature, variable_name):
        raw_input = self.variable_input_string.input_string
        if (variable_name == "variable_clock" and intended_feature == "clock_setting"):
            # Time variable HH:MM, modify HH:MM
            time_string = str(raw_input).zfill(4) + "00"
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif (variable_name == "variable_kitchen_timer" and intended_feature == "kitchen_timer"):
            # Time variable MM:SS, modify MM:SS
            time_string = "00" + str(raw_input).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif (variable_name == "variable_microwave_cooking_time" and intended_feature in ["microwave_cook", "speedy_cooking"]):
            # Time variable MM:SS, modify MM:SS
            time_string = "00" + str(raw_input).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif (variable_name == "variable_weight_defrost" and intended_feature == "weight_defrost"):
            # Continuous variable, modify weight
            return float(raw_input)
        elif (variable_name == "variable_time_defrost" and intended_feature == "time_defrost"):
            # Time variable MM:SS, modify MM:SS
            time_string = "00" + str(raw_input).zfill(4)
            return f"{time_string[:2]}:{time_string[2:4]}:{time_string[4:]}"
        elif (variable_name == "variable_microwave_power_level" and intended_feature in ["microwave_cook", "time_defrost"]):
            # Discrete variable, modify power level
            return f"PL{int(raw_input)}"
        return raw_input

    def get_original_input(self, goal_string, intended_feature, variable_name):
        digits_only = ''.join(char for char in str(goal_string) if char.isdigit())
        if (variable_name == "variable_clock" and intended_feature == "clock_setting"):
            # The required input is HH:MM, remove the last two digits
            result = digits_only[:-2].lstrip('0')
            return result if result else '0'
        elif (variable_name == "variable_kitchen_timer" and intended_feature == "kitchen_timer"):
            # The required input is MM:SS, remove the first two digits
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif (variable_name == "variable_microwave_cooking_time" and intended_feature in ["microwave_cook", "speedy_cooking"]):
            # The required input is MM:SS, remove the first two digits
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif (variable_name == "variable_weight_defrost" and intended_feature == "weight_defrost"):
            # Continuous variable, return as is
            return str(int(float(goal_string)))
        elif (variable_name == "variable_time_defrost" and intended_feature == "time_defrost"):
            # The required input is MM:SS, remove the first two digits
            result = digits_only[2:].lstrip('0')
            return result if result else '0'
        elif (variable_name == "variable_microwave_power_level" and intended_feature in ["microwave_cook", "time_defrost"]):
            # Discrete variable, return the last digit
            return digits_only[-1]
        return digits_only

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Clear input string if not adjusting input
        if action_name not in meta_actions_dict.values():
            self.variable_input_string.input_string = ""

        # Check child lock
        if self.variable_child_lock.get_current_value() == "locked" and action_name not in ["press_stop_cancel_button", "press_and_hold_stop_cancel_button"]:
            self.display = "child lock: locked"
            return self.display

        # Execute action
        return super().run_action(action_name, execution_times, **kwargs)
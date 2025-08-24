import sys 
sys.path.append("/data/home/jian/RLS_microwave/utils")
from _5_build_world_model._0_logic_units import DiscreteVariable, ContinuousVariable, Appliance, Mode, TimeVariable

class PiecewiseTimeVariable(TimeVariable):
    def __init__(self, value_range=None, current_value=None, step_value=None):
        super().__init__(value_range=value_range, current_value=current_value, step_value=step_value)
        self.conditional_steps = []
        # Adding conditional steps for microwave cooking time
        self.add_conditional_step(lambda x: self.convert_to_seconds(x) < 60, 5)
        self.add_conditional_step(lambda x: 60 <= self.convert_to_seconds(x) < 300, 10)
        self.add_conditional_step(lambda x: 300 <= self.convert_to_seconds(x) < 600, 30)
        self.add_conditional_step(lambda x: 600 <= self.convert_to_seconds(x) < 1800, 60)
        self.add_conditional_step(lambda x: 1800 <= self.convert_to_seconds(x) <= 5700, 300)

    

class VariableAutoMenuFoodWeight(DiscreteVariable):
    def __init__(self):
        self.primary_categories = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8"]
        self.value_ranges = {
            "A-1": [200, 400],
            "A-2": [250, 350, 450],
            "A-3": [200, 300, 400],
            "A-4": [50, 100],
            "A-5": [200, 400, 600],
            "A-6": [250, 350, 450],
            "A-7": [1, 2, 3],
            "A-8": [50, 85, 100]
        }
        self.primary_category = "A-1"
        super().__init__(self.value_ranges[self.primary_category])

    def update_value_range(self, menu_code):
        if menu_code in self.value_ranges:
            self.primary_category = menu_code
            self.set_value_range(self.value_ranges[menu_code])

    def compare(self, other):
        if not isinstance(other, VariableAutoMenuFoodWeight):
            raise ValueError("Can only compare with another VariableAutoMenuFoodWeight instance")

        primary_index_self = self.primary_categories.index(self.primary_category)
        primary_index_other = other.primary_categories.index(other.primary_category)

        # Normalize the primary index difference
        primary_diff = abs(primary_index_self - primary_index_other)
        max_primary_index = len(self.primary_categories) - 1
        normalized_primary_diff = primary_diff / max_primary_index if max_primary_index != 0 else 0

        # If there's a difference in the primary category, the secondary difference is set to 1
        if normalized_primary_diff > 0:
            normalized_secondary_diff = 1
        else:
            # Compare the indices within the value range
            secondary_index_diff = abs(self.value_index - other.value_index)

            # Normalize the secondary index difference
            max_secondary_index = len(self.value_range) - 1
            normalized_secondary_diff = secondary_index_diff / max_secondary_index if max_secondary_index != 0 else 0

        return normalized_secondary_diff

class MicrowaveMode(Mode):
    def __init__(self, mode_list, current_value=("empty", 1)):
        super().__init__(mode_list, current_value)
        self.two_stages = DiscreteVariable(value_range=[False, True], current_value=False)

    def switch_mode(self, button_name):
        if self.current_value != ("empty", 1):
            mode = self.current_value[0]
            step = self.current_value[1] 
            controls = self.get_actions(mode, step + 1)
            if controls is not None: 
                if button_name in controls:
                    self.current_value = (mode, step + 1) 
                    return  
            
            if mode != "auto_menu" and step == len(self.mode_list[mode]) - 1 and self.two_stages.get_current_value() == False:
                for new_mode in self.mode_list.keys():
                    if new_mode != "auto_menu" and button_name in self.get_actions(new_mode, 1):
                        self.current_value = (new_mode, 1)
                        self.two_stages.set_current_value(True)
                        return
        else:
            for mode in self.mode_list.keys():
                if button_name in self.get_actions(mode, 1):
                    self.current_value = (mode, 1)
    
    
mode_list = {
    "empty": [{"step": 1, "actions": []} ],
    "clock_setting": [
        {"step": 1, "actions": ["press_clock_button"]},
        {"step": 2, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_clock_setting_hour"},
        {"step": 3, "actions": ["press_clock_button"]},
        {"step": 4, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_clock_setting_minute"},
        {"step": 5, "actions": ["press_clock_button"]}   
    ],
    "microwave_cooking": [
        {"step": 1, "actions": ["press_microwave_button"]},
        {"step": 2, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_microwave_cooking_power"},
        {"step": 3, "actions": ["press_start_plus30sec_confirm_button"]},
        {"step": 4, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_microwave_cooking_time"},
        {"step": 5, "actions": ["press_start_plus30sec_confirm_button"]},
        #{"step": 6, "actions": ["press_start_plus30sec_confirm_button"], "variable": "variable_microwave_cooking_time"}
    ],
    "speedy_cooking_1": [
        {"step": 1, "actions": ["press_start_plus30sec_confirm_button"], "variable": "variable_speedy_cooking_1"},
    ],
    # here the step value is 30
    "speedy_cooking_2": [
        {"step": 1, "actions": ["press_down_arrow_button"]},
        {"step": 2, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_speedy_cooking_2"},
        {"step": 3, "actions": ["press_start_plus30sec_confirm_button"]}
    ],
    # here the step value is function 

    "defrost_by_weight": [
        {"step": 1, "actions": ["press_weight_defrost_button"]},
        {"step": 2, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_defrost_weight"},
        {"step": 3, "actions": ["press_start_plus30sec_confirm_button"]}
    ],
    "defrost_by_time": [
        {"step": 1, "actions": ["press_time_defrost_button"]},
        {"step": 2, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_defrost_time"},
        {"step": 3, "actions": ["press_start_plus30sec_confirm_button"]},
        #{"step": 4, "actions": ["press_start_plus30sec_confirm_button"], "variable": "variable_microwave_cooking_time"}
    ],
    "kitchen_timer": [
        {"step": 1, "actions": ["press_kitchen_timer_button"]},
        {"step": 2, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_kitchen_timer"},
        {"step": 3, "actions": ["press_start_plus30sec_confirm_button"]}
    ],
    "auto_menu": [
        {"step": 1, "actions": ["press_up_arrow_button"]},
        {"step": 2, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_auto_menu"},
        {"step": 3, "actions": ["press_start_plus30sec_confirm_button"]},
        {"step": 4, "actions": ["press_up_arrow_button", "press_down_arrow_button"], "variable": "variable_auto_menu_food_weight"},
        {"step": 5, "actions": ["press_start_plus30sec_confirm_button"]}
    ],
    "lock_function": [
        {"step": 1, "actions": ["press_and_hold_stop_button"], "variable": "variable_lock"}
    ],
    # program about display
    #"inquiring_function": [
    #    {"step": 1, "actions": ["press_microwave_button"]},
    #    {"step": 2, "actions": ["press_clock_button"]}
    #]
}

class ApplianceMicrowave(Appliance):

    def __init__(self):
        
        super().__init__()
        self.reset()

    def reset(self):
        self.mode = MicrowaveMode(mode_list=mode_list, current_value=("empty", 1))

        self.variable_clock_setting_hour = ContinuousVariable(value_range=[0, 23], current_value=0, step_value=1)
        self.variable_clock_setting_minute = ContinuousVariable(value_range=[0, 59], current_value=0, step_value=1)
        self.variable_microwave_cooking_power = DiscreteVariable(value_range=["P100", "P80", "P50", "P30", "P10"], current_value="P100")
        self.variable_microwave_cooking_time = PiecewiseTimeVariable(value_range=["0:00", "95:00"], current_value='0:00', step_value=5)
        self.variable_defrost_time = PiecewiseTimeVariable(value_range=["0:00", "95:00"], current_value='0:00', step_value=5)
        self.variable_defrost_weight = ContinuousVariable(value_range=[100, 2000], current_value=100, step_value=100)
        self.variable_speedy_cooking_1 = TimeVariable(value_range=["0:30", "95:00"], current_value='0:00', step_value=30)
        self.variable_speedy_cooking_2 = PiecewiseTimeVariable(value_range=["0:00", "95:00"], current_value='0:00', step_value=5)
        self.variable_kitchen_timer = PiecewiseTimeVariable(value_range=["0:00", "95:00"], current_value='0:00', step_value=5)
        self.variable_auto_menu = DiscreteVariable(value_range=["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8"], current_value="A-1")
        self.variable_auto_menu_food_weight = VariableAutoMenuFoodWeight()
        self.variable_lock = DiscreteVariable(value_range=["lock", "unlock"], current_value="unlock")
        self.variables = [self.mode, self.variable_clock_setting_hour, self.variable_clock_setting_minute, self.variable_microwave_cooking_power, self.variable_microwave_cooking_time, self.variable_defrost_weight, self.variable_kitchen_timer, self.variable_auto_menu, self.variable_auto_menu_food_weight, self.variable_lock, self.variable_speedy_cooking_1, self.variable_speedy_cooking_2, self.variable_defrost_time, self.mode.two_stages]
    
    def __str__(self):
        variable_names = [
            "mode",
            "variable_clock_setting_hour",
            "variable_clock_setting_minute",
            "variable_microwave_cooking_power",
            "variable_microwave_cooking_time",
            "variable_defrost_weight",
            "variable_kitchen_timer",
            "variable_auto_menu",
            "variable_auto_menu_food_weight",
            "variable_lock",
            "variable_speedy_cooking_1",
            "variable_speedy_cooking_2",
            "variable_defrost_time",
            "mode_two_stages"
        ]

        variable_strs = [f"{name}: {var.get_current_value()}" for name, var in zip(variable_names, self.variables)]
        result = "\n".join(variable_strs)
        return result
    
    def lock_check(func):
        def wrapper(self, *args, **kwargs):
            if self.variable_lock.current_value == "lock":
                print("Microwave is locked. No action can be performed.")
                return
            return func(self, *args, **kwargs)
        return wrapper

    @lock_check
    def press_clock_button(self):
        self.mode.switch_mode("press_clock_button")

    @lock_check
    def press_up_arrow_button(self):
        self.mode.switch_mode("press_up_arrow_button")
        variable = self.get_current_variable("press_up_arrow_button")
        self.assign_variable_to_next(variable)

    @lock_check
    def press_down_arrow_button(self):
        self.mode.switch_mode("press_down_arrow_button")
        variable = self.get_current_variable("press_down_arrow_button")
        self.assign_variable_to_prev(variable)

    @lock_check
    def press_start_plus30sec_confirm_button(self):
        self.mode.switch_mode("press_start_plus30sec_confirm_button")
        if self.mode.get_current_value() == ("auto_menu", 3):
            variable = self.variable_auto_menu_food_weight
            variable.update_value_range(self.variable_auto_menu.get_current_value())
        else:
            variable = self.get_current_variable("press_start_plus30sec_confirm_button")
            self.assign_variable_to_next(variable)

    @lock_check
    def press_weight_defrost_button(self):
        self.mode.switch_mode("press_weight_defrost_button")

    @lock_check
    def press_time_defrost_button(self):
        self.mode.switch_mode("press_time_defrost_button")

    @lock_check
    def press_kitchen_timer_button(self):
        self.mode.switch_mode("press_kitchen_timer_button")

    def press_and_hold_stop_button(self):
        self.mode.switch_mode("press_and_hold_stop_button")
        variable = self.get_current_variable("press_and_hold_stop_button")
        self.assign_variable_to_next(variable)

    @lock_check
    def press_microwave_button(self):
        self.mode.switch_mode("press_microwave_button")

    @lock_check
    def press_stop_button(self):
        self.reset()
    
   


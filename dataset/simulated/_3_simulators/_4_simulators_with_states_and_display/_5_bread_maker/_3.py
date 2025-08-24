# 5 variables

# Variable for cycle selection
variable_cycle = DiscreteVariable(
    value_range=["1 Basic", "2 French", "3 Gluten-Free", "4 Quick", "5 Sweet", "6 1.5lb. Express", "7 2.0lb Express", "8 Dough", "9 Jam", "10 Cake", "11 Whole Grain", "12 Bake"],
    current_value="1 Basic"
)

# Variable for crust color selection
variable_crust_color = DiscreteVariable(
    value_range=["Light", "Medium", "Dark"],
    current_value="Medium"
)

# Variable for loaf size selection
variable_loaf_size = DiscreteVariable(
    value_range=["1.5-lb", "2-lb"],
    current_value="2-lb"
)

# Variable for delay timer
variable_delay_timer = ContinuousVariable(
    value_ranges_steps=[(0, 13, 1)],  # Delay timer can be set from 0 to 13 hours in 1-hour increments
    current_value=0)

# Variable for start/stop operation
variable_start_running = DiscreteVariable(
    value_range=["off", "on"],
    current_value="off"
)

feature_list = {}

feature_list["select_cycle"] = [
    {"step": 1, "actions": ["press_cycle_button"], "variable": "variable_cycle", "step_size": 12}
]

feature_list["select_crust_color"] = [
    {"step": 1, "actions": ["press_crust_button"], "variable": "variable_crust_color", "step_size": 3}
]

feature_list["select_loaf_size"] = [
    {"step": 1, "actions": ["press_loaf_size_button"], "variable": "variable_loaf_size", "step_size": 2}
]

feature_list["set_delay_timer"] = [
    {"step": 1, "actions": ["press_delay_timer_plus_button", "press_delay_timer_minus_button"], "variable": "variable_delay_timer", "step_size": 14}
]

feature_list["start_stop_operation"] = [
    {"step": 1, "actions": ["press_start_stop_button", "press_and_hold_start_stop_button"], "variable": "variable_start_running", "step_size": 2}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_cycle = variable_cycle
        self.variable_crust_color = variable_crust_color
        self.variable_loaf_size = variable_loaf_size
        self.variable_delay_timer = variable_delay_timer
        self.variable_start_running = variable_start_running

    def press_cycle_button(self):
        # Update feature progress and set the cycle to the next value
        self.feature.update_progress("press_cycle_button")
        self.execute_action_and_set_next("press_cycle_button")

    def press_crust_button(self):
        # Update feature progress and set the crust color to the next value
        self.feature.update_progress("press_crust_button")
        self.execute_action_and_set_next("press_crust_button")

    def press_loaf_size_button(self):
        # Update feature progress and set the loaf size to the next value
        self.feature.update_progress("press_loaf_size_button")
        self.execute_action_and_set_next("press_loaf_size_button")

    def press_delay_timer_plus_button(self):
        # Update feature progress and increase the delay timer
        self.feature.update_progress("press_delay_timer_plus_button")
        self.execute_action_and_set_next("press_delay_timer_plus_button")

    def press_delay_timer_minus_button(self):
        # Update feature progress and decrease the delay timer
        self.feature.update_progress("press_delay_timer_minus_button")
        self.execute_action_and_set_prev("press_delay_timer_minus_button")

    def press_start_stop_button(self):
        # Update feature progress and toggle the start/stop operation
        self.feature.update_progress("press_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop_operation":
            self.variable_start_running.set_current_value("on" if self.variable_start_running.get_current_value() == "off" else "off")

    def press_and_hold_start_stop_button(self, duration=2):
        # Update feature progress and stop the operation if held for 2 seconds
        self.feature.update_progress("press_and_hold_start_stop_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_stop_operation" and duration >= 2:
            self.variable_start_running.set_current_value("off")

    def run_action(self, action_name, execution_times=1, **kwargs):
        # Execute the action and update the display
        action = getattr(self, action_name, None)
        if callable(action):
            sig = inspect.signature(action)
            valid_kwargs = {k: v for k, v in kwargs.items() if k in sig.parameters}
            for _ in range(execution_times):
                action(**valid_kwargs)
        self.update_display()
        return self.display
# Comments: In the original code, the feature to activate the gluten-free mode ("activate_gluten_free_mode") was missing the ability to set a time delay. According to the user manual, the delayed start timer ensures the machine begins operation after a specified time. Thus, we need to modify the feature to include this functionality.

# Modifying the feature_list to add timer functionality for activating the gluten-free mode.
updated_feature_list = feature_list
updated_feature_list["activate_gluten_free_mode"] = [
    {"step": 1, "actions": ["press_gluten_free_button"], "variable": "variable_gluten_free_mode"},
    {"step": 2, "actions": ["press_timer_up_button", "press_timer_down_button"], "variable": "variable_timer"},
]

class ExtendedSimulator(Simulator):
    def reset(self):
        super().reset()
        self.feature = Feature(feature_list=updated_feature_list, current_value=("empty", 1))

    def press_gluten_free_button(self):
        # Update feature progress and activate gluten-free mode
        self.feature.update_progress("press_gluten_free_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "activate_gluten_free_mode":
            self.variable_gluten_free_mode.set_current_value("on")

    def press_timer_up_button(self):
        # Update feature progress and increase delay timer
        self.feature.update_progress("press_timer_up_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "activate_gluten_free_mode":
            self.execute_action_and_set_next("press_timer_up_button")

    def press_timer_down_button(self):
        # Update feature progress and decrease delay timer
        self.feature.update_progress("press_timer_down_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "activate_gluten_free_mode":
            self.execute_action_and_set_prev("press_timer_down_button")
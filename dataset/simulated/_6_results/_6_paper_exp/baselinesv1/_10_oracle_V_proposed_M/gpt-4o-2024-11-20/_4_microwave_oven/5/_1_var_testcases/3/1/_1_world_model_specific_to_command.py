# The original code for the Simulator is missing a key feature on how to explicitly set the timer for durations other than the pre-defined discrete options. 
# The task specifies adjusting the timer to "60 minutes", but the current implementation does not provide a mechanism to achieve this. 
# The user manual also mentions setting the desired cooking duration but doesn't limit it to pre-defined values as per the code.

# Correcting this issue and providing appropriate features and functionality to match the user manual and the requested command.

# Updated feature list to include a more flexible timer setting with continuous value adjustments.
updated_feature_list = feature_list
updated_feature_list["adjust_timer_dial"] = [
    {"step": 1, "actions": ["turn_timer_dial_clockwise", "turn_timer_dial_anticlockwise"], "variable": "variable_timer_dial"}
]

# Extending the simulator to correct and fully implement features according to the user manual and command requirements.
class ExtendedSimulator(Simulator): 
    def reset(self):
        super().reset()
        self.feature = Feature(feature_list=updated_feature_list, current_value=("empty", 1))
        # Updating the timer dial as a ContinuousVariable to match the possibility of setting "60 minutes".
        self.variable_timer_dial = ContinuousVariable(
            value_ranges_steps=[(0, 60, 1)],  # Timer values from 0 to 60 minutes in 1-minute steps
            current_value=0
        )

    def turn_timer_dial_clockwise(self):
        # Update feature progress and adjust the timer dial variable.
        self.feature.update_progress("turn_timer_dial_clockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            self.variable_timer_dial.next()

    def turn_timer_dial_anticlockwise(self):
        # Update feature progress and adjust the timer dial variable.
        self.feature.update_progress("turn_timer_dial_anticlockwise")
        current_feature = self.feature.current_value[0]
        if current_feature == "adjust_timer_dial":
            self.variable_timer_dial.prev()
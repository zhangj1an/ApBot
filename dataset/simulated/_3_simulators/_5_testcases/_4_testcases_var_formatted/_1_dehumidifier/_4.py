[
    {
        "command": "Turn on the dehumidifier and set the fan speed to 'low' for a quiet operation while you're working.",
        "id": 1,
        "important_target_states": {
            "variable_fan_speed": "low",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 5,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Power on the dehumidifier and set the timer to '2H' to run it for two hours while you're out.",
        "id": 2,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "2H"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "2H"
        }
    },
    {
        "command": "Start the dehumidifier and select the 'medium' fan speed to balance noise and dehumidification.",
        "id": 3,
        "important_target_states": {
            "variable_fan_speed": "medium",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "medium",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn on the dehumidifier and engage the 'night_mode' to ensure low noise levels while you sleep.",
        "id": 4,
        "important_target_states": {
            "variable_microbe_shield_night_mode": "night_mode",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_microbe_shield_night_mode": "night_mode",
            "variable_power_on_off": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Power up the dehumidifier and ensure the timer is set to '4H' for continuous operation during a dinner party.",
        "id": 5,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "4H"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "4H"
        }
    },
    {
        "command": "Start the dehumidifier and switch to 'high' fan speed to quickly reduce humidity after a rainy day.",
        "id": 6,
        "important_target_states": {
            "variable_fan_speed": "high",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_fan_speed": "high",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn on the dehumidifier and select 'microbe_shield' to eliminate mold and bacteria in the room.",
        "id": 7,
        "important_target_states": {
            "variable_microbe_shield_night_mode": "microbe_shield",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_microbe_shield_night_mode": "microbe_shield",
            "variable_power_on_off": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Power on the dehumidifier and set to 'turbo' fan speed for fast moisture removal in the basement.",
        "id": 8,
        "important_target_states": {
            "variable_fan_speed": "turbo",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_fan_speed": "turbo",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Engage the dehumidifier and set the timer to '8H' to operate overnight.",
        "id": 9,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "8H"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "8H"
        }
    },
    {
        "command": "Turn the dehumidifier on and change the fan speed to 'medium' for watching TV without disturbance.",
        "id": 10,
        "important_target_states": {
            "variable_fan_speed": "medium",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "medium",
            "variable_microbe_shield_night_mode": "off",
            "variable_power_on_off": "on",
            "variable_timer": "0"
        }
    }
]

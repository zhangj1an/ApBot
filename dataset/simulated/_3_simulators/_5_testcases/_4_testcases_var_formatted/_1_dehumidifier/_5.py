[
    {
        "command": "Power on the dehumidifier and set the fan speed to 'mid.'",
        "id": 1,
        "important_target_states": {
            "variable_fan_speed": "mid",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "mid",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn on the dehumidifier and toggle the ion generator to 'on.'",
        "id": 2,
        "important_target_states": {
            "variable_ion_generator": "on",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_ion_generator": "on",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Switch on the dehumidifier and set the timer for 2 hours.",
        "id": 3,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "2H"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "2H"
        }
    },
    {
        "command": "Power on the dehumidifier and activate the sleep mode.",
        "id": 4,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_sleep_mode": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "on",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn the dehumidifier on and adjust the fan speed to 'high.'",
        "id": 5,
        "important_target_states": {
            "variable_fan_speed": "high",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_fan_speed": "high",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn the dehumidifier on and adjust the fan speed to 'mid.'",
        "id": 6,
        "important_target_states": {
            "variable_fan_speed": "mid",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "mid",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Power on the dehumidifier and set the fan speed to 'low.'",
        "id": 7,
        "important_target_states": {
            "variable_fan_speed": "low",
            "variable_power_on_off": "on"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Turn on the dehumidifier and set a 4-hour shut-off timer.",
        "id": 8,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "4H"
        },
        "optimal_step_size": 4,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "4H"
        }
    },
    {
        "command": "Power on the dehumidifier and ensure the sleep mode is 'off.'",
        "id": 9,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off"
        },
        "optimal_step_size": 3,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "0"
        }
    },
    {
        "command": "Power on the dehumidifier and set the timer for 1 hour.",
        "id": 10,
        "important_target_states": {
            "variable_power_on_off": "on",
            "variable_timer": "1H"
        },
        "optimal_step_size": 2,
        "target_state": {
            "variable_fan_speed": "low",
            "variable_ion_generator": "off",
            "variable_power_on_off": "on",
            "variable_sleep_mode": "off",
            "variable_timer": "1H"
        }
    }
]

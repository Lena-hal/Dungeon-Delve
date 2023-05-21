#here are all the error messages that can happen

REPORT_LINK = " please report this bug at https://github.com/Lena-hal/Dungeon-Delve"

def animation_max_frame_exceded(victim):
    print("ERROR - animation frame is shorter than max value, this happened to:" + str(victim) + REPORT_LINK)
    
def animation_short_frame(victim):
    print("ERROR - animation frame modifier was set for too short time period (0 or less frames), this happened to:" + str(victim) + REPORT_LINK)

def animation_too_small_max_frame(victim):
    print("ERROR - max frame of the animation was set to 0, you can't have animation with 0 frames, this happened to: " + str(victim) + REPORT_LINK)

def texture_manager_invalid_path(path):
    print(f"ERROR - texture manager could not find {path}, maybe it wasn't indexed? {REPORT_LINK}")

def invalid_texture_modificator(modifier):
    print(f"ERROR - texture modifiing process could not find {modifier}, this modifier is not suported {REPORT_LINK}")

def polymorphism_rule_violation(victim):
    print("ERROR - polymorphism rule was violated, this happened to:" + str(victim) + REPORT_LINK)

def polymorphism_rule_violation_made_an_issue(victim):
    print("ERROR - polymorphism rule was violated and caused an issue, this happened to:" + str(victim) + REPORT_LINK)
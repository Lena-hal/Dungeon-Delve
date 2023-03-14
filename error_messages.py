#here are all the error messages that can happen

REPORT_LINK = " please report this bug at https://github.com/Lena-hal/hra"

def animation_max_frame_exceded(victim):
    print("ERROR - animation frame is shorter than max value, this happened with:" + str(victim) + REPORT_LINK)
    
def animation_short_frame(victim):
    print("ERROR - animation frame modifier was set for too short time period (0 or less frames), this happened with:" + str(victim) + REPORT_LINK)
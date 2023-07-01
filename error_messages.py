# here are all the error messages that can happen

REPORT_LINK = " please report this bug at https://github.com/Lena-hal/Dungeon-Delve"


def animation_max_frame_exceded(victim):
    """
    used to signalise that the max frame of an animation is exceded
    :param victim: the object that caused the error
    """
    print("ERROR - animation frame is shorter than max value, this happened to:" + str(victim) + REPORT_LINK)


def animation_short_frame(victim):
    """
    used to signalise that the animation frame modifier was set for too short time period
    :param victim: the object that caused the error
    """
    print("ERROR - animation frame modifier was set for too short time period (0 or less frames), this happened to:" + str(victim) + REPORT_LINK)


def animation_too_small_max_frame(victim):
    """
    used to signalise that the max frame of an animation is 0 or less
    :param victim: the object that caused the error
    """
    print("ERROR - max frame of the animation was set to 0, you can't have animation with 0 frames, this happened to: " + str(victim) + REPORT_LINK)


def texture_manager_invalid_path(path):
    """
    used to signalise that the texture manager could not find the texture
    :param path: the path to the texture
    """
    print(f"ERROR - texture manager could not find {path}, maybe it wasn't indexed? {REPORT_LINK}")


def invalid_texture_modificator(modifier):
    """
    used to signalise that the texture modifier was not suported
    :param modifier: the modifier that was not suported
    """
    print(f"ERROR - texture modifiing process could not find {modifier}, this modifier is not suported {REPORT_LINK}")


def polymorphism_rule_violation(victim):
    """
    used to signalise that the polymorphism rule was violated
    :param victim: the object that caused the error
    """
    print("ERROR - polymorphism rule was violated, this happened to:" + str(victim) + REPORT_LINK)


def polymorphism_rule_violation_made_an_issue(victim):
    """
    used to signalise that the polymorphism rule was violated and caused an issue
    :param victim: the object that caused the error
    """
    print("ERROR - polymorphism rule was violated and caused an issue, this happened to:" + str(victim) + REPORT_LINK)

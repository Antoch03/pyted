

class VersioneerConfiguration:
    pass


def get_configuration():
    """
    """
    configuration = VersioneerConfiguration()
    configuration.VCS = "git"
    configuration.verbose = False
    return configuration


def get_versions():
    """
    """
    version_dictionary  = dict()
    configuration       = get_configuration()
    verbose             = configuration.verbose
    version_dictionary["version"] = ""

    return version_dictionary




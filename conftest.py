from hypothesis import settings, HealthCheck, Verbosity

settings.register_profile("settings_profile",
                          max_examples=10000,
                          #verbosity=Verbosity.verbose,
                          suppress_health_check=(HealthCheck.filter_too_much,))

settings.load_profile("settings_profile")

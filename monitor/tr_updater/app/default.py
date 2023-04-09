

class AbstractUpdater:

    user_agent: str = 'TruckersMP Launcher/1.x'

    headers: dict = {
        'User-Agent': user_agent,
    }

    cache: dict = {
        'ats': {},
        'ets2': {},
        'system': {},
    }

    to_update = {}

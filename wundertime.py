from __future__ import print_function
from datetime import datetime
import pytz, requests

BASE_URL = 'http://autocomplete.wunderground.com/aq?query='

def find_time_at_location(location):
    query = requests.get(BASE_URL+location).json()
    results = []
    for location in query['RESULTS']:
        try:
            local_tz = pytz.timezone(location['tz'])
        except pytz.exceptions.UnknownTimeZoneError:
            # Couldn't find the location
            next
        else:
            results.append([
                location['name'],
                datetime.now(local_tz).strftime('%c'),
                location['tzs']
            ])
        return results

try:
    import sopel.module
except ImportError:
    # Probably running from commandline
    pass
else:
    @sopel.module.commands('time')
    @sopel.module.example('.time london')
    def f_time(bot, trigger):
        """Look up the time name with wunderground"""
        if trigger.group(2):
            query = trigger.group(2).strip().lower()
            results = find_time_at_location(query)
            if results:
                for result in results:
                    bot.say('Time for {} is {} ({})'.format(*result))
            else:
                bot.say('Couldn\'t look up time for "{}"'.format(query))
        return sopel.module.NOLIMIT

if __name__ == '__main__':
    import sys
    query = 'london'
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    print('Looking up "{}"'.format(query))
    results = find_time_at_location(query)
    if results:
        for result in results:
            print("Time for {} is {} ({})".format(*result))
    else:
        print('Couldn\'t look up time for "{}"'.format(query))

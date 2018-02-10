# sopel-wundertime

WunderMap based time lookup script for Sopel IRC bot.

## Installation

Tested on Ubuntu 1604LTS. Requires pytz, requests.
```
sudo pip3 install requests
```

In your ~/.sopel/default.cfg or similar disable the clock module:

```
[core]
exclude = clock
...
```

## Testing

```
$ python3 sopel-wundertime/wundertime.py alice springs
Looking up "alice springs"
Time for Alice Springs, Australia is Sat Feb 10 18:37:32 2018 (ACST)
$
```


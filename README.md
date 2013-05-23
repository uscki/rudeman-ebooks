rudeman-ebooks
==============

Een markov chain twitter bot als grens van het universum

Live op [rudeman_ebooks](https://twitter.com/rudeman_ebooks)

Benodigdheden
-------------

- Python (http://python.org/)
- python-twitter (https://github.com/bear/python-twitter)
- Twitter API toegang (https://dev.twitter.com/apps) en 4 OAuth codes:


		CONSUMER_KEY    = 'je-consumer-key'
		CONSUMER_SECRET = 'je-consumer-secret'
		ACCESS_KEY      = 'een-access-key'
		ACCESS_SECRET   = 'een-access-secret'


Waarom?
-------

Dit is een heel simpel taalmodel waar iets minder onzinnige onzin uitkomt dat een volstrekt willekeurige. Maar dat ligt natuurlijk aan je corpus. Met python kan je makkelijk leuke kunstjes doen. Geïnspireerd op horse_ebooks en jwz_ebooks.

Hoe?
----

python markov.py [debug] <br />
Debugstatement zorgt dat er niet getwitterd wordt en print elke 5 seconden een nieuwe uitspraak in de terminal.

We bouwen een dictionary op die elk woord mapt naar een lijst van woorden die er (direct) op kunnen volgen in het corpus
Hierbij worden dubbelen gewoon toegevoegd. Als je dan een wilekeurig woord uit dat rijtje pakt om er achter te plakken, krijg je een mooie waarschijnlijkheidsverdeling.
Dat betekent: `p(a na b)` is `|a na b| / |b|`.<br />
(...)<br />
Zie http://en.wikipedia.org/wiki/Parody_generator <br />
Fijne feestdagen en het zonnestelsel.

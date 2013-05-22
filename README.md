rudeman-ebooks
==============

Een hidden markov model twitter bot als grens van het universum

Benodigdheden
-------------

- Python (http://python.org/)
- python-twitter (https://github.com/bear/python-twitter)
- Twitter API toegang (https://dev.twitter.com/apps) en 4 OAuth codes:

> CONSUMER_KEY    = 'je-consumer-key'
> CONSUMER_SECRET = 'je-consumer-secret'
> ACCESS_KEY      = 'een-access-key'
> ACCESS_SECRET   = 'een-access-secret'


Waarom?
-------

Dit is een heel simpel taalmodel waar iets minder onzinnige onzin uitkomt dat een volstrekt willekeurige. Maar dat ligt natuurlijk aan je corpus. Met python kan je makkelijk leuke kunstjes doen.

Hoe?
----

Elk woord krijgt een lijstje met welke woorden er na voorkomen in het corpus. Hierbij worden dubbelen gewoon toegevoegd. Als je dan een wilekeurig woord uit dat rijtje pakt om er achter te plakken, krijg je een mooie waarschijnlijkheidsverdeling.
Dat betekent dat de kans op een woord `a` na woord `b` is 0 als `a` nooit na `b` voorkomt in het corpus, en anders `het aantal keren dat a na b voorkomt / het aantal woorden dat na b komt`.
(...)
Grens van het universum.
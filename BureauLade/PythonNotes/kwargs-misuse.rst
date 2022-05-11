.. Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017
.. -*- coding: utf-8 -*-

=======================
``kwargs`` als argument
=======================

.. container:: lead

   ``kwargs``: use or misuse?

.. post:: 2017/03/29
   :tags: Python, feedback
   :category: Tips, rough
   :location: EHV

   Elke python-programmeur kent het :dfn:`kwargs` concept, waarmee een variabel aantal **named**- (of
   ‘keyword’) argumenten *ontvangen* kan worden in een functie. Soms wordt dit concept
   echter *onhandig* gebruikt.

In een *ontvangende* functie gebruikt men vaak de parameter-naam ``kwargs`` (dus als: ‘formal
parameter’); al is deze naam niet verplicht, het gaat om de ‘``**``’-syntax. Soms wordt die naam ook
gebruikt als argument; dus bij het aanroepen van die functie. Dat is natuurlijk niet nodig; het
gaat juist om alle *andere* (named) argumenten; die verzameld worden in ``kwargs``

.. tip:: Wat is ook al weer een *parameter* en wat een *argument*?

   Taal-specialisten maken een verschil tussen *parameters* en *argumenten*, veel programmeurs
   in de praktijk. Dat kan verwarend zijn.
   Immers: ``kwargs`` is een afkorting van **k**\ey\ **w**\ord-**arg**\ument\ **s**. En een veel
   gebruike naam voor de **parameter** om die variable-aantal named-argumenten te “verzamelen”.

   .. seealso::

      De `Python-FAQ
      <https://docs.python.org/faq/programming.html#what-is-the-difference-between-arguments-and-parameters>`__
      voor het verschil tussen parameters en argumenten.

Natuurlijk is het soms handig meerdere *”waarden”* in één data-object te verzamelen voordat die als
argument doorgegeven wordt. Zeker in web-frameworks (zoals `Flask <http://flask.pocoo.org>`__ en
`Django <https://www.DjangoProject.com>`__) gebeurd dat vaak. Een typisch functie berekend dan allerlei
gegevens, die daarna aan een template-engines (zie oa. `Jinja2 <http://jinja.pocoo.org>`__)
doorgegeven worden. Omdat elke template anders is, zijn de parameters (zowel aantal, naam als
structuur) niet vooraf bekend. Toch is het **niet** *nodig* om het ``kwargs``-concept in dit soort
gevallen te gebruiken! Met een gewone ``dict`` kan het ook.

Toch is het ``kwargs``-concept vaak te prefereren; het geeft de gebruikers vrijheid. De aanroepende
functie kan een dict gebruiken, om die waarden te verzamelen. Of named-parameters gebruiken; of een
mix...

Die vrijheid wordt soms misbruikt, of verkeerd begrepen. Dan start elke functie bijvoorbeeld met
het *declaren* van die **kwargs** variabele, als een lege dict. Daarna die gevuld, soms al op de
volgende regels, en met constanten of eenvoudige expressies. Een voorbeeld:

.. code-block:: python

   def demo_waarom():
       """Waarom hier `kwargs` gebruiken?"""
       kwargs = {}
       kwargs['start'] = datetime.datetime.now()
       kwargs['end']   = kwargs['start'] + datetime.timedelta(days=7)
       kwargs['DEMO']  = "Kan beter"
       ...
       return render_template('aWeek.html', **kwargs)

Waarom? En hoe beter?
=====================

Mijn vraag bij bovenstaande code is vaak waarom? Waarom heet die variabele **kwargs**? Maar ook:
waarom deze constructie. Immers de code kan eenvoudig korter en leesbaarder gemaakt worden. Soms
kan de helft gewoon weg!

Als zal dat niet altijd kunnen, daarom laat ik hieronder in een paar stappen zien hoe het beter kan.

Andere naam
-----------

De eerste stap is een de naam **kwargs** vervangen door iets beters. Een beschrijvende naam, die
aangeeft om welke *waarden* het gaat is vaak te prefereren. Al is dat soms lastig, zeker in een
demo of een korte functie. In dat laatste geval kies ik zelf vaak voor ``d`` als afkorting
van *dict*. In dit geval lijkt het om week-info te gaan; en gebruik in de naam ‘week’.

.. code-block:: python

   def demo_andere_naam():
       """Bijna elke variabele-naam is beter dan `kwargs`"""
       week = {}
       week['start'] = datetime.datetime.now()
       week['end']   = week['start'] + datetime.timedelta(days=7)
       week['DEMO']  = "Al iets beter"
       ...
       return render_template('aWeek.html', **week)

Vul de dict direct
------------------

In bovenstaande code zijn 4 regels nodig om een dictionary te vullen, waarbij de naam van de dict
telkens herhaald wordt. Dat lastig te onderhouden en niet nodig. De meeste waarde kunnen immers
direct in die dictionary gezet worden.

.. code-block:: python

   def demo_vul_direct():
       """Een lege dict is niet nodig; waarom niet direct de waarden invullen?"""
       now = datetime.datetime.now()
       week = {'start': now,
               'end'  :  now + datetime.timedelta(days=7),
               'DEMO' : "Beter te onderhouden"}
       ...
       return render_template('aWeek.html', **week)

Zonder kwargs!
--------------

In een paar stapje is de code korter, leesbaarder en onderhoud-vriendelijk(er) geworden. Maar het
``kwargs``-concept wordt nog steeds (mis)bruikt. Dat is echter niet nodig. Het enige dat nodig is,
zijn de ``start`` en ``end`` datums van de week en een ``DEMO`` string. Door die als named
parameter door te geven wordt de code nog korter en leesbaarder. En is de kwargs (cq week)
variabele niet nodig.

.. code-block:: python

   def demo_zonder_kwargs():
       """De kwargs/week dict is helemaal niet nodig!"""
       now = datetime.datetime.now()
       return render_template('aWeek.html', start=now, end=now+datetime.timedelta(days=7), DEMO="kwargs is niet nodig")

Niet alleen is deze code meer dan 60% korter, ook is het veel duidelijker welke waarden doorgegeven
worden. Het is heel duidelijk geworden dat de parameters ``start``, ``end`` en ``DEMO`` gebruikt
worden om die html-pagina te maken.

Conclusie
=========

We hebben gezien dat het **kwargs-concept** heel handig is -- veel frameworks gebruiken het dan ook
en gebruiken ``kwargs`` als formale parameter naam. We hebben ook gezien dat die naam als
*variabele-naam* niet heel veel duidelijkheid geeft. Bijna altijd is er een betere naam te
bedenken.

Belangrijker is hoe we zo’n functie aanroepen en --waar nodig-- de dict vullen. Constante waarden,
of waarden die met een eenvoudig expressies te bereken zijn, kunnen met direct gebruikt
worden. Ofwel als named-parameter, of (‘literal’) bij het maken van de dict. Soms is meer code
nodig, vaak is een gewone *lokale* variabele dan het handigste. Die als named parameter doorgegeven
kan worden.

Door een combinatie van deze standaad *denkstappen* en een streven om de code leesbaar te maken
wordt de code vaak veel onderhoudbaarder en meestal korter.




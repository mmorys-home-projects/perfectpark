============
Perfect Park
============


.. image:: https://img.shields.io/pypi/v/perfectpark.svg
        :target: https://pypi.python.org/pypi/perfectpark

.. image:: https://img.shields.io/travis/mmorys/perfectpark.svg
        :target: https://travis-ci.com/mmorys/perfectpark

.. image:: https://readthedocs.org/projects/perfectpark/badge/?version=latest
        :target: https://perfectpark.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A Raspberry Pi hosted distance sensor to help you park perfectly in your garage, every time.

A smart sensor for you garage which will indicate, via colored LEDs, how far your car needs to pull in to the garage to close the door safely. The distance sensing is accomplished with an ultrasonic sensor, and control is handled with a Raspberry Pi. The ultrasonic sensor is only activated when the garage door is opened, which is determined via an MQTT message. The source of the MQTT message is a Home Assistant instance with a garage door sensor, but that is outside of this project.


* Free software: MIT license
* Documentation: https://perfectpark.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

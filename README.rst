Pelican Global RST Include
==========================

``Global RST Include`` is a plugin for `Pelican`_ allowing for the convenient and straight-forward inclusion of global `RST`_ files into every RST article.
This can make sense for central definitions of, for example, custom code roles, the default code role and abbreviations.
Refer to `my blog article <https://mhoff.net/article/2016/06/30/global-includes-for-rst/>`_ for further motivation and background.

*This repository is no longer maintained. Forks of this repository are probably improved and more up-to-date. https://github.com/ryancdotorg/pelican-global-rst-include appears to be compatible with newer versions of Pelican.* 

Usage
-----

Clone this repository to a folder of your choice (best inside the pelican project folder).
Then, add the relative path to this plugin to the list of plugins (``PLUGINS`` in, e.g. ``pelicanconf.py``) [#]_.

Now you can define which RST files should be included.
For this, simply add the relative paths to the list ``RST_GLOBAL_INCLUDES``.
The contents of every file in there, will then be virtually [#]_ included at the beginning [#]_ of each of your RST articles.


Your ``pelicanconf.py`` and directory structure could now look like this:

.. code-block:: python

    # ...

    PLUGIN_PATHS = [
        # other paths
        "plugins"
    ]

    PLUGINS = [
        # other plugins
        "pelican-global-rst-include"
    ]

    RST_GLOBAL_INCLUDES = [ "include/globals.rst" ]

    # ...

.. code-block:: text

    pelican project
    |-- include
    |   |-- globals.rst
    |-- content
    |   |-- some_article.rst
    |-- plugins
    |   |-- pelican-global-rst-include
    |....


Now, rerunning ``pelican`` will yield the modifications the global RST-files introduce to your articles.

.. [#] You can also utilize ``PLUGIN_PATH`` to set the path to your folder of plugins and, with this, shorten your relative plugin paths.
.. [#] The article file is not modified. Its contents are read, prepended by the contents to include and then processed.
.. [#] Ordering is preserved. The content of the first include file in the list will be at the very beginning of the aggregated contents to be processed.

Settings
--------

``RST_GLOBAL_INCLUDES``
    list of RST-files (relative to pelican project root) to be injected into all RST-articles

Possible Issues & Future Work
-----------------------------

Unfortunately, `Docutils`_ is very hardcoded when it comes to reading and parsing source files.
It may be extensible when it comes to actually modifying the Docutils code, but as a user of the system things get ugly.

Out of this several (possible) issues arise:

* Updates to Docutils could break this plugin
* Subtle bugs could be contained.
* ``docutils.io.FileInput`` shows several signs of handling encoding different when using a python version above 3.0.
  It *could* be that the global include files should be handled the same way for the subsequent concatenation to be consistent.

License
-------

Published under the `MIT`_ license.

.. _Pelican: http://blog.getpelican.com/
.. _RST: http://docutils.sourceforge.net/rst.html
.. _Docutils: http://docutils.sourceforge.net/
.. _MIT: http://opensource.org/licenses/MIT

.. _installing:

Installing and getting started
------------------------------

To install the released version of terra, you can use ``pip`` (i.e. ``pip
install terra``). It's also possible to install the released version using
``conda`` (i.e. ``conda install terra``), although this may lag behind the
version availible from PyPI.

Alternatively, you can use ``pip`` to install the development version, with the
command ``pip install git+git://github.com/jhamman/terra.git#egg=terra``.
Another option would be to to clone the `github repository
<https://github.com/jhamman/terra>`_ and install with ``pip install .`` from
the source directory. terra itself is pure Python, so installation should be
reasonably straightforward.

When using the development version, you may want to refer to the `development
docs <?>`_. Note that these
are not built automatically and may at times fall out of sync with the actual
master branch on github.


Dependencies
~~~~~~~~~~~~

-  Python 2.7 or 3.3+

Mandatory dependencies
^^^^^^^^^^^^^^^^^^^^^^

-  `numpy <http://www.numpy.org/>`__

-  `scipy <http://www.scipy.org/>`__

-  `matplotlib <matplotlib.sourceforge.net>`__

-  `pandas <http://pandas.pydata.org/>`__

-  `xarray <http://xarray.pydata.org/>`__

-  `seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`__

-  `cartopy <http://scitools.org.uk/cartopy/docs/latest/index.html>`__


Recommended dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

-  `statsmodels <http://statsmodels.sourceforge.net/>`__

-  `geopandas <http://geopandas.org/index.html/>`__

The `pip` installation script will attempt to download the mandatory
dependencies if they do not exist at install-time.

I recommend using terra with the `Anaconda distribution
<https://store.continuum.io/cshop/anaconda/>`_, as this makes it easy to manage
the main dependencies, which otherwise can be difficult to install.

I attempt to keep terra importable and generally functional on the versions
available through the stable Debian channels.  There may be cases where some
more advanced features only work with newer versions of these dependencies,
although these should be relatively rare.

There are also some known bugs on older versions of matplotlib, so you should
in general try to use a modern version. For many use cases, though, older
matplotlibs will work fine.

terra is tested on the most recent versions offered through ``conda``.


Importing terra
~~~~~~~~~~~~~~~~~

terra will apply its default style parameters to the global matplotlib style
dictionary when you import it. This will change the look of all plots,
including those created by using matplotlib functions directly. To avoid this
behavior and use the default matplotlib aesthetics (along with any
customization in your ``matplotlibrc``), you can import the ``terra.apionly``
namespace.

terra has several other pre-packaged styles along with high-level :ref:`tools
<aesthetics_tutorial>` for managing them, so you should not limit yourself to the
default aesthetics.

By convention, ``terra`` is abbreviated to ``eos`` on import.


Testing
~~~~~~~

To test terra, run ``make test`` in the root directory of the source
distribution. This runs the unit test suite (which can also be exercised
separately by running ``py.test``). It also runs the code in the example
notebooks to smoke-test a broader and more realistic range of example usage.

The full set of tests requires an internet connection to download the example
datasets, but the unit tests should be able to run offline.


Bugs
~~~~

Please report any bugs you encounter through the github `issue tracker
<https://github.com/jhamman/terra/issues/new>`_. It will be most helpful to
include a reproducible example on one of the example datasets (accessed through
:func:`load_dataset`). It is difficult debug any issues without knowing the
versions of terra and matplotlib you are using, as well as what matplotlib
backend you are using to draw the plots, so please include those in your bug
report.

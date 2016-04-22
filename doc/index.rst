.. raw:: html

    <style type="text/css">
    .thumbnail {{
        position: relative;
        float: left;
        margin: 10px;
        width: 180px;
        height: 200px;
    }}

    .thumbnail img {{
        position: absolute;
        display: inline;
        left: 0;
        width: 170px;
        height: 170px;
    }}

    </style>

terra: geospatial data visualization
=======================================

.. raw:: html


    <div style="clear: both"></div>
    <div class="container-fluid hidden-xs hidden-sm">
      <div class="row">
        <a href="examples/anscombes_quartet.html">
          <div class="col-md-2 thumbnail">
            <img src="_static/anscombes_quartet_thumb.png">
          </div>
        </a>
        <a href="examples/many_pairwise_correlations.html">
          <div class="col-md-2 thumbnail">
            <img src="_static/many_pairwise_correlations_thumb.png">
          </div>
        </a>
        <a href="examples/many_facets.html">
          <div class="col-md-2 thumbnail">
            <img src="_static/many_facets_thumb.png">
          </div>
        </a>
        <a href="examples/scatterplot_matrix.html">
          <div class="col-md-2 thumbnail">
            <img src="_static/scatterplot_matrix_thumb.png">
          </div>
        </a>
        <a href="examples/hexbin_marginals.html">
          <div class="col-md-2 thumbnail">
            <img src="_static/hexbin_marginals_thumb.png">
          </div>
        </a>
        <a href="examples/scatterplot_categorical.html">
          <div class="col-md-2 thumbnail">
            <img src="_static/scatterplot_categorical_thumb.png">
          </div>
        </a>
      </div>
    </div>
    <br>

   <div class="container-fluid">
   <div class="row">
   <div class="col-md-6">
   <br>

terra is a Python library for geospatial data visualization based on matplotlib.
It provides a high-level interface for drawing attractive geospatial graphics.
terra is the geospatial extension of the popular
`seaborn library <http://stanford.edu/~mwaskom/software/seaborn/>`_.

For a brief introduction to the ideas behind the package, you can read the
:ref:`introductory notes <introduction>`. More practical information is on the
:ref:`installation page <installing>`. You may also want to browse the
:ref:`example gallery <example_gallery>` to get a sense for what you can do with
terra and then check out the :ref:`tutorial <tutorial>` and
:ref:`API reference <api_ref>` to find out how.

To see the code or report a bug, please visit the `github repository
<https://github.com/jhamman/terra>`_.


.. raw:: html

   </div>
   <div class="col-md-3">
   <h2>Documentation</h2>

.. toctree::
   :maxdepth: 1

   introduction
   whatsnew
   installing
   examples/index
   api
   tutorial

.. raw:: html

   </div>
   <div class="col-md-3">
   <h2>Features</h2>

* Style functions: :ref:`API <style_api>` | :ref:`Tutorial <aesthetics_tutorial>`
* Color palettes: :ref:`API <colormaps_api>` | :ref:`Tutorial <colormaps_tutorial>`

.. raw:: html

   </div>
   </div>
   </div>

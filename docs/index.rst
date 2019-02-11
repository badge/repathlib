.. repathlib documentation master file

Welcome to repathlib's documentation!
=====================================

repathlib combines the simplicity of pathlib with the power of regular
expressions, making it easier to find files and directories.

repathlib provides a :class:`~repathlib.repathlib.Path` class which
subclasses :py:class:`pathlib.Path`, and adds the following methods to
it:

   - :meth:`~repathlib.repathlib.PosixPath.search`
   - :meth:`~repathlib.repathlib.PosixPath.match_`
   - :meth:`~repathlib.repathlib.PosixPath.fullmatch`
   - :meth:`~repathlib.repathlib.PosixPath.findall`
   - :meth:`~repathlib.repathlib.PosixPath.finditer`
   - :meth:`~repathlib.repathlib.PosixPath.reiterdir`

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

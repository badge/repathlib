API
===

This documentation includes only those methods that have been added to
the base :py:class:`pathlib.Path` class; refer to that class's
documentation for everything else. In addition, ``pathlib.Path``'s
definition overrides the ``__new__`` method to construct either a
``PosixPath`` or a ``WindowsPath``. This doesn't have any impact on the
end user, but means we have to include one of those classes here to use
autodoc:.

.. autoclass:: repathlib.repathlib.PosixPath

   .. automethod:: repathlib.repathlib.PosixPath.search
   .. automethod:: repathlib.repathlib.PosixPath.match_
   .. automethod:: repathlib.repathlib.PosixPath.fullmatch
   .. automethod:: repathlib.repathlib.PosixPath.findall
   .. automethod:: repathlib.repathlib.PosixPath.finditer
   .. automethod:: repathlib.repathlib.PosixPath.reiterdir

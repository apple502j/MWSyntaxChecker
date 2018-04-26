"""Subpackage containing all checks to use."""
import pkgutil

__all__ = []
for _loader, _modname, _is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(_modname)
    globals()[_modname] = _loader.find_module(
        _modname
    ).load_module(_modname)

del pkgutil

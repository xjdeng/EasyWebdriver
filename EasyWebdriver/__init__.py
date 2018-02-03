try:
    from .main import Chrome, Firefox
except ImportError:
    from main import Chrome, Firefox
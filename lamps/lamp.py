try:
    import unicornhat as unicorn
    print("unicorn hat detected")
except ImportError:
    from .fakeunicorn import unicornhat as unicorn


class Lamp:
    """
    The lamp class definition
    """

    def __init__(self, brightness=1):
        """
        docstring
        """
        unicorn.brightness(brightness)

    @staticmethod
    def set_all(red, green, blue):
        """
        docstring
        """
        unicorn.set_all(red, green, blue)

    @staticmethod
    def show():
        """
        docstring
        """
        unicorn.show()

    @staticmethod
    def clear():
        """
        docstring
        """
        unicorn.clear()

    @staticmethod
    def get_pixel(x, y):
        """
        docstring
        """
        unicorn.get_pixel(x, y)

    @staticmethod
    def off():
        """
        docstring
        """
        unicorn.off()

    @staticmethod
    def brightness(b):
        """
        docstring
        """
        unicorn.brightness(b)

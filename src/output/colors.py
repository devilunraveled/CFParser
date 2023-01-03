class Color :
    Base = "\033[38;5;"
    End = "m"
    Black = Base + "000" + End
    Red = Base + "001" + End
    Green = Base + "002" + End
    Blue = Base + "004" + End
    Orange = Base + "209" + End
    Violet = Base + "201" + End
    Cyan = Base + "086" + End
    Reset = "\033[0m"

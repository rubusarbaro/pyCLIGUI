from functions import clear_screen

class screen :
    def __init__(self, width: int , height: int, border_style: str) :
        self.width = width
        self.height = height
        self.border_icon = border_style

        self.layout = self.build_layout()
    
    def build_layout(self) :
        ud_border = []
        for x in range(0, self.width) :
            ud_border.append(self.border_icon)
        
        layout = []
        layout.append(ud_border)

        for y in range(0, self.height-2) :
            row = []
            row.append(self.border_icon)

            for z in range(0, self.width-2) :
                row.append("  ")
            row.append(self.border_icon)
            layout.append(row)

        layout.append(ud_border)
        return layout

    def print_screen(self) :

        """
        Print the layout in the "screen" class object.
        """

        # Clean the last screen printed.    
        clear_screen()

        # First, it iterates every sublist in the list "layout". Then, it iterates every item in the sublist.
        # It concatenates every item in the sublist to create a row. It prints the row.
        for line in self.layout :
            row = ""
            for item in line :
                row += item
            print(row)

class Application(object):
    def __init__(self, name, **params):
        self._name = name
        self._menu = params.get('menu')
        self._divider_width = params.get('divider_width', 50)

    def menu(self):
        print('=' * self._divider_width)
        print(f"\t\t{self._name}!")
        print('=' * self._divider_width)
        for i, option in enumerate(self._menu['options'], start=1):
            print(f"{i}. {option}")
        print('=' * self._divider_width)
        
        return int(input(f'{self._menu["prompt"]}'))
        

    def run(self):
        _running = True
        while _running: 
            choice = self.menu()
            match choice:
                case 1:
                    print("1")
                case 2:
                    print("2")
                case 3:
                    print('3')
                case 4:
                    print("4")
                case 5:
                    _running = False
                case _:
                    print("Invalid choice. Please try again.")
                    
class Page():
    def __init__(self) -> None:
        self.references = dict()

    def add_reference(self, var:str, val:float):
        self.references[var] = val
        print(f"Assigned {var} = {val}")

    def find_reference(self, var: str):
        try:
            return self.references[var]
        except KeyError:
            print(f"Variable {var} not found")
            return None
        except Exception as e:
            print("Exception Occured")
            print(e)
            return None


class Pager():
    def __init__(self) -> None:
        self.currentPage = None
        self.pages:dict = {}

    def new_page(self, number) -> Page:
        self.pages[number] = Page()

    def switch_page(self, number) -> Page:
        self.currentPage = number

    def add(self, var, value: float):
        try:
            self.pages[self.currentPage].add_reference(var, value)
        except:
            print("No page Exists")

    def find(self, var) -> float:
        try:
            return self.pages[self.currentPage].find_reference(var)
        except KeyError:
            print(self.pages)
            print(f"Page {self.currentPage} does not exist")
            return None

    def show_references(self) -> None:
        if self.currentPage is None:
            print("No current page selected")
            return
        page = self.pages[self.currentPage]
        if not page.references:
            print("No references in the current page")
            return
        for var, val in page.references.items():
            print(f"{var} = {val}")

pager = Pager()
pager.new_page('0')
pager.switch_page('0')

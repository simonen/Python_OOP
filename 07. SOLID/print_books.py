from abc import ABC, abstractmethod


class Printable(ABC):
    def __init__(self, content: str):
        self.content = content

    @abstractmethod
    def get_content(self):
        ...

class PrintingDevice(ABC):
    @abstractmethod
    def print(self, formatted: Printable) -> str:
        ...

    def __str__(self) -> str:
        return self.__class__.__name__

class Book(Printable):

    def get_content(self):
        return self.content

    def __str__(self):
        return self.content

class Image(Printable):
    def get_content(self):
        return self.content

class Formatter(ABC):
    @abstractmethod
    def format(self, printable: Printable) -> Printable:
        ...

    def __str__(self) -> str:
        return self.__class__.__name__

class BasicFormatter(Formatter):
    def format(self, printable: Printable) -> Printable:
        new_content = f"Basically formatted \"{printable.content}\""
        printable.content = new_content
        return Book(new_content)


class Colorizer(Formatter):
    def format(self, printable: Printable) -> Printable:
        ...


class FormatterFactory:
    _registry: dict[type[Printable], type[Formatter]] = {
        Book: BasicFormatter,
        Image: Colorizer,
    }

    @classmethod
    def create_for(cls, printable: Printable) -> Formatter:
        formatter_cls = cls._registry.get(type(printable), None)
        if formatter_cls is None:
            raise ValueError(f"No formatter registered for ...")
        return formatter_cls()


class Plotter(PrintingDevice):
    def print(self, formatted: Printable) -> str:
        return f"Plotting {formatted.content}...."


class Process:
    def __init__(self, printer: PrintingDevice, formatter: Formatter, printable: Printable) -> None:
        self.printer = printer
        self.formatter = formatter
        self.printable = printable

    def print(self):
        formatted_book = self.formatter.format(self.printable)
        return self.printer.print(formatted_book)


book = Book('Book of Books')
canon = Plotter()
formatter = FormatterFactory.create_for(book)

process = Process(canon, formatter, book)
print(process.print())
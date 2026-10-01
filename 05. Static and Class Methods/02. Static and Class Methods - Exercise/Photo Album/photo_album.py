from math import ceil


class PhotoAlbum:
    SLOTS: int = 4                   # per page

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls.SLOTS)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for page in range(self.pages):
            if len(self.photos[page]) < self.SLOTS:
                    self.photos[page].append(label)
                    return (f"{label} photo added successfully on page {page + 1}"
                            f" slot {len(self.photos[page])}")

        return "No more free slots"

    def display(self) -> str:
        res = []
        for page in self.photos:
            res.append('-' * 11)
            res.append(" ".join(['[]' for _ in page]))
        res.append('-' * 11)
        return "\n".join(res)


album = PhotoAlbum(2)
print(album.photos)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.display())

# photo_count = 9
# cols = 4
# rows = ceil(photo_count / cols)
class PhotoAlbum:

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4 if photos_count % 4 == 0 else (photos_count // 4) + 1
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[self.pages - 1]) == 4:
            return "No more free slots"

        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"

    def display(self):
        photo_slots = list(map(lambda x: ['[]'] * len(x), self.photos))
        res = []
        if self.pages > 0:
            res.append(f"{'-' * 11}")
        for i in photo_slots:
            res.append(f"{' '.join(i)}\n{'-' * 11}")

        return '\n'.join(res)


album = PhotoAlbum(2)
album2 = PhotoAlbum.from_photos_count(0)
print(album2.display())
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())

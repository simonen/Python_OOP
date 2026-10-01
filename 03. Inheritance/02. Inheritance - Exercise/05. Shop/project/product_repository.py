from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def _find_by_name(self, product_name: str) -> Product | None:
        return next((p for p in self.products if p.name == product_name), None)

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str):
        product = self._find_by_name(product_name)
        return product if product else None

    def remove(self, product_name: str):
        product = self._find_by_name(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
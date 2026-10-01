from project.category import Category
from project.topic import Topic
from project.document import Document
from typing import TypeVar


T = TypeVar("T", Document, Topic, Category)

class Storage:
    def __init__(self) -> None:
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def _find_object(self, object_id, store: list[T]) -> T | None:
        value = next(filter(lambda x: x.id == object_id, store), None)
        return value

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = self._find_object(category_id, self.categories)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self._find_object(topic_id, self.topics)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = self._find_object(document_id, self.documents)
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id) -> None:
        category = self._find_object(category_id, self.categories)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = self._find_object(topic_id, self.topics)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = self._find_object(document_id, self.documents)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id: int) -> Document | None:
        document = self._find_object(document_id, self.documents)
        return document

    def __repr__(self) -> str:
        return "\n".join(str(x) for x in self.documents)

from typing import Generic, Type, TypeVar, List, Optional, Iterable
from sqlalchemy.orm import Session
from sqlalchemy import select

T = TypeVar('T')

class Repository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def add(self, entity: T) -> T:
        self.session.add(entity)
        return entity

    def get(self, id_: int) -> Optional[T]:
        return self.session.get(self.model, id_)

    def list(self) -> List[T]:
        return list(self.session.scalars(select(self.model)))

    def delete(self, entity: T) -> None:
        self.session.delete(entity)

    def add_all(self, items: Iterable[T]) -> None:
        self.session.add_all(list(items))

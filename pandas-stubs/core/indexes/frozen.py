from typing import Generic, Iterator, List, overload, TypeVar, Union


_T = TypeVar("_T")


class FrozenList(Generic[_T]):
    @overload
    def __getitem__(self, idx: int) -> _T:
        ...

    @overload
    def __getitem__(self, idx: Union[List[int], slice]) -> FrozenList[_T]:
        ...

    def __iter__(self) -> Iterator[_T]:
        ...

    def __len__(self) -> int:
        ...

    def __contains__(self, key: object) -> bool:
        ...

    def __reversed__(self) -> FrozenList[_T]:
        ...

    def __radd__(self, other: Union[FrozenList[_T], List[_T], Tuple[_T, ...]]) -> FrozenList[_T]:
        ...

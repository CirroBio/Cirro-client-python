from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_definition import ColumnDefinition


T = TypeVar("T", bound="Table")


@_attrs_define
class Table:
    """
    Attributes:
        desc (str):
        cols (List['ColumnDefinition']):
        name (Union[Unset, str]): User-friendly name of asset
        type (Union[Unset, str]): Type of file Example: parquet.
        rows (Union[Unset, int]): Number of rows in table
        path (Union[Unset, str]): Relative path to asset
    """

    desc: str
    cols: List["ColumnDefinition"]
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    rows: Union[Unset, int] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        desc = self.desc

        cols = []
        for cols_item_data in self.cols:
            cols_item = cols_item_data.to_dict()
            cols.append(cols_item)

        name = self.name

        type = self.type

        rows = self.rows

        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "desc": desc,
                "cols": cols,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if rows is not UNSET:
            field_dict["rows"] = rows
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.column_definition import ColumnDefinition

        d = src_dict.copy()
        desc = d.pop("desc")

        cols = []
        _cols = d.pop("cols")
        for cols_item_data in _cols:
            cols_item = ColumnDefinition.from_dict(cols_item_data)

            cols.append(cols_item)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        rows = d.pop("rows", UNSET)

        path = d.pop("path", UNSET)

        table = cls(
            desc=desc,
            cols=cols,
            name=name,
            type=type,
            rows=rows,
            path=path,
        )

        table.additional_properties = d
        return table

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

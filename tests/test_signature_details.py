import typing

import pytest

from ninja.signature.details import is_collection_type


@pytest.mark.parametrize(
    ("annotation", "expected"),
    [
        pytest.param(typing.List, True, id="true_for_typing_List"),
        pytest.param(list[int], True, id="true_for_parameterized_native_list"),
        pytest.param(list, True, id="true_for_native_list"),
        pytest.param(typing.Set, True, id="true_for_typing_Set"),
        pytest.param(set[int], True, id="true_for_parameterized_native_set"),
        pytest.param(set, True, id="true_for_native_set"),
        pytest.param(typing.Tuple, True, id="true_for_typing_Tuple"),
        pytest.param(tuple[int], True, id="true_for_parameterized_native_tuple"),
        pytest.param(tuple, True, id="true_for_native_tuple"),
        pytest.param(
            type("Custom", (), {}),
            False,
            id="false_for_custom_type_without_typing_origin",
        ),
        pytest.param(
            typing.NewType("SomethingNew", str),
            False,
            id="false_for_instance_without_typing_origin",
        ),
    ],
)
def test_is_collection_type_returns(annotation: typing.Any, expected: bool):
    assert is_collection_type(annotation) is expected

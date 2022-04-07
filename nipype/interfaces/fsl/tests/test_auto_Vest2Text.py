# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Vest2Text


def test_Vest2Text_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=0,
        ),
        out_file=dict(
            argstr="%s",
            extensions=None,
            position=1,
            usedefault=True,
        ),
        output_type=dict(),
    )
    inputs = Vest2Text.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Vest2Text_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = Vest2Text.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

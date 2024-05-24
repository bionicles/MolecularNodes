import molecularnodes as mn
import molecularnodes.blender as bl
import pytest

from .constants import data_dir, attributes
from .utils import sample_attribute, NumpySnapshotExtension

mn.unregister()
mn.register()


formats = ["mol", "sdf"]


@pytest.mark.parametrize("format", formats)
def test_open(snapshot_custom, format):
    molecule = mn.io.parse.SDF(data_dir / f"caffeine.{format}")

    assert molecule.array
    assert molecule.file


@pytest.mark.parametrize("format", formats)
@pytest.mark.parametrize("style", ["ball_and_stick", "spheres", "surface"])
def test_load(snapshot_custom: NumpySnapshotExtension, format, style):
    mol = mn.io.load(data_dir / f"caffeine.{format}", style=style)
    assert mol.object

    if style == "spheres":
        bl.nodes.get_style_node(mol.object).inputs["EEVEE"].default_value = True
    mn.blender.nodes.realize_instances(mol.object)

    for attribute in attributes:
        assert snapshot_custom == sample_attribute(mol, attribute, evaluate=True)

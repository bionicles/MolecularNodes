import bpy
import pytest
import numpy as np
import molecularnodes as mn

from .utils import sample_attribute, NumpySnapshotExtension
from .constants import (
    data_dir,
    codes,
    attributes
)

# register the operators, which isn't done by default when loading bpy
# just via headless float_decimals
mn.unregister()
mn.register()


@pytest.mark.parametrize("code", codes)
def test_op_api_cartoon(snapshot_custom: NumpySnapshotExtension, code, style='ribbon', format="bcif"):
    scene = bpy.context.scene
    scene.MN_import_node_setup = True
    scene.MN_pdb_code = code
    scene.MN_import_style = style
    scene.MN_import_node_setup = True
    scene.MN_import_build_assembly = False
    scene.MN_import_centre = False
    scene.MN_import_del_solvent = False
    scene.MN_import_format_download = format

    bpy.ops.mn.import_wwpdb()

    obj_1 = bpy.context.active_object
    obj_2 = mn.io.fetch(code, style=style, format=format).object

    # objects being imported via each method should have identical snapshots
    for mol in [obj_1, obj_2]:
        for name in attributes:
            if name == "sec_struct" or name.startswith("."):
                continue
            assert snapshot_custom == sample_attribute(
                mol, name, evaluate=True)


@pytest.mark.parametrize("code", codes)
@pytest.mark.parametrize("file_format", ['bcif', 'cif', 'pdb'])
def test_op_local(snapshot_custom, code, file_format):
    scene = bpy.context.scene
    scene.MN_import_node_setup = False
    scene.MN_import_build_assembly = False
    scene.MN_import_del_solvent = False
    scene.MN_import_format_download = file_format
    path = str(mn.io.download(code=code, format=file_format, cache=data_dir))
    scene.MN_import_local_path = path
    scene.MN_centre_type = 'centroid'

    scene.MN_import_centre = False
    bpy.ops.mn.import_protein_local()
    bob = bpy.data.objects[-1]

    scene.MN_import_centre = True
    bpy.ops.mn.import_protein_local()
    bob_centred = bpy.data.objects[-1]

    bob_pos = sample_attribute(bob, 'position', n=10, evaluate=False)
    assert snapshot_custom == bob_pos
    bob_centred_pos = sample_attribute(
        bob_centred, 'position', n=10, evaluate=False)
    assert snapshot_custom == bob_centred_pos
    assert not np.allclose(bob_pos, bob_centred_pos)


def test_op_api_mda(snapshot_custom: NumpySnapshotExtension):
    topo = str(data_dir / "md_ppr/box.gro")
    traj = str(data_dir / "md_ppr/first_5_frames.xtc")
    name = bpy.context.scene.MN_import_md_name

    bpy.context.scene.MN_import_md_topology = topo
    bpy.context.scene.MN_import_md_trajectory = traj
    bpy.context.scene.MN_import_style = 'ribbon'

    bpy.ops.mn.import_protein_md()
    obj_1 = bpy.context.active_object
    assert obj_1.name == name
    assert not bpy.data.collections.get(f"{name}_frames")

    bpy.context.scene.MN_md_in_memory = True
    name = 'NewTrajectoryInMemory'

    obj_2, universe = mn.io.md.load(topo, traj, name="test", style='ribbon')
    frames_coll = bpy.data.collections.get(f"{obj_2.name}_frames")

    assert not frames_coll

    for mol in [obj_1, obj_2]:
        for att in attributes:
            assert snapshot_custom == sample_attribute(mol, att)

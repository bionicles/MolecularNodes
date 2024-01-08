import bpy
import pytest
import molecularnodes as mn
from .utils import evaluate
from .constants import (
    test_data_directory, 
    codes
)
from molecularnodes.io.mda import HAS_mda

if HAS_mda:
    import MDAnalysis as mda
from .utils import apply_mods, sample_attribute_to_string

# register the operators, which isn't done by default when loading bpy
# just via headless float_decimals
mn.unregister()
mn.register()


@pytest.mark.parametrize("code", codes)
def test_op_api_cartoon(snapshot, code, style = 'ribbon', file_format = "mmtf"):
    scene = bpy.context.scene
    scene.MN_import_node_setup = True
    scene.MN_pdb_code = code
    scene.MN_import_style = style
    scene.MN_import_node_setup = True
    scene.MN_import_build_assembly = False
    scene.MN_import_centre = False
    scene.MN_import_del_solvent = False
    scene.MN_import_format_download = file_format
    
    bpy.ops.mn.import_protein_rcsb()
    
    obj_1 = bpy.context.active_object
    obj_2 = mn.io.pdb.load(code, style=style, file_format = file_format)
    
    # objects being imported via each method should have identical snapshots
    for model in [obj_1, obj_2]:
        object = evaluate(model)
        for name in object.data.attributes.keys():
            if name == "sec_struct" or name.startswith("."):
                continue
            snapshot.assert_match(
                sample_attribute_to_string(object, name), 
                f"{name}.txt"
            )

def test_op_api_mda(snapshot):
    topo = str(test_data_directory / "md_ppr/box.gro")
    traj = str(test_data_directory / "md_ppr/first_5_frames.xtc")
    name = bpy.context.scene.MN_import_md_name
    
    bpy.context.scene.MN_import_md_topology  = topo
    bpy.context.scene.MN_import_md_trajectory  = traj
    
    bpy.ops.mn.import_protein_md()
    obj_1 = bpy.context.active_object
    assert obj_1.name == name
    assert not bpy.data.collections.get(f"{name}_frames")
    
    bpy.context.scene.MN_md_in_memory = True
    name = 'NewTrajectoryInMemory'
    
    obj_2, universe = mn.io.md.load(topo, traj, name = "test", style = 'ribbon')
    frames_coll = bpy.data.collections.get(f"{obj_2.name}_frames")
    
    assert not frames_coll
    
    for mol in [obj_1, obj_2]:
        apply_mods(mol)
        for att in mol.data.attributes.keys():
            snapshot.assert_match(
                sample_attribute_to_string(mol, att), 
                f"{att}.txt"
            )

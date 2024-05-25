import bpy
from bpy.props import BoolProperty, StringProperty, EnumProperty, IntProperty

bpy.types.Scene.MN_import_centre = BoolProperty(
    name="Centre Structure",
    description="Move the imported Molecule on the World Origin",
    default=False,
)

bpy.types.Scene.MN_centre_type = EnumProperty(
    name="Method",
    default="mass",
    items=(
        (
            "mass",
            "Mass",
            "Adjust the structure's centre of mass to be at the world origin",
            1,
        ),
        (
            "centroid",
            "Centroid",
            "Adjust the structure's centroid (centre of geometry) to be at the world origin",
            2,
        ),
    ),
)

bpy.types.Scene.MN_import_del_solvent = BoolProperty(
    name="Remove Solvent",
    description="Delete the solvent from the structure on import",
    default=True,
)
bpy.types.Scene.MN_import_panel_selection = IntProperty(
    name="MN_import_panel_selection",
    description="Import Panel Selection",
    subtype="NONE",
    default=0,
)
bpy.types.Scene.MN_import_build_assembly = BoolProperty(name="Build Assembly", default=False)
bpy.types.Scene.MN_import_node_setup = BoolProperty(
    name="Setup Nodes",
    default=True,
    description="Create and set up a Geometry Nodes tree on import",
)


class MolecularNodesObjectProperties(bpy.types.PropertyGroup):
    subframes: IntProperty(  # type: ignore
        name="Subframes",
        description="Number of subframes to interpolate for MD trajectories",
        default=0,
    )
    molecule_type: StringProperty(  # type: ignore
        name="Molecular Type",
        description="How the file was imported, dictating how MN interacts with it",
        default="",
    )
    pdb_code: StringProperty(  # type: ignore
        name="PDB",
        description="PDB code used to download this structure",
        maxlen=4,
        options={"HIDDEN"},
    )

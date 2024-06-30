from .func import button_custom_iswitch

menu_items = {
    "style": [
        {
            "label": "Spheres",
            "name": "Style Spheres",
            "description": "Style to apply the traditional space-filling atomic representation of atoms. Spheres are scaled based on the `vdw_radii` attribute. By default the _Point Cloud_ rendering system is used, which is only visible inside of Cycles.",
            "video_url": "https://imgur.com/KjKkF2u",
        },
        {
            "label": "Cartoon",
            "name": "Style Cartoon",
            "description": "Style to apply the traditional cartoon representation of protein structures. This style highlights alpha-helices and beta-sheets with arrows and cylinders.",
            "video_url": "https://imgur.com/1xmdfxZ",
        },
        {
            "label": "Ribbon",
            "name": "Style Ribbon",
            "description": "Style that creates a continuous solid ribbon or licorice tube through the backbones of peptides and nucleic acids.",
            "video_url": "https://imgur.com/iMxEJaH",
        },
        {
            "label": "Surface",
            "name": "Style Surface",
            "description": "Style that creates a surface representation based on the proximity of atoms to a probe that is moved through the entire structure.",
            "video_url": "https://imgur.com/ER8pcYf",
        },
        {
            "label": "Ball and Stick",
            "name": "Style Ball and Stick",
            "description": "Style that creates cylinders for bonds and spheres for atoms. The atoms can be either Eevee or Cycles compatible, with customisation to resolution and radius possible.",
            "video_url": "https://imgur.com/kuWuOsw",
        },
        {
            "label": "Sticks",
            "name": "Style Sticks",
            "description": "Style that creates a cylinder for each bond. Cylindrical caps to the cylinders are currently not supported. Best to use [`Style Ball and Stick`](#style-ball-and-stick).",
            "video_url": "https://imgur.com/4ZK1AMo",
        },
        {
            "label": "Preset 1",
            "name": "Style Preset 1",
            "description": "Quickly switch between several different pre-made preset styles. Best used when using MolecularNodes via scripts, ensuring all atoms are displayed using a combination of cartoons and atoms.",
            "video_url": "https://imgur.com/gCQRWBk.mp4",
        },
        {
            "label": "Preset 2",
            "name": "Style Preset 2",
            "description": "Quickly switch between several different pre-made preset styles. Best used when using MolecularNodes via scripts, ensuring all atoms are displayed using a combination of cartoons and atoms.",
            "video_url": "https://imgur.com/gCQRWBk.mp4",
        },
        {
            "label": "Preset 3",
            "name": "Style Preset 3",
            "description": "Quickly switch between several different pre-made preset styles. Best used when using MolecularNodes via scripts, ensuring all atoms are displayed using a combination of cartoons and atoms.",
            "video_url": "https://imgur.com/gCQRWBk.mp4",
        },
        {
            "label": "Preset 4",
            "name": "Style Preset 4",
            "description": "Quickly switch between several different pre-made preset styles. Best used when using MolecularNodes via scripts, ensuring all atoms are displayed using a combination of cartoons and atoms.",
            "video_url": "https://imgur.com/gCQRWBk.mp4",
        },
    ],
    "select": [
        {
            "label": "Separate Atoms",
            "name": "Separate Atoms",
            "description": "Select only the desired input atoms. The output is bits of geometry, which include the selection and include the inverse of the selected atoms. You can expand the selection to include an entire residue if a single atom in that residue is selected, by setting `Whole Residue` to `True`.",
            "video_url": "https://imgur.com/VsCW0HY",
        },
        {
            "label": "Separate Polymers",
            "name": "Separate Polymers",
            "description": "Separate the input atomic geometry into it's different polymers or `Protein`, `Nucleic Acid` and `other`.",
            "video_url": "https://imgur.com/ICQZxxz",
        },
        "break",
        {
            "label": "custom",
            "function": button_custom_iswitch,
            "values": [
                {
                    "label": "Chain",
                    "field": "chain_id",
                    "dtype": "BOOLEAN",
                    "name": "Select Chain_",
                    "prefix": "",
                    "property_id": "chain_ids",
                    "description": "Select single or multiple of the different chains. Creates a selection based on the `chain_id` attribute.",
                    "video_url": "https://imgur.com/P9ZVT2Z",
                },
                {
                    "label": "Entity",
                    "field": "entity_id",
                    "name": "Select Entity_",
                    "dtype": "BOOLEAN",
                    "prefix": "",
                    "property_id": "entity_ids",
                    "description": "Select single or multiple of the different entities. Creates a selection based on the `entity_id` attribute.",
                    "video_url": "https://imgur.com/fKQIfGZ",
                },
                {
                    "label": "Segment",
                    "field": "segid",
                    "name": "Select Segment_",
                    "dtype": "BOOLEAN",
                    "prefix": "",
                    "property_id": "segments",
                    "description": "",
                },
                {
                    "label": "Ligand",
                    "field": "res_name",
                    "name": "Select Ligand_",
                    "dtype": "BOOLEAN",
                    "prefix": "",
                    "property_id": "ligands",
                    "description": "Select single or multiple of the different ligands.",
                    "video_url": "https://imgur.com/s2seWIw",
                },
            ],
        },
        "break",
        {
            "label": "Attribute",
            "name": "Select Attribute",
            "description": "Select atoms that have true for the given attribute name.",
        },
        {
            "label": "Is Peptide",
            "name": "Is Peptide",
            "description": "Select the atoms involved in a peptide chain.",
        },
        {
            "label": "Is Nucleic",
            "name": "Is Nucleic",
            "description": "Select the atoms involved in nucleic acid polymer.",
        },
        {
            "label": "Is Lipid",
            "name": "Is Lipid",
            "description": "Select the atoms involved in lipid molecules.",
        },
        {
            "label": "Is Solvent",
            "name": "Is Solvent",
            "description": "Select the atoms that are part of the solvent.",
        },
        "break",
        {
            "label": "Atomic Number",
            "name": "Select Atomic Number",
            "description": "Select single elements, by matching to the `atomic_number` field. Useful for selecting single elements, or combining to select elements higher than 20 on the periodic table.",
            "video_url": "https://imgur.com/Bxn33YK",
        },
        {
            "label": "Element",
            "name": "Select Element",
            "description": "Select individual elements, for the first 20 elements on the periodic table. For selections of higher elements, use [`MN_select_atomic_number`](#select-atomic-number). Creating a node which includes more elements becomes too large to be practical.",
            "video_url": "https://imgur.com/nRQwamG",
        },
        "break",
        {
            "label": "Bonded",
            "name": "Select Bonded",
            "description": "Based on an initial selection, finds atoms which are within a certain number of bonds of this selection. Output can include or excluded the original selection.",
            "video_url": "https://imgur.com/g8hgXup",
        },
        {
            "label": "Res Whole",
            "name": "Select Res Whole",
            "description": "Expand the given selection to include a whole residue, if a single atom in that residue is selected. Useful for when a distance or proximity selection includes some of the residue and you wish to include all of the residue.",
            "video_url": "https://imgur.com/JFzwE0i",
        },
        "break",
        {
            "label": "Is Alpha Carbon",
            "name": "Is Alpha Carbon",
            "description": "Select the alpha carbons of a peptide.",
        },
        {
            "label": "Is Backbone",
            "name": "Is Backbone",
            "description": "Select the backbone atoms of a peptide or nucleic acid polymer.",
        },
        {
            "label": "Is Side Chain",
            "name": "Is Side Chain",
            "description": "Select the side chain atoms of a peptide or nucleic acid polymer.",
        },
        {
            "label": "Is Helix",
            "name": "Is Helix",
            "description": "Select the atoms in a alpha-helix or similar.",
        },
        {
            "label": "Is Sheet",
            "name": "Is Sheet",
            "description": "Select the atoms in a beta-sheet or similar.",
        },
        {
            "label": "Is Loop",
            "name": "Is Loop",
            "description": "Select the atoms not in a sheet or helix.",
        },
        "break",
        {
            "label": "Res ID",
            "name": "mn.residues_selection_custom",
            "backup": "Select Res ID_",
            "description": "Create a more complex selection for the `res_id` field, by specifying multiple ranges and potential single `res_id` numbers. This node is built uniquely each time, to the inputs will look different for each user.\nIn the example below, residues 10 & 15 are selected, as well as residues between and including 20-100.\nThe node was created by inputting `10, 15, 20-100` into the node creation field.",
            "video_url": "https://imgur.com/OwAXsbG",
        },
        {
            "label": "Res ID Single",
            "name": "Select Res ID",
            "description": "Select a atoms based on their `res_id` number.",
            "video_url": "https://imgur.com/BL6AOP4",
        },
        {
            "label": "Res ID Range",
            "name": "Select Res ID Range",
            "description": "Select multiple residues by specifying a _Min_ and a _Max_, defining a range that includes or excludes based on the `res_id` number.",
            "video_url": "https://imgur.com/NdoQcdE",
        },
        {
            "label": "Res Name",
            "name": "Select Res Name",
            "description": "Select protein or nucleic acids based on their residue name.",
            "video_url": "https://imgur.com/kjzH9Rs",
        },
        "break",
        {
            "label": "Cube",
            "name": "Select Cube",
            "description": "Create a selection that is inside the `Empty_Cube` object. When this node is first created, an _empty_ object called `Empty_Cube` should be created. You can always create additional empty objects through the add menu, to use a different object. The rotation and scale of the object will be taken into account for the selection.",
            "video_url": "https://imgur.com/P4GZ7vq",
        },
        {
            "label": "Sphere",
            "name": "Select Sphere",
            "description": "Create a selection that is within a spherical radius of an object, based on that object's scale. By default an _empty_ object called `Empty_Sphere` is created. You can use other objects or create a new empty to use. The origin point for the object will be used, which should be taken in to account when using molecules. Use [`MN_select_proximity`](#select-proximity) for selections which are within a certain distance of a selection of atoms instead of a single origin point.",
            "video_url": "https://imgur.com/xdeTZR7",
        },
        {
            "label": "Proximity",
            "name": "Select Proximity",
            "description": "Create a selection based on the proximity to the Target Atoms of the input. A sub-selection of the Target atoms can be used if the `Selection` input is used. You can expand the selection to include an entire residue if a single atom in that residue is selected, by setting `Whole Residue` to `True`.\nIn the example below, the `Style Atoms` is being applied to a selection, which is being calculated from the proximity of atoms to specific chains. As the cutoff for the selection is changed, it includes or excludes more atoms. The `Whole Residue` option also ensures that entire residues are shown.",
            "video_url": "https://imgur.com/RI80CRY",
        },
    ],
    "color": [
        {
            "label": "Set Color",
            "name": "Set Color",
            "description": "The is the primary way to change the color of structures in Molecular Nodes. Colors for cartoon and ribbon are taken from the _alpha-carbons_ of the structures. Change the color of the input atoms, based on a selection and a color field. The color field can be as complex of a calculation as you wish. In the example below the color for the whole structure can be set, or the color can be based on a color for each chain, or the result of mapping a color to an attribute such as `b_factor`.",
            "video_url": "https://imgur.com/667jf0O",
        },
        "break",
        {
            "label": "custom",
            "function": button_custom_iswitch,
            "values": [
                {
                    "label": "Chain",
                    "field": "chain_id",
                    "dtype": "RGBA",
                    "name": "Color Chain_",
                    "prefix": "",
                    "property_id": "chain_ids",
                    "description": "Choose the colors for individual chains in the structure. This node is generated for each particular molecule, so the inputs will look different based on the imported structure. For larger structures with many chains this node may become too large to be practical, in which case you might better use [`Color Entity ID`](#color-entity-id).",
                    "video_url": "https://imgur.com/9oM24vB",
                },
                {
                    "label": "Segment",
                    "field": "segid",
                    "name": "Color Segment_",
                    "dtype": "RGBA",
                    "prefix": "",
                    "property_id": "segments",
                    "description": "",
                },
                {
                    "label": "Entity",
                    "field": "entity_id",
                    "name": "Color Entity_",
                    "dtype": "RGBA",
                    "prefix": "",
                    "property_id": "entity_ids",
                    "description": "Choose the colors for individual entities in the structure. Multiple chains may be classified as the same entity, if they are copies of the same chain but in different conformations or positions and rotations. The nodes is generated for each individual structure, if `entity_id` is available.",
                    "video_url": "https://imgur.com/kEvj5Jk",
                },
                {
                    "label": "Ligand",
                    "field": "res_name",
                    "name": "Color Ligand_",
                    "dtype": "RGBA",
                    "prefix": "",
                    "property_id": "ligands",
                    "description": "Choose the colors for individual ligands in the structure.",
                    "video_url": "https://imgur.com/bQh8Fd9",
                },
            ],
        },
        "break",
        {
            "label": "Goodsell Colors",
            "name": "Color Goodsell",
            "description": "Change the inputted color to be darker for non-carbon atoms. Creates a _Goodsell Style_ color scheme for individual chains.",
            "video_url": "https://imgur.com/gPgMSRa",
        },
        {
            "label": "Rainbow",
            "name": "Color Rainbow",
            "description": "Generate a rainbow color palette, that changes over from start to finish along a peptide chain. Can be one rainbow over the entire structure, or create a rainbow of a per-chani basis.",
        },
        {
            "label": "Attribute Map",
            "name": "Color Attribute Map",
            "description": "Interpolate between two or three colors, based on the value of an attribute field such as `b_factor`. Choosing the minimum and maximum values with the inputs.",
            "video_url": "https://imgur.com/lc2o6e1",
        },
        {
            "label": "Attribute Random",
            "name": "Color Attribute Random",
            "description": "Generate a random color, based on the given attribute. Control the lightness and saturation of the color with the inputs.",
            "video_url": "https://imgur.com/5sMcpAu",
        },
        {"label": "Backbone", "name": "Color Backbone", "description": ""},
        {
            "label": "pLDDT",
            "name": "Color pLDDT",
            "description": "Assigns colors using the `b_factor` attribute, which contains the `pLDDT` attribute for models that come from AlphaFold.",
        },
        {
            "label": "Backbone",
            "name": "Color Backbone",
            "description": "Color atoms by whether or not they form part of a peptide or nucleic backbone",
        },
        {
            "label": "Secondary Structure",
            "name": "Color Sec Struct",
            "description": "Choose a color for the different secondary structures, based on the `sec_struct` attribute.",
            "video_url": "https://imgur.com/wcJAUp9",
        },
        "break",
        {
            "label": "Element",
            "name": "Color Element",
            "description": "Choose a color for each of the first 20 elements on the periodic table. For higher atomic number elements use [`Color Atomic Number`](#color-atomic-number).",
            "video_url": "https://imgur.com/iMGZKCx",
        },
        {
            "label": "Atomic Number",
            "name": "Color Atomic Number",
            "description": "Choose a color for an individual element. Select the element based on `atomic_number`. Useful for higher atomic number elements which are less commonly found in structures.",
            "video_url": "https://imgur.com/pAloaAF",
        },
        {
            "label": "Res Name",
            "name": "Color Res Name",
            "description": "Choose a color for each of the 20 naturally occurring amino acids or the 4 base nucleic acids (DNA / RNA)",
            "video_url": "https://imgur.com/1yhSVsW",
        },
        {
            "label": "Common Elements",
            "name": "Color Common",
            "description": "Choose a color for each of the common elements. This is a smaller convenience node for elements which commonly appear in macromolecular structures",
            "video_url": "https://imgur.com/GhLdNwy",
        },
    ],
    "topology": [
        {
            "label": "Find Bonds",
            "name": "Topology Find Bonds",
            "description": "Finds bonds between atoms based on distance. Based on the vdw_radii for each point, finds other points within a certain radius to create a bond to. Does not preserve the index for the points, detect bond type, or transfer all attributes",
            "video_url": "https://imgur.com/oUo5TsM",
        },
        {
            "label": "Break Bonds",
            "name": "Topology Break Bonds",
            "description": "Will delete a bond between atoms that already exists based on a distance cutoff, or is selected in the `Selection` input. Leaves the atoms unaffected",
            "video_url": "https://imgur.com/n8cTN0k",
        },
        {
            "label": "Compute Backbone",
            "name": "Topology Compute Backbone",
            "description": "Gets the backbone positions for each AA residue and stores them as attributes, and additionally computes the phi and psi angles for each residue in radians.\n\nIn the video example, the Phi and Psi angles are mapped from (-Pi, Pi) to (0, 1), which is used in the Color Ramp node to choose colors. This is computed on the alpha carbons, but can be used on any of the resulting atoms for the corresponding residues, which is shown in the second video.",
            "video_url": ["https://imgur.com/9DNzngY", "https://imgur.com/W3P9l10"],
        },
        {
            "label": "DSSP",
            "name": "Topology DSSP",
            "description": "Calculate the secondary structure of a structure, storing it on the `sec_struct` attribute.",
        },
        "break",
        {
            "label": "Res Info",
            "name": "Res Info",
            "description": "Read information about the atoms with the context of each residue the atom is in",
        },
        {
            "label": "Chain Info",
            "name": "Chain Info",
            "description": "Read information about the residues within the context of each chain",
        },
        {
            "label": "Centroid",
            "name": "Centroid",
            "description": "Calculate the centroid point for the selection for each group in the `Group ID`",
        },
        "break",
        {
            "label": "Bond Count",
            "name": "Bond Count",
            "description": "The number of bonds for an atom",
        },
        {
            "label": "Edge Info",
            "name": "Edge Info",
            "description": 'Get information for the selected edge, evaluated on the point domain. The "Edge Index" selects the edge from all possible connected edges. Edges are unfortunately stored somewhat randomly. The resulting information is between the evaluating point and the point that the edge is between. Point Index returns -1 if not connected.\n\nIn the video example, cones are instanced on each point where the Edge Index returns a valid connection. The Edge Vector can be used to align the instanced cone along that edge. The length of the edge can be used to scale the cone to the other point. As the "Edge Index" is changed, the selected edge changes. When "Edge Index" == 3, only the atoms with 4 connections are selected, which in this model (1BNA) are just the phosphates.',
            "video_url": "https://imgur.com/Ykyis3e",
        },
        {
            "label": "Edge Angle",
            "name": "Point Edge Angle",
            "description": ' Calculate the angle between two edges, selected with the edge indices. For molecule bonds, combinations of [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)] will select all possible bond angles.\n\nIn the video example, two edges are selected with their "Edge Index" values. Those atoms which aren\'t valid return false and do not get instanced. The two edge vectors are used to calculate the perpendicular vector through cross product, around which the rotation for the cone is rotated. This demonstrates the ability to calculate the edge angle between the two selected edges.',
            "video_url": "https://imgur.com/oQP6Cv8",
        },
        {
            "label": "Points of Edge",
            "name": "Points of Edge",
            "description": 'Finds the conntected point for the selected "Edge Index", and returns each point index for all of the points connected to that point. If the connection doesn\'t exist, or the connection is back to the original point, -1 is returned.\n\nIn the video example, a new point is selected based on the "Edge Index". At that point, all of the connecting points are exposed as indices `0, 1, 2, 3`. If that index is not a valid point or connection, or the point is the same as the original point that is being evaluated, then -1 is returned. \n\nThis is one of the more complicated topology nodes, but allows indexing of the atoms that are bonded to a bonded atom. This helps with doing calculations for planar molecules.',
            "video_url": "https://imgur.com/fZ6srIS",
        },
        "break",
        {
            "label": "Point Group Mask",
            "name": "Point Group Mask",
            "description": "Returns the index for the atom for each unique group (from res_id) for each point in that group. Allows for example, all atoms in a group to be rotated around the position of the selected atom.\n\nIn the video example, the `atom_name` is used to select an atom within the groups. Each atom's position is then offset to that position, showing the group-wise selection.",
            "video_url": "https://imgur.com/sD3jRTR",
        },
        {
            "label": "Backbone Positions",
            "name": "Backbone Positions",
            "description": 'If the atoms have been through the "Compute Backbone" node, then the backbone atom positions will be available as attributes through this node.\n\nIn the video example, the `Alpha Carbons` output is styled as spheres, where the position is mixed with some of the backbone posiitons. The backbone positions can also be selected from the AA residue higher or lower with the specified offset.',
            "video_url": "https://imgur.com/6X2wnpY",
        },
        "break",
        {
            "label": "3 Point Angle",
            "name": "3 Point Angle",
            "description": "Calculate the angle between 3 different points. These points are selected based on their index in the point domain, with Index B being the centre of the calculation.\n\nIn the video example, the same calculation that is occurring internally inside of the `MN_topo_edge_angle` node, is being handled explicity by this node. If the `Index` is being used as `Index B` then the current point that is being evaluated is the centre of the angle calculation. If this value is changed, then the point at the corresponding index is used, which results in a smaller angle in the example video.",
            "video_url": "https://imgur.com/qXyy2ln",
        },
        {
            "label": "2 Point Angle",
            "name": "2 Point Angle",
            "description": "Calculate the angle that two points make, relative to the current point being evaluated. Points are selected based on their index, with the centre of the angle calculation being the current point's position. Equivalent to using 3-Point angle and using `Index` as the `Index B`.\n\nIn the example video, the angle calculation is similar to that of the 3-Point Angle node, but the middle point is always the current point.",
            "video_url": "https://imgur.com/xp7Vbaj",
        },
        {
            "label": "Point Distance",
            "name": "Point Distance",
            "description": "Calculate the distance and the vector between the evaluating point and the point selected via the Index.\n\nIn the example video, each point is calculating a vector and a distance between itself and the indexed point. When the Point Mask node is used, this index is then on a per-group basis, so each point in the group points to just the group's corresponding point.",
            "video_url": "https://imgur.com/AykNvDz",
        },
    ],
    "assembly": [
        {
            "label": "Biological Assembly",
            "name": "mn.assembly_bio",
            "backup": "MN_assembly_",
            "description": "Creates a biological assembly by applying rotation and translation matrices to individual chains in the structure. It is created on an individual molecule basis, if assembly instructions are detected when imported.\n\n::: callout-caution \n\nStyle Spheres requires the material to be set again after the assembly node, as the material is currently lost when joining multiple point clouds.\n\n:::",
            "video_url": "https://imgur.com/TNc102v",
        },
        {
            "label": "Center Assembly",
            "name": "MN_assembly_center",
            "description": "Move an instanced assembly to the world origin. Some structures are not centred on the world origin, so this node can reset them to the world origin for convenient rotation and translation and animation.",
            "video_url": "https://imgur.com/pgFTmgC",
        },
    ],
    "DNA": [
        {
            "label": "Double Helix",
            "name": "MN_dna_double_helix",
            "description": "Create a DNA double helix from an input curve.\nTakes an input curve and instances for the bases, returns instances of the bases in a double helix formation",
        },
        {
            "label": "Bases",
            "name": "MN_dna_bases",
            "description": "Provide the DNA bases as instances to be styled and passed onto the Double Helix node",
        },
        "break",
        {
            "label": "Style Spheres Cycles",
            "name": "MN_dna_style_spheres_cycles",
            "description": "Style the DNA bases with spheres only visible in Cycles",
        },
        {
            "label": "Style Spheres EEVEE",
            "name": "MN_dna_style_spheres_eevee",
            "description": "Style the DNA bases with spheres visible in Cycles and EEVEE",
        },
        {
            "label": "Style Surface",
            "name": "MN_dna_style_surface",
            "description": "Style the DNA bases with surface representation",
        },
        {
            "label": "Style Ball and Stick",
            "name": "MN_dna_style_ball_and_stick",
            "description": "Style the DNA bases with ball and stick representation",
        },
    ],
    "animate": [
        {
            "label": "Animate Frames",
            "name": "Animate Frames",
            "description": "Animate the atoms of a structure, based on the frames of a trajectory from the `Frames` collection in the input. The structure animates through the trajectory from the given start frame to the given end frame, as the `Animate 0..1` value moves from `0` to `1`. Values higher than `1` start at the beginning again and the trajectory will loop repeating every `1.00`.\nPosition and `b_factor` are interpolated if available. By default linear interpolation is used. Smoothing in and out of each frame can be applied with the `Smoother Step`, or no interpolation at all.",
            "video_url": "https://imgur.com/m3BPUxh",
        },
        {
            "label": "Animate Value",
            "name": "Animate Value",
            "description": "Animate a float value between the specified min and max values, over specified range of frames. If clamped, frames above and below the start and end will result in the min and max output values, otherwise it will continue to linearly interpolate the value beyond the min and max values.",
            "video_url": "https://imgur.com/2oOnwRm",
        },
        "break",
        {
            "label": "Animate Trails",
            "name": "Animate Trails",
            "description": "Add trails to the atoms as they are animated, which trail the specified number of frames behind the atoms",
        },
        "break",
        {
            "label": "Centre on Selection",
            "name": "Centre on Selection",
            "description": "Move the input points to be centred on their calculated cnetroid point, which is based on the selection. The optional `Group ID` value applies this transformation on a per-group basis",
        },
        {
            "label": "Res Wiggle",
            "name": "Animate Wiggle",
            "description": "Create a procedural animation of side-chain movement. 'Wiggles' the side-chains of peptide amino acids based on the `b_factor` attribute. Wiggle is currently only supported for protein side-chains and does not check for steric clashing so higher amplitudes will result in strange results. The animation should seamlessly loop every `1.00` of the `Animate 0..1` input.",
            "video_url": "https://imgur.com/GK1nyUz",
        },
        {
            "label": "Peptide to Curve",
            "name": "Animate Peptide to Curve",
            "description": "Take the protein residues from a structure and align then along an input curve. Editing the curve will change how the atoms are arranged. The output atoms can be styled as normal.",
            "video_url": "https://imgur.com/FcEXSZx",
        },
        "break",
        {
            "label": "Noise Position",
            "name": "MN_animate_noise_position",
            "description": "Create 3D noise vector based on the position of points in 3D space. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node.",
            "video_url": "https://imgur.com/B8frW1C",
        },
        {
            "label": "Noise Field",
            "name": "MN_animate_noise_field",
            "description": "Create a 3D noise vector based on the input field. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node. Different field inputs result in different noise being applied. Using the `chain_id` results in the same noise being generated for each atom in each chain, but different between chains.",
            "video_url": "https://imgur.com/hqemVQy",
        },
        {
            "label": "Noise Repeat",
            "name": "MN_animate_noise_repeat",
            "description": "Create a 3D noise vector based on the input field, that repeats every `1.00` for the `Animate 0..1` input. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node. Different field inputs result in different noise being applied. Using the `chain_id` results in the same noise being generated for each atom in each chain, but different between chains.",
            "video_url": "https://imgur.com/GNQcIlx",
        },
    ],
    "utils": [
        {
            "label": "Curve Resample",
            "name": "MN_utils_curve_resample",
            "description": "",
        },
        {
            "label": "Attribute Map",
            "name": "Attribute Map",
            "description": "Sample an attribute from the mesh and remap from the minimum to the maximum to the specified values",
        },
        {
            "label": "Between Integer",
            "name": "Between Integer",
            "description": "Test if an integer is between (and including) the upper and lower bounds",
        },
        {
            "label": "Between Float",
            "name": "Between Float",
            "description": "Test if a float is between the upper and lower bounds",
        },
        {
            "label": "Between Vector",
            "name": "Between Vector",
            "description": "Test if a vector is element-wise between the upper and lower bounds.",
        },
        {
            "label": "Offset Integer",
            "name": "Offset Integer",
            "description": "Evaluate an integer by an index that is offset by the specified amount",
        },
        {
            "label": "Offset Vector",
            "name": "Offset Vector",
            "description": "Evaluate a vector by an index that is offset by the specified amount",
        },
        {
            "label": "Offset Boolean",
            "name": "Offset Boolean",
            "description": "Evaluate a boolean by an index that is offset by the specified amount",
        },
        {
            "label": "Group Info",
            "name": "Group Info",
            "description": "Based on the Group ID input, return the size of the group and the indices of the first and last items of the group",
        },
        {
            "label": "Vector Angle",
            "name": "MN_utils_vector_angle",
            "description": "Compute the angle in radians between two vectors.",
        },
        {
            "label": "Vector Axis Angle",
            "name": "MN_utils_vector_angle_axis",
            "description": 'Computes the angle between two vectors, AB & CD around around the axis of BC. The first vector AB is treated as the "12 O\'clock" up position, looking down the axis towards C, with angles being return in the range of (-Pi, Pi). Clockwise angles are positive and anti-clockwise angles are negative.',
            "video_url": "",
        },
        {
            "label": "Cartoon Utilities",
            "name": ".MN_utils_style_cartoon",
            "description": "The underlying node group which powers the cartoon style",
        },
        {
            "label": "Spheres Cycles",
            "name": ".MN_utils_style_spheres_cycles",
            "description": "A sphere atom representation, visible ONLY in Cycles. Based on point-cloud rendering",
        },
        {
            "label": "Spheres EEVEE",
            "name": ".MN_utils_style_spheres_eevee",
            "description": "A sphere atom representation, visible in EEVEE and Cycles. Based on mesh instancing which slows down viewport performance",
        },
    ],
    "cellpack": [
        {"label": "Pack Instances", "name": "Ensemble Instance", "description": ""}
    ],
    "density": [
        {
            "label": "Style Surface",
            "name": "Style Density Surface",
            "description": "A surface made from the electron density given a certain threshold value.",
            "video_url": "https://imgur.com/jGgMSd4",
        },
        {
            "label": "Style Wire",
            "name": "Style Density Wire",
            "description": "A wire surface made from the electron density given a certain threshold value.",
            "video_url": "https://imgur.com/jGgMSd4",
        },
        {
            "label": "Sample Nearest Attribute",
            "name": "Sample Nearest Atoms",
            "description": "Sample the nearest atoms from another object, to get the colors or other attributes and apply them to a volume mesh.",
            "video_url": "https://imgur.com/UzNwLv2",
        },
    ],
}

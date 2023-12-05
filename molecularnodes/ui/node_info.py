from .func import (
    button_custom_color, 
    button_custom_selection
)

menu_items = {
    'style': [
        {
            'label': 'Presets',
            'name': 'MN_style_presets',
            "description" : "Quickly switch between several different pre-made preset styles. Limited user facing settings. For more complex styles, combine other styles and tweak their settings.", 
            "extra_info": "In the example video below, we switch between several pre-made preset styles. These are combinations of the base style nodes. If you use <kbd>Tab</kbd> to go inside the node groups(<kbd>Ctrl</kbd> + <kbd>Tab</kbd> to go out of the node group), you can see the different presets, and inside those presets you can see the different nodes that are combined to create the preset styles.",
            "video_url" : "https://imgur.com/9sJIB5H"
        },
        {
            'label': 'Spheres',
            'name': 'MN_style_spheres',
            "description": "Create a sphere scaled based on its `vdw_radii` attribute for each atom. To make the atoms visible in EEVEE, enable the `EEVEE` input. EEVEE spheres will negatively impact performance on larger structures.",
            'extra_info': 'The EEVEE atoms are instances of an icosahderon. You can control how many subdivisions those instances have, and if they have smooth shading applied. Both of those settings don\'t affect the Cycles point-cloud atoms.',
            "video_url": "https://imgur.com/GTcT7bT"
        },
        {
            'label': 'Cartoon',
            'name': 'MN_style_cartoon',
            "description": 'Creates cartoon representation of peptide chains, with arrows, alpha helices and other common cartoon elements.',
            'extra_info': 'The cartoon style is currently only applied to peptide chains which already have `sec_struct` attributes calculated and applied. This is currently only available when imported from the PDB or the loading of some local files.',
            "video_url": "https://imgur.com/q9ZnhUn"
        },
        {
            'label': 'Ribbon',
            'name': 'MN_style_ribbon',
            "description": "Style that creates a continuous solid ribbon or licorice tube through the backbones of peptides and nucleic acids.",
            "video_url": "https://imgur.com/pGhwyYb"
        },
        {
            'label': 'Surface',
            'name': 'MN_style_surface',
            "description": "Create a gassuian surface, based on the `vdw_radii` of the atoms and an adjustable probe size.",
            'extra_info': 'You can change whether to create separate surfaces, and what attribute to separate those surfaces by (defualt: `chain_id`). Coloring is done by the closest alpha carbon. Disable this to sample the nearest atom. The `Blur` changes how much those neary colors are mixed before being applied to the surface.',
            "video_url": "https://imgur.com/4boXWpl"
        },
        {
            'label': 'Ball and Stick',
            'name': 'MN_style_ball_and_stick',
            "description": "Create a sphere for each atom and a cylinder for each bond. Double bonds not currently supported.",
            'extra_info': 'Number of subdividisions can be controlled for both the sphere (EEVEE only) and the bond. Increased number will yield a smoother result at the cost of lower performance.',
            "video_url": "https://imgur.com/SkfsILI"
        },
        {
            'label': 'Stick',
            'name': 'MN_style_stick',
            "description": "Cylinders with cylindrical ends for each bond. Similar to Ball and Stick but atom is scaled to match the bond.",
            "video_url": "https://imgur.com/JNH5P7f"
        }
    ],
    'select': [
        {
            'label': 'Separate Atoms',
            'name': 'MN_select_separate_atoms',
            'description': "Select only the desired input atoms. The output is bits of geometry, which include the selection and include the inverse of the selected atoms. You can expand the selection to include an entire residue if a single atom in that residue is selected, by setting `Whole Residue` to `True`.", 
            'video_url': "https://imgur.com/VsCW0HY"
        },
        {
            'label': 'Separate Polymers',
            'name': 'MN_select_separate_polymers',
            'description': "Separate the input atomic geometry into it's different polymers or `Protein`, `Nucleic Acid` and `other`.", 
            'video_url': 'https://imgur.com/ICQZxxz'
        },
        "break",
        {
            'label': 'custom',
            'function': button_custom_selection,
            'values': [
                {
                    'label': 'Chain', 
                    'field': 'chain_id', 
                    'name': 'MN_select_chain_',
                    'prefix': 'Chain ', 
                    'property_id': 'chain_id_unique', 
                    "description": "Select single or multiple of the different chains. Creates a selection based on the `chain_id` attribute.",
                    "video_url": "https://imgur.com/P9ZVT2Z"
                    },
                {
                    'label': 'Entity', 
                    'field': 'entity_id', 
                    'name': 'MN_select_entity_',
                    'prefix': '', 
                    'property_id': 'entity_names', 
                    "description": "Select single or multiple of the different entities. Creates a selection based on the `entity_id` attribute.",
                    "video_url": "https://imgur.com/fKQIfGZ"
                    },
                {
                    'label': 'Ligand', 
                    'field': 'res_name', 
                    'name': 'MN_select_ligand_',
                    'prefix': '', 
                    'property_id': 'ligands', 
                    "description": "Select single or multiple of the different ligands.",
                    "video_url": "https://imgur.com/s2seWIw"
                    }
            ]
        },
        "break",
        {
            'label': 'Cube',
            'name': 'MN_select_cube',
            "description": "Create a selection that is inside the `Empty_Cube` object. When this node is first created, an _empty_ object called `Empty_Cube` should be created. You can always create additional empty objects through the add menu, to use a different object. The rotation and scale of the object will be taken into account for the selection.",
            "video_url": "https://imgur.com/P4GZ7vq"
        },
        {
            'label': 'Sphere',
            'name': 'MN_select_sphere',
            "description": "Create a selection that is within a spherical radius of an object, based on that object's scale. By default an _empty_ object called `Empty_Sphere` is created. You can use other objects or create a new empty to use. The origin point for the object will be used, which should be taken in to account when using molecules. Use [`MN_select_proximity`](#select-proximity) for selections which are within a certain distance of a selection of atoms instead of a single origin point.",
            "video_url": "https://imgur.com/xdeTZR7"
        },
        "break",
        {
            'label': 'Secondary Structure',
            'name': 'MN_select_sec_struct',
            "description": "Select based on the assigned secondary structure information. Only returns a selection if the `sec_struct` attribute exists on the atoms. Will be imported from files where it is present", #or can be calculated using the [`MN_utils_dssp'](#utils-dssp) node.",
            "video_url": "https://imgur.com/IindS3D"
        },
        {
            'label': 'Backbone',
            'name': 'MN_select_backbone',
            "description": "Selection fields for the backbone and side chains of the protein and nucleic acids.",
            "video_url": "https://imgur.com/Sbl6ns5"
        },
        {
            'label': 'Atomic Number',
            'name': 'MN_select_atomic_number',
            'description': "Select single elements, by matching to the `atomic_number` field. Useful for selecting single elements, or combining to select elements higher than 20 on the periodic table.",
            'video_url': "https://imgur.com/Bxn33YK"
        },
        {
            'label': 'Element',
            'name': 'MN_select_element',
            "description": "Select individual elements, for the first 20 elements on the periodic table. For selections of higher elements, use [`MN_select_atomic_number`](#select-atomic-number). Creating a node which includes more elements becomes too large to be practical.",
            "video_url": "https://imgur.com/nRQwamG"
        },
        {
            'label': 'Attribute',
            'name': 'MN_select_attribute',
            "description": "Selections based on the different attributes that are available on the atomic geometry.",
            "video_url": "https://imgur.com/HakZ4sx"
        },
        {
            'label': 'Bonded Atoms',
            'name': 'MN_select_bonded',
            "description": "Based on an initial selection, finds atoms which are within a certain number of bonds of this selection. Output can include or excluded the original selection.",
            "video_url": "https://imgur.com/g8hgXup"
        },
        "break",
        {
            'label': 'Res ID', 
            'name': 'mn.residues_selection_custom', 
            'backup': 'MN_select_res_id_',
            "description": "Create a more complex selection for the `res_id` field, by specifying multiple ranges and potential single `res_id` numbers. This node is built uniquely each time, to the inputs will look different for each user.\nIn the example below, residues 10 & 15 are selected, as well as residues between and including 20-100.\nThe node was created by inputting `10, 15, 20-100` into the node creation field.",
            "video_url": "https://imgur.com/OwAXsbG"
        }, 
        {
            'label': 'Proximity', 
            'name': 'MN_select_proximity', 
            "description": "Create a selection based on the proximity to the Target Atoms of the input. A sub-selection of the Target atoms can be used if the `Selection` input is used. You can expand the selection to include an entire residue if a single atom in that residue is selected, by setting `Whole Residue` to `True`.\nIn the example below, the `MN_style_atoms` is being applied to a selection, which is being calculated from the proximity of atoms to specific chains. As the cutoff for the selection is changed, it includes or excludes more atoms. The `Whole Residue` option also ensures that entire residues are shown.",
            "video_url": "https://imgur.com/RI80CRY"
        }, 
        {
            'label': 'Res ID Single', 
            'name': 'MN_select_res_id_single', 
            "description": "Select a single residue based on the `res_id` number.",
            "video_url": "https://imgur.com/BL6AOP4"
        },
        {
            'label': 'Res ID Range', 
            'name': 'MN_select_res_id_range', 
            "description": "Select multiple residues by specifying a _minimum_ and a _maximum_ which will create the selection based on the `res_id` number.",
            "video_url": "https://imgur.com/NdoQcdE"
        },
        {
            'label': 'Res Name Peptide', 
            'name': 'MN_select_res_name_peptide', 
            "description": "Select single or multiple protein residues by name. Includes the 20 naturally occurring amino acids.",
            "video_url": "https://imgur.com/kjzH9Rs"
        },
        {
            'label': 'Res Name Nucleic', 
            'name': 'MN_select_res_name_nucleic', 
            "description": "Select single or multiple nucleic residues by name.",
            "video_url": "https://imgur.com/qnUlHpG"
        }, 
        {
            'label': 'Res Whole',
            'name': 'MN_select_res_whole',
            "description": "Expand the given selection to include a whole residue, if a single atom in that residue is selected. Useful for when a distance or proximity selection includes some of the residue and you wish to include all of the residue.",
            "video_url": "https://imgur.com/JFzwE0i"
        },
    ],
    'color': [
        {
            'label': 'Set Color',
            'name': 'MN_color_set',
            "description": "The is the primary way to change the color of structures in Molecular Nodes. Colors for cartoon and ribbon are taken from the _alpha-carbons_ of the structures. Change the color of the input atoms, based on a selection and a color field. The color field can be as complex of a calculation as you wish. In the example below the color for the whole structure can be set, or the color can be based on a color for each chain, or the result of mapping a color to an attribute such as `b_factor`.",
            "video_url": "https://imgur.com/667jf0O"
        },
        "break",
        {
            'label': 'custom',
            'function': button_custom_color,
            'values': [
                {
                    'label': 'Chain', 
                    'field': 'chain_id', 
                    'name': 'MN_select_chain_',
                    'prefix': 'Chain', 
                    'property_id': 'chain_id_unique', 
                    "description": "Choose the colors for individual chains in the structure. This node is generated for each particular molecule, so the inputs will look different based on the imported structure. For larger structures with many chains this node may become too large to be practical, in which case you might better use [`MN_color_entity_id`](#color-entity-id).",
                    "video_url": "https://imgur.com/9oM24vB"
                    },
                {
                    'label': 'Entity', 
                    'field': 'entity_id', 
                    'name': 'MN_color_entity_',
                    'prefix': '', 
                    'property_id': 'entity_names', 
                    "description": "Choose the colors for individual entities in the structure. Multiple chains may be classified as the same entity, if they are copies of the same chain but in different conformations or positions and rotations. The nodes is generated for each individual structure, if `entity_id` is available.",
                    "video_url": "https://imgur.com/kEvj5Jk"
                    },
                {
                    'label': 'Ligand', 
                    'field': 'res_name', 
                    'name': 'MN_color_ligand_',
                    'prefix': '', 
                    'property_id': 'ligands', 
                    "description": "Choose the colors for individual ligands in the structure.",
                    "video_url": "https://imgur.com/bQh8Fd9"
                    }
            ]
        },
        "break",
        {
            'label': 'Goodsell Colors',
            'name': 'MN_color_goodsell',
            "description": "Change the inputted color to be darker for non-carbon atoms. Creates a _Goodsell Style_ color scheme for individual chains.",
            "video_url": "https://imgur.com/gPgMSRa"
        },
        {
            'label': 'Attribute Map',
            'name': 'MN_color_attribute_map',
            "description": "Interpolate between two or three colors, based on the value of an attribute field such as `b_factor`. Choosing the minimum and maximum values with the inputs.",
            "video_url": "https://imgur.com/lc2o6e1"
        },
        {
            'label': 'Attribute Random',
            'name': 'MN_color_attribute_random',
            "description": "Generate a random color, based on the given attribute. Control the lightness and saturation of the color with the inputs.",
            "video_url": "https://imgur.com/5sMcpAu"
        },
        {
            'label': 'Backbone',
            'name': 'MN_color_backbone',
            'description': ""
        },
        {
            'label': 'Secondary Structure',
            'name': 'MN_color_sec_struct',
            "description": "Choose a color for the different secondary structures, based on the `sec_struct` attribute.",
            "video_url": "https://imgur.com/wcJAUp9"
        },
        "break",
        {
            'label': 'Element',
            'name': 'MN_color_element',
            "description": "Choose a color for each of the first 20 elements on the periodic table. For higher atomic number elements use [`MN_color_atomic_number`](#color-atomic-number).",
            "video_url": "https://imgur.com/iMGZKCx"
        },
        {
            'label': 'Atomic Number',
            'name': 'MN_color_atomic_number',
            "description": "Choose a color for an individual element. Select the element based on `atomic_number`. Useful for higher atomic number elements which are less commonly found in structures.",
            "video_url": "https://imgur.com/pAloaAF"
        },
        {
            'label': 'Res Name Peptide',
            'name': 'MN_color_res_name_peptide',
            "description": "Choose a color for each of the 20 naturally occurring amino acids. Non AA atoms will retain their currently set color.",
            "video_url": "https://imgur.com/1yhSVsW"
        },
        {
            'label': 'Res Name Nucleic',
            'name': 'MN_color_res_name_nucleic',
            "description": "Choose a color for each of the nucleic acids. Non nucleic acid atoms will retain their currently set color.",
            "video_url": "https://imgur.com/LpLZT3F"
        },

        {
            'label': 'Element Common',
            'name': 'MN_color_common',
            "description": "Choose a color for each of the common elements. This is a smaller convenience node for elements which commonly appear in macromolecular structures. Use [`MN_color_element`](#color-element) for the first 20 elements and [`MN_color_atomic_number`](#color-atomic-number) for individual elements with higher atomic numbers.",
            "video_url": "https://imgur.com/GhLdNwy"
        },
    ],
    'bonds': [
        {
            'label': 'Find Bonds',
            'name': '.MN_bonds_find',
            'description': "Finds bonds between atoms based on distance. Based on the vdw_radii for each point, finds other points within a certain radius to create a bond to. Does not preserve the index for the points. Does not detect bond type"
        },
        {
            'label': 'Break Bonds',
            'name': '.MN_bonds_break',
            'description': "Will delete a bond between atoms that already exists based on a distance cutoff"
        }
    ],

    'assembly': [
        {
            'label': 'Biological Assembly', 
            'name': 'mn.assembly_bio', 
            'backup': 'MN_assembly_',
            "description": "Creates a biological assembly by applying rotation and translation matrices to individual chains in the structure. It is created on an individual molecule basis, if assembly instructions are detected when imported.",
            "video_url": "https://imgur.com/6jyAP1z"
        }, 
        {
            'label': 'Center Assembly', 
            'name': 'MN_assembly_center', 
            "description": "Move an instanced assembly to the world origin. Some structures are not centred on the world origin, so this node can reset them to the world origin for convenient rotation and translation and animation.",
            "video_url": "https://imgur.com/pgFTmgC"
        }
    ],


    'dna' : [
        {
            'label': 'Double Helix',
            'name': 'MN_dna_double_helix',
            'description': "Create a DNA double helix from an input curve.\nTakes an input curve and instances for the bases, returns instances of the bases in a double helix formation"
        },
        {
            'label': 'Bases',
            'name': 'MN_dna_bases',
            'description': "Provide the DNA bases as instances to be styled and passed onto the Double Helix node"
        },
        "break",
        {
            'label': 'Style Spheres Cycles',
            'name': 'MN_dna_style_spheres_cycles',
            'description': "Style the DNA bases with spheres only visible in Cycles"
        },
        {
            'label': 'Style Spheres EEVEE',
            'name': 'MN_dna_style_spheres_eevee',
            'description': "Style the DNA bases with spheres visible in Cycles and EEVEE"
        },
        {
            'label': 'Style Surface',
            'name': 'MN_dna_style_surface',
            'description': "Style the DNA bases with surface representation"
        },
        {
            'label': 'Style Ball and Stick',
            'name': 'MN_dna_style_ball_and_stick',
            'description': "Style the DNA bases with ball and stick representation"
        }
    ],

    'animate' : [
        {
            'label': 'Animate Frames',
            'name': 'MN_animate_frames',
            "description": "Animate the atoms of a structure, based on the frames of a trajectory from the `Frames` collection in the input. The structure animates through the trajectory from the given start frame to the given end frame, as the `Animate 0..1` value moves from `0` to `1`. Values higher than `1` start at the beginning again and the trajectory will loop repeating every `1.00`.\nPosition and `b_factor` are interpolated if available. By default linear interpolation is used. Smoothing in and out of each frame can be applied with the `Smoother Step`, or no interpolation at all.",
            "video_url": "https://imgur.com/m3BPUxh"
        },
        {
            'label': 'Animate Value',
            'name': 'MN_animate_value',
            "description": "Animate a float value between the specified min and max values, over specified range of frames. If clamped, frames above and below the start and end will result in the min and max output values, otherwise it will continue to linearly interpolate the value beyond the min and max values.",
            "video_url": "https://imgur.com/2oOnwRm"
        },
        "break",
        {
            'label': 'Res Wiggle',
            'name': 'MN_animate_res_wiggle',
            "description": "Create a procedural animation of side-chain movement. 'Wiggles' the side-chains of peptide amino acids based on the `b_factor` attribute. Wiggle is currently only supported for protein side-chains and does not check for steric clashing so higher amplitudes will result in strange results. The animation should seamlessly loop every `1.00` of the `Animate 0..1` input.",
            "video_url": "https://imgur.com/GK1nyUz"
        },
        {
            'label': 'Res to Curve',
            'name': 'MN_animate_res_to_curve',
            "description": "Take the protein residues from a structure and align then along an input curve. Editing the curve will change how the atoms are arranged. The output atoms can be styled as normal.",
            "video_url": "https://imgur.com/FcEXSZx"
        },
        "break",
        {
            'label': 'Noise Position',
            'name': 'MN_animate_noise_position',
            "description": "Create 3D noise vector based on the position of points in 3D space. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node.",
            "video_url": "https://imgur.com/B8frW1C"
        },
        {
            'label': 'Noise Field',
            'name': 'MN_animate_noise_field',
            "description": "Create a 3D noise vector based on the input field. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node. Different field inputs result in different noise being applied. Using the `chain_id` results in the same noise being generated for each atom in each chain, but different between chains.",
            "video_url": "https://imgur.com/hqemVQy"
        },
        {
            'label': 'Noise Repeat',
            'name': 'MN_animate_noise_repeat',
            "description": "Create a 3D noise vector based on the input field, that repeats every `1.00` for the `Animate 0..1` input. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node. Different field inputs result in different noise being applied. Using the `chain_id` results in the same noise being generated for each atom in each chain, but different between chains.",
            "video_url": "https://imgur.com/GNQcIlx"
        }
    ],

    'utils' : [
        {
            'label': 'Curve Resample', 
            'name': 'MN_utils_curve_resample', 
            'description': ''
            },
        # {
        #     'label': 'Determine Secondary Structure', 
        #     'name': 'MN_utils_dssp', 
        #     'description': ''
        #     },
        {
            'label': 'Cartoon Utilities', 
            'name': '.MN_utils_style_cartoon', 
            'description': 'The underlying node group which powers the cartoon style'
            },
        {
            'label': 'Spheres Cycles', 
            'name': '.MN_utils_style_spheres_cycles', 
            'description': 'A sphere atom representation, visible ONLY in Cycles. Based on point-cloud rendering'
            },
        {
            'label': 'Spheres EEVEE', 
            'name': '.MN_utils_style_spheres_eevee', 
            'description': 'A sphere atom representation, visible in EEVEE and Cycles. Based on mesh instancing which slows down viewport performance'
            }
    ],

    'cellpack' : [
        {
            'label' : 'Pack Instances',
            'name'  : 'MN_pack_instances', 
            'description': ''
        }
    ],

    'density' : [
            {
                'label': 'Style Surface',
                'name': 'MN_density_style_surface',
                "description": "A surface made from the electron density given a certain threshold value.",
                "video_url": "https://imgur.com/jGgMSd4"
            },
            {
                'label': 'Style Wire',
                'name': 'MN_density_style_wire',
                "description": "A wire surface made from the electron density given a certain threshold value.",
                "video_url": "https://imgur.com/jGgMSd4"
            },
            {
                'label': 'Sample Nearest Attribute',
                'name': 'MN_density_sample_nearest',
                "description": "Sample the nearest atoms from another object, to get the colors or other attributes and apply them to a volume mesh.",
                "video_url": "https://imgur.com/UzNwLv2"
            }
        ]
}
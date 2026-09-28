# """
# All prompts used for image captioning.
# """

# PROMPTS = {

#     "basic": """
# Describe this image.
# """,

#     "detailed": """
# Describe this image in detail.

# Include:
# - Main subject
# - Objects present
# - Colors
# - Background
# - Actions
# - Lighting
# - Environment

# Write at least 8 complete sentences.
# """,

#     "dense": """
# Generate a dense caption for this image.

# Mention every visible object,
# their colors,
# their positions,
# relationships,
# background,
# lighting,
# camera angle,
# and scene context.

# Write a highly descriptive paragraph.
# """,

#     "objects_only": """
# List every object visible in the image.

# For each object mention:
# - Name
# - Color
# - Approximate location
# - Size relative to the image
# """,

#     "scene_understanding": """
# Explain the complete scene.

# Describe:
# - What is happening
# - Who or what is present
# - The environment
# - Relationships between objects
# - Mood
# - Time of day if visible
# - Weather if visible

# Write detailed paragraphs.
# """,

#     "caption_dataset": """
# Generate a detailed caption suitable for an image captioning dataset.

# The caption should accurately describe:
# - Objects
# - Attributes
# - Colors
# - Actions
# - Background
# - Spatial relationships
# - Scene context

# Avoid assumptions.
# Only describe what is visible.
# """,


#     "very_detailed": """
# You are an expert computer vision and image annotation assistant.

# Your task is to produce a comprehensive and highly detailed caption of the given image.

# Only describe information that is directly visible in the image.
# Do not make assumptions or infer facts that cannot be seen.

# Your caption should include:

# 1. Main subject(s)
# 2. Every visible object
# 3. Physical appearance of each object
# 4. Colors, textures, patterns, and materials
# 5. Approximate size of objects
# 6. Relative positions of objects
# 7. Foreground
# 8. Midground
# 9. Background
# 10. Lighting conditions
# 11. Shadows and reflections
# 12. Camera angle and viewpoint
# 13. Environment (indoor/outdoor)
# 14. Actions being performed
# 15. Facial expressions or emotions if clearly visible
# 16. Relationships between objects
# 17. Fine visual details that might be useful for image understanding.

# Write one detailed paragraph of at least 250 words.
# Do not summarize.
# Do not use bullet points.
# """,

# }




PROMPTS ={ 
    "1":"""

Provide a comprehensive and objective description of this image.

Include every visible detail without making assumptions. Describe:

1. Main subject(s)
2. Animal breed/species (if identifiable)
3. Fur/coat color, markings, patterns, texture, and eye color
4. Body posture, pose, facial expression, and gaze direction
5. Size and physical characteristics
6. Clothing, collars, tags, accessories, or other worn items
7. Objects surrounding the subject
8. Background elements
9. Indoor or outdoor setting
10. Lighting conditions
11. Colors present throughout the image
12. Camera angle and framing
13. Relative positions of all visible objects
14. Any readable text
15. Activities or interactions occurring
16. Overall scene context

Do not omit small details. If something cannot be determined with confidence, explicitly state that it is not clearly visible instead of guessing..
 PROVIDE IT IN PARAGRAPGH.
  """,
    "2":"""
 Generate an extremely detailed dense caption for this image.

 Describe every visible object, attribute, color, texture, material, size, position, orientation, and relationship between objects.

 For animals include:
 - probable breed
 - coat type
 - fur pattern
 - fur length
 - eye color
 - nose color
 - ear shape
 - tail appearance
 - whiskers
 - paw color
 - approximate age (only if visually evident)

 For the environment include:
 - floor or ground
 - walls
 - furniture
 - vegetation
 - sky
 - weather
 - lighting
 - shadows
 - reflections
 - depth of field
 - background blur

 Avoid subjective opinions. Mention uncertainty whenever identification is not possible.
 """,

#  "3":"""
# Act as an expert computer vision annotator creating a dataset-quality image caption.

# Describe the image in exhaustive detail.

# Include:

# • Subject identification
# • Breed/species if visually recognizable
# • Physical appearance
# • Coat colors and markings
# • Texture
# • Visible anatomy
# • Pose
# • Orientation
# • Facial expression
# • Eye contact
# • Objects present
# • Relative spatial locations
# • Background
# • Scene type
# • Lighting
# • Camera perspective
# • Colors
# • Materials
# • Activities
# • Interactions
# • Occlusions
# • Image quality
# • Focus
# • Any unusual or distinctive features

# Use precise and objective language.

# Never invent information. If uncertain, state "cannot be determined from the image."

# """,

#  "4":"""

#  Describe this image with maximum possible detail.

#  Inspect the image carefully from foreground to background and mention every visible detail.

#  For every animal identify, if possible:
#  - breed
#  - species
#  - coat pattern
#  - fur texture
#  - dominant and secondary colors
#  - eye color
#  - nose
#  - ears
#  - whiskers
#  - tail
#  - paws
#  - body build
#  - approximate age category
#  - emotional appearance

#  For every object describe:
#  - color
#  - material
#  - shape
#  - size
#  - location
#  - relationship to nearby objects

#  Also describe:
#  - background
#  - lighting
#  - weather
#  - shadows
#  - reflections
#  - perspective
#  - camera angle
#  - image composition
#  - depth of field

#  Only describe what is directly visible.


#  """,

#  "5":"""
#  Write a highly dense, descriptive caption designed to visually reverse-engineer this image. Focus heavily on sensory data: specify exact color palettes (e.g., 'crimson red', 'matte black'), types of lighting (e.g., 'harsh top-down sunlight', 'soft cinematic neon glow'), textures ('brushed metal', 'coarse fabric'), and the specific camera perspective ('low-angle shot', 'macro macro-lens close-up'). Avoid vague adjectives like 'beautiful' or 'interesting'—use purely descriptive, concrete terms.

#  """,


 "6":"""

 Analyze the image and break down your caption into a highly detailed paragraph covering the following specific attributes:

     Subject/Breed: Exact identification and specific strain/variant.

     Color & Markings: All visible hues, shading, and patterns.

     Size & Scale: Physical proportions and spatial relation to the environment.

     Texture & Material: Fine details (e.g., coarse fur, glossy finish, matte texture).

     Environment: Complete description of the setting, foreground, and background.
     Combine these into a seamless, hyper-detailed master caption


 """,


 "7":"""
 Examine this image with forensic level detail. Write a comprehensive caption that documents everything visible. Identify the specific breed/type of the subject, its precise color palette (down to the undercoat or secondary shades), its size relative to its environment, the exact expression or state, and the condition of the surroundings. Mention every single object, color, and texture present in the frame, leaving absolutely nothing out.


 """,



# "8":"""
# Analyze this image and write an exhaustive, highly detailed caption. Do not summarize. Include the exact breed or species, precise color gradients, size and scale relative to surroundings, textures, lighting conditions, background elements, and the positioning of every object. Describe it so vividly that someone who is blind could perfectly visualize every single asset, color nuance, and structural detail in the image

# """,



#  "9":"""
#  Provide a comprehensive, granular description of the main subject in this image for inventory and cataloging purposes. State its exact breed/type, primary and secondary colors (including patterns like brindling, spots, or gradients), estimated dimensions or size category, material or fur texture, and its exact posture/orientation. Also, list all background objects and their colors to ensure no detail is missed
#  """,




# "10":"""
#  Act as an expert prompt engineer. Write a highly descriptive, dense caption of this image that could be used to recreate it perfectly using a text-to-image AI. You must include: the precise breed/model, specific color hex-types (e.g., cream, charcoal, golden), the scale and size proportions, the texture of the surfaces, the camera angle, the lighting setup, and every minor background element. Avoid vague words like 'beautiful' or 'nice'—stick strictly to objective, measurable visual facts.

#  """,


#  "11":"""

#  Provide a forensic visual analysis of the image. Your caption must combine a description of the subject with the technical execution of the photo. Detail the subject (the tricolor puppy, its four-legged stance, its downward rightward gaze, and the markings on its face), the textures present (scruffy fur, sandy grains, rough dirt, smooth weeds), the lighting (natural overhead daylight casting soft shadows), and the camera settings (vertical aspect ratio, shallow depth of field, sharp foreground focus with a heavily blurred background).


#  """,




#  "12":"""
#  Act as an expert visual analyst. Meticulously scan the provided image and generate an exhaustive, highly granular description detailing every visible element. You must explicitly cover:

#      The subject’s exact lifecycle stage (puppy vs. adult) and physical stance (confirm how many legs are touching the ground).

#      The exact mapping of the coat colors (white, black, tan/brown), where they meet, and the nature of the markings.

#      Micro-details on the puppy, including the texture of its coat, its whiskers, its folded ears, and the specific specks of sand/dirt clinging to its forehead.

#      The exact composition of the ground terrain (sand, twigs, specific plant leaves) and tiny artifacts like the blue synthetic fibers near its paw.

#      The lighting, vertical framing, and the ambiguous, blurry white object in the top-left background.
#      Write this as a seamless, deeply detailed narrative. Do not assume or hallucinate; stick strictly to the visible pixels.

#  """,



# "13":"""

# Extract every visual detail from this image and organize it into the following strict, structured categories. Provide maximum detail for each section and do not use generic template responses:

#     Subject Typology: [Probable breed mix indicators, estimated age in weeks/months, physical maturity]

#     Anatomy & Posture: [Exact stance, leg placement, head tilt, eye gaze direction, ear structure]

#     Colorway & Patterning: [Zonal breakdown of white, black, and brown fur; description of facial mask]

#     Micro-Textures & Debris: [Fur texture, presence of sand/dirt particles on the body, whisker visibility]

#     Foreground Terrain: [Exact ground material, vegetation types, small debris, and artificial items/strings]

#     Background & Technical Data: [Depth of field, focus level, lighting quality, identification of out-of-focus background shapes]

# """,



#  "14":"""

#  Write a comprehensive, multi-paragraph caption for this image intended for master-level accessibility alt-text. The description must be so detailed that a visually impaired person can reconstruct the exact scene in their mind. Start with a foundational overview, then detail the puppy from its nose to its paws (including color boundaries, the sand on its fur, its curious expression, and ear shape). Finally, detail the environment completely—mapping out the sandy ground, the creeping green weeds, the scattered twigs, the blue plastic strands, and the bokeh effect on the background elements.

#  """,



#  "15":"""

#  You are going to write an ultra-detailed caption of this image, but first, you must perform a self-correction pass to eliminate common AI hallucinations.

# Step 1: Look closely at the image. Mentally draft a description of the puppy's pose, the ground, and the background.
# Step 2: Explicitly verify: Is the puppy standing on two legs or four? (Answer: Four). Is it on green grass or sandy dirt? (Answer: Sandy dirt with weeds). Are its ears pointing straight up or folded down? (Answer: Folded/floppy). What is actually on its head—is its fur "worn" or is it just covered in sand? (Answer: Tiny specks of sand).
# Step 3: Based on these verified facts, write a highly detailed, comprehensive caption that describes every single element in the frame (subject, colors, exact pose, background, debris, and lighting) with 100% accuracy.


# # """,


#  "16":"""
#  Act as an expert animal photographer and AI vision analyst. Analyze the provided image with extreme attention to detail. Output your response strictly in JSON format with the following keys:

#       primary_subject: What the main subject is.
#       breed_or_species: The specific breed (if animal) or type of object.
#       color_and_pattern: Exact colors, markings, gradients, or textures (e.g., 'brindle', 'solid black', 'merle').
#       size_and_proportions: Estimated size relative to the frame or surroundings (e.g., 'large, taking up 60% of the frame', 'small and compact').
#       posture_and_pose: Exact body positioning, weight distribution, and angle (e.g., 'frontal profile, sitting with weight shifted right, head slightly tilted').
#       facial_expression: Ear position, eye contact, mouth state.
#       environment_and_lighting: Brief description of the background and lighting conditions.
#       comprehensive_caption: A single, fluent paragraph combining all the above details seamlessly
#   """,

#  "17":"""

# Provide a highly detailed, multi-sentence caption for this image. You must explicitly address the following elements in your description. Do not skip any of them:

#     Identification & Breed: Identify the exact breed or species if visible.
#     Coloration: Describe the base color, secondary colors, and any specific patterns (spots, stripes, roaning, shading).
#     Size: Describe the physical mass and height of the subject (e.g., stocky, lean, petite, massive).
#     Posture & Anatomy: Describe the stance (standing, laying, crouching), the position of the legs, the arch of the back, and the angle of the head/neck.
#     Action/State: What is the subject currently doing?
#     Context: What is the immediate background?
#     Combine these into a cohesive, descriptive paragraph.
#  """,

  "18":"""

 Examine this image as a professional animal judge or biologist. Write a detailed caption that reads like a professional assessment. Include the specific breed, coat color and texture, physical conformation (size, bone structure, proportions), and precise posture (e.g., 'stacked', 'loose standing', 'play bow'). Describe the subject's gaze and ear set. Finally, summarize the overall scene in one continuous, richly descriptive paragraph
  """,
#  "19":"""
# Describe this image in vivid, evocative detail. Begin by identifying the subject and its specific breed. Paint a picture with words by describing the exact hues and patterns of its coat/surface. Describe its physical presence—is it imposing, delicate, or average in size? Detail its posture and the way it holds its body in space. Finally, describe how the subject interacts with its immediate environment. Ensure the final output is a single, highly detailed paragraph that leaves no visual element undescribed.
#  """,
#  "20":"""
# Look closely at the image. Provide a detailed caption that includes the subject's breed, exact coloration, and posture. Crucially, estimate the subject's size and weight class by comparing it to surrounding objects (e.g., furniture, doors, grass blades, human hands). Describe its physical build (e.g., long-legged, barrel-chested) and its current stance. Write the caption as a continuous, flowing paragraph.
#  """,
# "21":"""

# Generate a detailed caption in exactly 5 to 6 sentences.

# Describe:
# - the animal
# - breed if identifiable
# - fur color
# - posture
# - actions
# - environment
# - lighting
# - objects visible
# - overall atmosphere

# Only describe what is visible.
# Do not invent details.
#  """,

#  "22":"""
# Carefully analyze the image and generate a detailed caption. Include:

# Main subject (type, category, specific name if possible)
# Physical attributes (color, size, texture, patterns)
# Pose and actions
# Background and environment
# Lighting conditions
# Mood or atmosphere
# Provide a clear, natural paragraph.
#  """,

# "23":"""
# Describe the image like a professional visual analyst. Identify all visible objects, their relationships, spatial arrangement, colors, textures, and activities. Mention foreground, midground, and background separately. Provide a detailed yet coherent caption.
#  """,

# "24":"""

# Generate a detailed caption focusing on the primary object. Include its appearance, position, orientation, and interaction with surroundings. Then describe the environment and any secondary objects.
#  """,

# "25":"""
# Analyze the scene and describe what is happening. Include: who/what is present, what actions are occurring, where the scene is taking place, and any contextual clues that explain the situation.
#  """,


# "26":"""
# Provide a detailed caption for this image. Describe the main subject, objects, actions, colors, setting, lighting, and any notable details. Keep the description factual and avoid making assumptions.
# """,
# "27":""" 
# Generate a concise caption similar to the MS COCO dataset. Use a single sentence describing the most important content in the image.
# """,
 "28":"""
 Describe everything visible in the image. Include all objects, their locations, interactions, colors, sizes, and the overall scene. Mention the foreground, middle ground, and background.
 """,
#  "29":"""
#  Provide a comprehensive description of this image including:
#  - Main subject
#  - Secondary objects
#  - Actions
#  - Relative positions
#  - Colors
#  - Materials
#  - Lighting
#  - Weather (if visible)
#  - Environment
#  - Camera perspective
#  Do not infer information that is not visible.
#  """,
# "30":"""
# Generate a detailed image caption suitable for training an image captioning model. Include all visible objects, their attributes, relationships, activities, and the scene context. Be objective and avoid speculation.
# """,
# "31":"""
# Analyze the image and provide:

# Main Subject:
# Objects:
# Actions:
# Background:
# Colors:
# Lighting:
# Environment:
# Notable Details:

# Finally, write one complete descriptive caption.
# """,

# "32":"""
# Look at this image and write a description that acts as a blueprint for a kid to draw it. Use simple but incredibly descriptive words. Tell the child exactly where to place their pencil, what shapes to draw, and what colors to use.
# Example format: 'First, in the middle of the page, draw a large, round, sunny-yellow circle. Inside that circle, near the top...'
# Make sure no detail—like a small cloud in the corner or a shadow on the ground—is left out.
# """,

# "33":"""
# Generate a dense, granular caption for this image. Imagine you are explaining this photo to a blind artist who needs to recreate it perfectly on a canvas.
# Describe the scene from the background to the foreground. Include the exact color gradients, the textures of the surfaces (e.g., 'glossy,' 'rough and cracked'), the lighting source and shadows, the expressions on any faces, and the exact positioning of every element relative to the frame. Avoid abstract interpretations; only describe what is visually present.
# """,

# "34":"""
# Analyze this image and write a highly detailed description designed for a child to draw it exactly. Do not just summarize the scene. Instead, break it down like a paint-by-numbers or step-by-step drawing tutorial.

#     Background: Describe the colors, textures, and elements in the very back (e.g., sky, walls, horizon).

#     Layout & Placement: Where is every object located? Use precise spatial terms (e.g., 'in the bottom-left corner,' 'overlapping the tree,' 'centered horizontally').

#     Shapes & Sizes: Describe the main objects by their basic geometric shapes and relative sizes (e.g., 'a large, oval-shaped rock twice the size of the bucket next to it').

#     Colors & Lighting: Specify the exact shades (e.g., 'bright lime green,' not just 'green') and where the light/shadows fall.
#     Keep the language clear and concrete so a child can easily visualize and replicate it.
# """,

# "35":"""
# Generate a dense, granular caption for this image. Imagine you are explaining this photo to a blind artist who needs to recreate it perfectly on a canvas.
# Describe the scene from the background to the foreground. Include the exact color gradients, the textures of the surfaces (e.g., 'glossy,' 'rough and cracked'), the lighting source and shadows, the expressions on any faces, and the exact positioning of every element relative to the frame. Avoid abstract interpretations; only describe what is visually present.
# """,

# "36":"""
# Analyze this image and write an incredibly granular, detailed description so that a child could draw it exactly. You must prioritize the main character above all else so they are not skipped or glossed over.

# Structure your response into these exact sections:

#     The Main Character's Anatomy & Features: Describe their exact pose, the direction they are facing, their expression, eye color, hair texture/style, and any distinct physical traits (e.g., 'sitting cross-legged, facing the right side of the page, with a wide open-mouthed smile showing two top teeth').

#     The Main Character's Clothing & Textures: Describe every piece of clothing, its exact colors, patterns, and how it sits on the body (e.g., 'wearing a bright red hoodie with a yellow zipper halfway down, and blue denim jeans with a small tear on the left knee').

#     The Immediate Surroundings: What is the character touching or interacting with? (e.g., 'holding a round, green apple in their right hand').

#     The Background & Spatial Layout: Describe the rest of the environment and exactly where the character is positioned within it (e.g., 'The character is centered in the lower half of the page. Behind them is...').

# Do not use vague summaries. Describe everything as literal shapes, colors, and positions.
# """,


# "37":"""
# [Task: Image Extraction]
# Extract all visual data points from the image for an exact drawing replica. 

# [Data Fields]
# - Subject Classification: [Identify precise breed/species/type]
# - Subject Primary Color: [Exact shade]
# - Subject Secondary Markings: [Location, shape, and color of spots/patterns]
# - Subject Anatomical Details: [Eyes, ears, snout, tail, limb position]
# - Subject Clothing/Texture: [Fabric type, fur length, exact colors]
# - Spatial Coordinates: [Exact grid location of subject]
# - Background Elements: [Everything behind the subject, described by shape and color]

# Fill out every field with literal data. Do not write full prose sentences if bullet points are more accurate.
# """,




# "38":"""
# Write a step-by-step drawing instruction guide for a child to recreate this image exactly. 

# Step 1: The Main Character's Identity. State the exact breed or specific type of character.
# Step 2: Drawing the Character's Head. Describe the exact shapes, eye details, expressions, and markings.
# Step 3: Drawing the Character's Body. Describe the exact pose, limbs, fur texture, or clothing details. Do not skip any features.
# Step 4: Drawing the Environment. Describe the colors, textures, and placement of the background elements surrounding the character.

# Be highly descriptive. Avoid abstract words like "beautiful" or "cute"; use concrete shapes and color names instead.
# """,




# "39":"""
# Deconstruct the main character in this image into a literal drawing guide. Fill out every section completely:

# [Subject Type] -> Specify the exact breed, age, or species.
# [Head Deconstruction] -> Describe the shape, eyes, ears, hair/fur patterns, and exact facial expression.
# [Body & Attire Deconstruction] -> Describe the torso, limbs, clothing materials, collars, harnesses, logos, or fur gradients.
# [Physical Action] -> Explain the exact weight distribution and posture (e.g., leaning left, sitting on haunches, paws pressed together).
# [Environment] -> Describe the colors and items in the immediate foreground and background.
# """,




# "40":"""
# Identify the main animal in this image and provide a hyper-detailed drawing blueprint for a child to replicate it perfectly. You must follow this structure exactly:

# <breed_classification>
# Identify the exact breed or species. List 3 distinct physical markers that prove it is this breed (e.g., ear shape, snout length, coat pattern).
# </breed_classification>

# <character_anatomy>
# - Head & Face: Describe eye color, shape, gaze direction, nose/snout color, and exact ear positioning.
# - Coat & Texture: Describe the exact fur texture (e.g., fluffy, wiry, short-haired) and the precise distribution of colors/spots.
# - Body Pose: Describe the exact mechanical position of all four limbs and the tail.
# </character_anatomy>

# <background_layout>
# Describe the background objects and floor texture strictly in relation to where the animal is sitting/standing.
# </background_layout>
# """,




# "41":"""
# Act as a deterministic image parsing engine. Divide this image into a 3x3 grid (Top/Middle/Bottom x Left/Center/Right). Provide a strict visual description:

# 1. MAIN CHARACTER IDENTIFICATION: State the exact breed, species, or distinct character type.
# 2. GRID LOCATION: Specify exactly which grid zones the main character occupies.
# 3. CHARACTER MICRO-DETAILS: Describe the character's exact facial features, clothing/fur textures, and body posture in absolute detail. Do not skip any physical traits.
# 4. SURROUNDINGS: Describe the objects directly touching or adjacent to the main character.

# Do not use summary phrases. Be literal and descriptive.
# """,


# "42":"""
#  You are an expert image captioning and visual scene analysis model. Your task is to generate an extremely detailed, objective, and accurate caption of the provided image. The description should be so complete that a skilled artist could recreate the image as closely as possible without seeing the original.

# Follow these instructions carefully:

# Write the output as a single continuous paragraph of at least 10–20 detailed sentences (do not use bullet points).
# Describe only what is visually observable. Do not invent or assume facts that are not supported by the image.
# Start with an overview of the entire scene before describing individual elements.
# Describe the main subject(s) in exhaustive detail, including:
# Species (if animal), breed (if confidently identifiable), or state "breed unknown" if uncertain.
# Apparent size and proportions.
# Colors and color patterns.
# Fur, feathers, skin, scales, or texture.
# Facial features.
# Eyes (shape, color if visible, direction of gaze).
# Nose, ears, mouth, whiskers, horns, tail, paws, claws, etc.
# Pose, posture, body orientation.
# Expression and body language.
# Clothing, accessories, collars, tags, jewelry, or equipment.
# Visible markings, scars, spots, stripes, or unique identifiers.
# Describe every object in the scene, including:
# Position relative to the main subject.
# Shape, size, material, texture, and color.
# Condition (new, old, worn, damaged, dirty, polished, etc.).
# Describe the entire background thoroughly:
# Indoor or outdoor environment.
# Architecture or landscape.
# Trees, plants, grass, flowers, sky, clouds, mountains, roads, buildings, furniture, vehicles, water, or other visible elements.
# Distances and spatial relationships between objects.
# Describe the lighting in detail:
# Natural or artificial.
# Direction of light.
# Intensity.
# Warm or cool tones.
# Shadows.
# Highlights.
# Reflections.
# Time of day if visually evident.
# Describe the image composition:
# Camera angle.
# Perspective.
# Framing.
# Subject placement.
# Foreground, middle ground, and background.
# Depth of field.
# Focus and blur.
# Describe colors comprehensively:
# Dominant colors.
# Accent colors.
# Color harmony and contrast.
# Saturation and brightness.
# Describe textures throughout the image:
# Smooth, rough, glossy, matte, fluffy, metallic, wooden, fabric, stone, etc.
# Describe any visible actions or interactions occurring in the scene.
# If people are visible, describe only observable characteristics, such as:
# Approximate age group (child, teenager, young adult, middle-aged, older adult).
# Apparent gender presentation (if visually evident; otherwise say "gender unclear").
# Clothing.
# Hairstyle.
# Facial hair.
# Facial expression.
# Pose.
# Body orientation.
# Actions.
# Relative position in the scene.
# Do NOT infer or guess sensitive attributes such as nationality, ethnicity, race, religion, occupation, income, political views, or personal identity. If these cannot be directly observed, do not mention them.
# If something is partially hidden, clearly state that it is partially occluded rather than guessing the missing details.
# Distinguish between certainty and uncertainty using phrases like "appears to be," "likely," or "not clearly visible" when appropriate.
# Mention any visible text, logos, signs, labels, or watermarks exactly as they appear if readable.
# Mention image quality aspects such as sharpness, noise, compression artifacts, motion blur, or low resolution if present.
# Describe the overall atmosphere or mood based only on visual cues, without inventing a story.
# Finish with a concise summary that captures the complete visual impression of the scene.

# Important: Accuracy is more important than creativity. Never hallucinate details. If a detail cannot be confidently determined from the image, explicitly state that it is unclear rather than guessing. The final output should read like a professional forensic visual description rather than a short caption, providing enough detail for an artist to faithfully recreate the image.
#  """,
# "43":"""
# Describe this image in a single detailed paragraph. Include the main subject's appearance (color, size, texture), its pose or action, the background/setting, lighting conditions, and the overall style (photo, illustration, 3D render, etc.). Be specific and objective — avoid vague or subjective words.
# """,
# "44":"""
# Write one concise sentence (15-20 words) that captures the key visual content of this image: subject, action, and setting. Prioritize the most visually important details.
# """,
#"45":"""
#Generate a caption in this format: [subject + attributes], [action/pose], [setting/background], [lighting], [style]. Separate each part with a comma. Be precise and avoid repetition.
#""",
# "46":"""
# Describe this image focusing on spatial layout — what is in the foreground, midground, and background, how objects are positioned relative to each other, and the camera angle or framing (close-up, wide shot, top-down, etc.).
# """,
"47":"""
Write an objective, factual description of exactly what is visible in this image, as if for accessibility alt-text. State colors, counts, and positions precisely. Do not add interpretation, emotion, or assumptions about what isn't directly visible.
""",





}



# You are an expert image captioning assistant.

# Analyze this image carefully and provide a highly detailed description.

# Include:

# - Main subject and appearance
# - All visible objects
# - Colors, textures, and patterns
# - Actions and interactions
# - Foreground and background
# - Environment and lighting
# - Spatial relationships between objects
# - Important visual details

# Only describe what is visible.
# Do not guess or add imaginary details.

# Write a detailed paragraph.


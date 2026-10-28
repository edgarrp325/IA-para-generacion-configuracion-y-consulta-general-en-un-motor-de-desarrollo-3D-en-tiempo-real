---
title: "Motion"
category: "General"
source_file: "AnimationRootMotionNodeOnImportedClips.html"
doc_type: "manual"
---

# Motion

Unity uses **root motion** to displace and orient the **GameObject** to displace and orient the **GameObject** at the root of the Animator hierarchy for all **Animation clips** at the root of the Animator hierarchy for all **Animation clips**. Sometimes, it is necessary to select a different node to act as the root motion source rather than the designated node.

To select a different Root Motion Node for all animation clips:

  1. Expand the Motion section.

  2. Select the new root motion source from the Root Motion Node menu. This menu list all the objects and nodes under the root of the imported file’s hierarchy. This includes _None_ (designated node) and _**Root Transform**_ , your character’s **mesh** , your character’s **mesh** objects, the root bone name, and a submenu for each item with child objects. Each submenu also contains the child object(s) themself and further sub-menus if those objects have child objects.

  3. Select Apply.

Traverse the hierarchy of objects to select a root motion node

When you select a different Root Motion Node, the newly selected root motion source overrides the manual root motion settings for each imported animation clip. This hides and overriddes the Root Transform Rotation, Root Transform Position (Y), and Root Transform Position (XZ) settings.
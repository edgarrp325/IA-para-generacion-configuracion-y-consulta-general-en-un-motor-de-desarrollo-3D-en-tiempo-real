---
title: "Shortcuts Manager"
category: "General"
source_file: "ShortcutsManager.html"
doc_type: "manual"
---

# Shortcuts Manager

The Shortcuts manager lets you view and manage keyboard shortcuts in Unity.

A shortcut is any key, or combination of keys, that is bound to a Unity command. A command is an action that is executed in the Editor. For example, the **R** key is bound to the command that activates the **Scale** tool in the **Scene** view.

You access the Shortcuts Manager from Unity’s main menu:

  * On Windows and Linux, select **Edit > Shortcuts**.
  * On macOS, select **Unity > Shortcuts**.

The Shortcuts Manager  
---  
**A** |  **Profile drop-down menu:** Allows you to manage, and switch between, different shortcut profiles. See Shortcut Profiles for details.  
**B** |  **Key map:** Shows you which keys are assigned to commands, and the commands they are assigned to. See The key map for details. You can also use the key map to manage shortcuts.  
**C** |  **Category list:** Commands are sorted into categories, which appear in the **Category** list. When you select a category, its commands appear in the **Command** list on the right.  
**D** |  **Command** and **Shortcut list:** Lists all commands in the selected Category and their assigned shortcuts. See The Command list for details. You can also use the Command list to manage shortcuts.  
  
### Assigning shortcuts to global vs. contextual commands

Unity commands can be global or contextual.

Global commands are always available. For example, by default the command to Undo an action is assigned to the **Ctrl/Cmd + Z** shortcut. Using that shortcut always undoes the last action, regardless of which windows are open and which tools are active.

Contextual commands only work when you use a particular view or set of tools. For example, by default the square bracket keys **[** and **]** are assigned to one set of commands in the **Terrain** tool and another set in the Grid Painting tool. When you press either of those keys, Unity executes the command for whichever tool is active.

Normally, you assign a shortcut to one global command, or one or more contextual commands _from different contexts_. Other multi-command combinations (for example, two global commands, or two contextual commands _from the same context_) create conflicts that you need to manage. For information about shortcut conflicts and how to manage them, see Shortcut conflicts.

Unity also has a few special global commands that can share shortcuts with other global commands without creating conflicts. For example the **Q** , **W** , and **E** keys are assigned to the View, Move, and Rotate tools respectively, but when you activate **Flythrough** mode, you use these keys to move down, forward, and up.

### The key map

This section explains how to use the key map to view shortcut assignments. For information on using the key map to add, remove, and modify shortcuts, see Managing shortcuts.

The key map shows you which keys and key combinations are assigned to commands.  
  
---  
| Pink keys are assigned to global commands.  
| Blue keys are assigned to contextual commands.  
| White keys are not assigned to any commands.  
| Grey keys are special keys that cannot be assigned to commands.  
  
For example, modifier keys such as **Shift** and **Ctrl/Cmd** , or utility keys such as **Return** and **Esc**.  
  
Selecting modifier keys such as **Shift** , **Ctrl/Cmd** , and **Alt** updates the key map to show which combinations of shortcuts and modifiers are assigned to commands. Active modifier keys turn blue in the key map.

Activating modifier keys changes the key map to show how key combinations are assigned

**Tip:** To temporarily activate modifier keys in the key map, hold them down on your keyboard.

To see which commands a particular key is assigned to, hover your mouse pointer over a shortcut key. The tooltip lists the commands the key is assigned to.

The **A** key is assigned to the 3D Viewport’s Fly Mode Left command.

For key combinations, activate the modifier keys by holding them down on your keyboard, or clicking them on the key map, and then hover your mouse pointer over a shortcut key.

The **Ctrl/Cmd + A** key combination is assigned to the **Edit > Select All** command

You can assign a single shortcut to more than one command. As long as Unity can’t execute the commands at the same time, the shortcut works transparently. However, if you map a shortcut to multiple commands that can be executed at the same time, you create a conflict. To find out about conflicts and how to manage them, see Shortcut conflicts below.

### The Command list

This section explains how to use the **Command** list to view shortcut assignments. For information about using the **Command** list to add, remove, and modify shortcuts, see Managing shortcuts.

The **Command** list shows you which shortcuts are assigned to specific commands. Choose a category from the **Category** list to display its commands and shortcuts in the **Command** list.

You can also search the **Command** list using the search box. As you type a search term, the **Command** list automatically narrows its scope to commands that match the search term.

If you search a specific category, you can switch between results in the selected category and results in the **All Unity Commands** category by setting the scope in the **Search** row.

## Managing shortcuts

The Shortcuts Manager provides several ways of assigning, modifying, unassigning, and resetting shortcuts.

You assign or modify shortcuts by doing one of the following:

  * Dragging and dropping commands from the Command list onto the key map.

  * Typing shortcuts in the Command list.

You unassign or reset shortcuts by doing one of the following:

  * Using the context menus in the key map or the Command list.

  * Deleting shortcut assignments directly in the Command list.

### Assigning shortcuts to commands

You assign shortcuts to commands using the key map or the **Command** list.

**To assign a shortcut using the key map:**

  1. Click any modifier keys you want to include in the shortcut (for example, **Shift** or **Ctrl/Cmd**).

  2. Drag and drop the command from the **Command** list onto the main shortcut key.  
  
As you hover over the key map, the cursor changes to indicate which assignments are possible.  
  

**To assign a shortcut from the Command list:**

  1. Double-click the command in the list to edit its shortcut field.

  2. With the cursor in the shortcut field, press the keys for the shortcut on your keyboard, as you would normally.  
  
  
Make sure you hold down any modifier keys you want to include in the shortcut (**Shift** or **Alt/Option** , for example).

If the shortcut is already assigned to a command, the new assignment creates a conflict. For information about managing conflicts, see Shortcut conflicts.

### Unassigning and resetting shortcuts

Use the key map or the **Command** list to remove a command’s assigned shortcut or reset a modified shortcut to its default mapping.

**Note:** Unity stores default shortcut assignments in the Default profile. See Shortcut Profiles for details.

**To unassign or reset a shortcut from the key map:**

  1. Right-click the shortcut key you want to unassign or reset.  
  
If you are unassigning/resetting a key combination, click any included modifier keys (**Shift** or **Ctrl/Cmd** , for example) before right-clicking the shortcut key.

  2. From the context menu:

     * Select **[COMMAND] > Reset to default** to re-assign the default shortcut to the command.

     * Select **[COMMAND] > Remove shortcut** to unassign the shortcut from the command.

**To unassign or reset a shortcut from the Command list:**

  1. Right-click the command of the shortcut you want to unassign or reset.

  2. From the context menu:

     * Choose **[COMMAND] > Reset to default** to re-assign the default shortcut to the command.
     * Choose **[COMMAND] > Remove shortcut** to unassign the shortcut from the command.

Alternatively:

  * Double-click a command of the shortcut you want to unassign, and press the **Return/Enter** key to delete the shortcut from the shortcut field.

## Shortcut conflicts

You can assign the same shortcut to more than one command, provided the commands cannot be executed at the same time. For example, a single shortcut might be assigned to a command in the **Scene view** and another command in the Animation window. Because the two windows cannot have focus at the same time, there’s no ambiguity about which command Unity executes when you use the shortcut.

Assigning a shortcut to two commands that _can_ be executed at the same time creates a conflict. For example, you create a conflict when you assign a single shortcut to:

  * One or more contextual commands _from the same context_.

  * More than one global command.

  * A combination of global and contextual commands.

The Shortcuts manager gives you options for handling conflicts when you create new shortcut assignments, and when you use a shortcut that is assigned to conflicting commands.

### Viewing conflicts in the Shortcuts Manager

Commands with shortcut conflicts appear with a “caution” icon in the **Command** list.

You can get a complete list of commands with conflicting shortcuts by selecting the **Binding Conflicts** category in the **Category** list.

### Managing conflicts when creating shortcuts

Assigning a shortcut to two conflicting commands opens the **Binding conflict** dialog.

  * Choose **Create Conflict** to assign the shortcut to the command, in addition to any existing command assignments.  
  
Unity adds all of the shortcut’s assigned commands to the shortcut to the **Binding Conflicts** category.

  * Choose **Reassign** to reassign the shortcut to the conflicting command. This clears any other command assignments.

  * Choose **Cancel** to exit without taking any action.

### Managing conflicts when using shortcuts

When you’re working in Unity, using a shortcut that is assigned to conflicting commands opens the Shortcut Conflict dialog.

  * Choose a command from the list and click the **Perform Selected** button to execute the command.  
  
Enable the **Rebind to selected command** option before executing the command to clear any other assignments so that the shortcut is assigned to the selected command only. This is equivalent to deleting the other assignments.

  * Choose **Resolve Conflict** to open the Shortcuts Manager, where you can modify the shortcuts to eliminate the conflict.

  * Choose **Cancel** to exit without taking any action.

## Shortcut profiles

Shortcuts are stored in profiles. Each profile is a complete set of Unity shortcuts that you can modify to suit your needs. You can create as many profiles as you like, and switch between them as needed. You can add, remove, or modify shortcuts in any active profile except the Default profile (see below). Changes to the active profile are immediate. Unity saves them automatically, and does not prompt you to accept or reject them.

Unity stores Shortcut profiles outside of the Project, in the Unity preferences directory:

  * On Windows: `%APPDATA%/Unity\Editor-5.x\Preferences\shortcuts`

  * On macOS: `~/Library/Preferences/Unity/Editor-5.x/shortcuts`

  * On Linux: `~/.config/unity3d/Preferences/Editor-5.x/shortcuts`

This means any profiles you create are available in all of your Projects.

**Upgrading:** When you upgrade from an older version of Unity, Unity migrates any shortcuts you had configured in the Preferences to a new shortcut profile called UserProfile.

### Managing shortcut profiles

You manage profiles from the profile drop-down menu at the top of the Shortcuts Manager:  
  
---  
**A** |  **Profile list:** Lists all available profiles. Choose one to make it the active profile  
**B** |  **Profile options:** Options for creating a new profile or renaming or deleting the active profile.  
  
#### Default shortcut profile

Unity has a Default profile with the “factory” shortcut settings. When you create a new profile, Unity copies the Default profile.

You cannot modify the Default profile. If you try to modify it, Unity automatically creates a copy (called _Default copy_), makes the copy the active profile, and applies your change to that copy.

## Bypassing the Shortcuts Manager for custom tools

When you select a key or key combination on your keyboard, Unity generates a keyboard event and sends that event to the active view. If the active view can use the event, for example to trigger an action, it does so. If not, the event is sent to the Shortcuts Manager, and Unity executes the command that the shortcut is assigned to.

When developing custom tools, you can intercept keyboard events programmatically before they reach the Shortcuts Manager. For example, you might want a custom tool to react to a key press in a more complex way than you can configure using the Shortcuts Manager.

How you intercept keyboard events depends on the system you use to create the interface for your custom tools.

If you are using the IMGUI system, see the following Scripting Reference topics:

  * Event.current

If you are using the UI Elements system, see the following Scripting Reference topics:

  * KeyDownEvent

  * CallbackEventHandler.RegisterCallback

  * CallbackEventHandler.HandleEvent

## User-defined shortcuts

As well as modifying shortcuts from the Shortcuts Manager, you can use the classes in the UnityEditor.ShortcutManagement namespace to define custom shortcuts in other places, such as **scripts** and packages. For example, you use the ShortcutAttribute and ClutchShortcutAttribute attributes to create new shortcuts.

When Unity loads the commands and shortcuts from another source, it:

  * Adds any new commands in the main menu to the **All Unity Commands** category in the **Command** list, so you can then use the Shortcuts Manager to create shortcuts for them.

  * Adds custom command categories to the **Category** list.

  * Adds custom keyboard shortcuts to the shortcuts database, so they appear in all shortcut profiles.

  * Shows any conflicts between the custom shortcuts and shortcuts in the current profile in the **Shortcut Conflicts** category in the **Command** list.
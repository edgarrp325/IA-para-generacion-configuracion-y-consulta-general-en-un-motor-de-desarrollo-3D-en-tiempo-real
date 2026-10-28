---
title: "Handle events"
category: "General"
source_file: "UIE-Events-Handling.html"
doc_type: "manual"
---

# Handle events

Events in **UI** Toolkit are similar to HTML events. When an event occurs, it’s sent to the target **visual element** Toolkit are similar to HTML events. When an event occurs, it’s sent to the target **visual element** and to all elements within the propagation path in the visual element tree.

The event handling sequence is as follows:

  1. Execute event callbacks on elements from the root element down to the parent of the event target. This is the **trickle-down phase** of the dispatch process.
  2. Execute event callbacks on the event target. This is the **target phase** of the dispatch process.
  3. Call `ExecuteDefaultActionAtTarget()` on the event target.
  4. Execute event callbacks on elements from the event target parent up to the root. This is the **bubble-up phase** of the dispatch process.
  5. Call `ExecuteDefaultAction()` on the event target.

As an event moves along the propagation path, the `Event.currentTarget` property updates to the element currently handling the event. Within an event callback function:

  * `Event.currentTarget` is the visual element that the callback registers on.
  * `Event.target` is the visual element where the original event occurs.

For more information, see Dispatching events.

## Register an event callback

You can register an event callback to customize the behavior of an individual instance of an existing class, such as reacting to a mouse click on a text label.

Each element along the propagation path (except the target) can receive an event twice:

  * Once during the trickle-down phase.
  * Once during the bubble-up phase.

By default, a registered callback executes during the target phase and the bubble-up phase. This default behavior ensures that a parent element reacts after its child element. 

On the other hand, if you want a parent element to react before its child, register your callback with the `TrickleDown.TrickleDown` option:
    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    ...
    VisualElement myElement = new VisualElement();
    
    // Register a callback for the trickle-down phase.
    myElement.RegisterCallback<MouseDownEvent>(MyCallback, TrickleDown.TrickleDown);
    ...
    

This informs the dispatcher to execute the callback at the target phase and the trickle-down phase.

To add a custom behavior to a specific visual element, register an event callback on that element. 

The following example registers a callback for the `MouseDownEvent`:
    
    
    // Register a callback on a mouse down event
    myElement.RegisterCallback<MouseDownEvent>(MyCallback);
    

The signature for the callback function looks like this:
    
    
    void MyCallback(MouseDownEvent evt) { /* ... */ }
    

You can register multiple callbacks for an event. However, you can only register the same callback function on the same event and propagation phase once. 

To remove a callback from a `VisualElement`, call the `myElement.UnregisterCallback()` method.

## Send custom data to an event callback

You can send custom data along with the callback to an event. To attach custom data, you must extend the call to register the callback.

The following example registers a callback for the `MouseDownEvent` and sends custom data to the callback function:
    
    
    // Send user data along to the callback
    myElement.RegisterCallback<MouseDownEvent, MyType>(MyCallbackWithData, myData);
    

The signature for the callback function looks like this:
    
    
    void MyCallbackWithData(MouseDownEvent evt, MyType data) { /* ... */ }
    

## Listen to value changes

UI controls can use the `value` property to hold data for their internal state. For example:

  * A `Toggle` holds a Boolean value that changes when the `Toggle` is turned on or off.
  * An `IntegerField` holds an integer that holds the field’s value.

You can get the value of the control by the following:

  * Get the value from the control directly: `int val = myIntegerField.value;`.

  * Listen to a `ChangeEvent` sent by the control and process the change when it happens. You must register your callback to the event like this:
        
        //RegisterValueChangedCallback is a shortcut for RegisterCallback<ChangeEvent>. 
        //It constrains the right type of T for any VisualElement that implements an 
        //INotifyValueChange interface.
        myIntegerField.RegisterValueChangedCallback(OnIntegerFieldChange); 
        

The signature for the callback function looks like this:
        
        void OnIntegerFieldChange(ChangeEvent<int> evt) { /* ... */ }
        

You can change the value of a control by the following:

  * Directly change the `value` variable: `myControl.value = myNewValue;`. This will trigger a new `ChangeEvent`.
  * Use `myControl.SetValueWithoutNotify(myNewValue);`. This won’t trigger a new `ChangeEvent`.

For more information, see Change events

## Capture the pointer

When you handle pointer input, you might want the control to capture a pointer. When a visual element captures a pointer, Unity sends all the events associated with the pointer to the visual element regardless of whether the pointer hovers over the visual element. For example, if you create a control that receives drag events and captures the pointer, the control still receives drag events regardless of the pointer location.

To capture a pointer, use capture events. See Create a drag-and-drop UI inside a custom Editor window for an example.

## Respond to events with custom controls

If you’re implementing custom controls, you can respond to UI Toolkit events in two ways:

  * Registering an event callback.
  * Implementing a default action.

How you choose to respond to events depends on the situation.

The differences between callbacks and default actions are:

  * Callbacks must register on instances of the class. Default actions run as virtual functions on the class.
  * Callbacks execute for all visual elements in the propagation path. Default actions run only for the event target.
  * Callbacks might perform additional checks to determine whether they should react to an event. For example, a callback handling a mouse click might check if the element is the target of the event. Default actions can skip this step.
  * Default actions have a slight performance advantage because they don’t require a lookup in the callback registry during the propagation phase.

### Implement a default action

A default action applies to all instances of the class. A class that implements default actions can also have callbacks registered on its instances.

When a class implements a default action, it must derive a new subclass of `VisualElement` and implement either the `ExecuteDefaultActionAtTarget()` method, the `ExecuteDefaultAction()` method, or both.

Default actions execute on each instance of a visual element sub-class when that instance receives an event. To customize default actions, you can override `ExecuteDefaultActionAtTarget()` and `ExecuteDefaultAction()`, as shown in the example below:
    
    
    override void ExecuteDefaultActionAtTarget(EventBase evt)
    {
        // Call the base function.
        base.ExecuteDefaultActionAtTarget(evt);
    
        if (evt.eventTypeId == MouseDownEvent.TypeId())
        {
            // ...
        }
        else if (evt.eventTypeId == MouseUpEvent.TypeId())
        {
            // ...
        }
        // More event types
    }
    

Implementing your default actions in `ExecuteDefaultAction()` allows you to stop or prevent the execution of a default action.

If you want the target default action to execute before its parent callback, implement the default actions in `ExecuteDefaultActionAtTarget()`.

You should view default actions as the behaviors that an element type should have when it receives an event. For example, a checkbox should toggle its state in response to a click event. To execute this, you can override a default action virtual function, instead of registering callbacks on all checkboxes.

## Best practices for custom controls

The following are best practices for custom controls.

### Implement behaviors

You should implement behaviors from your element with default actions. You can call `PreventDefault()` in a callback attached to an instance to cancel default element behaviors.

Additional benefits of implementing behaviors as default actions are:

  * Default actions don’t require a lookup in the callback registry.
  * Instances without callbacks don’t enter the propagation process.

For greater flexibility, you can execute default actions of the event target at two moments during the event dispatch process:

  * Between the trickle-down and the bubble-up propagation phase, immediately after execution of the target callbacks, override `ExecuteDefaultActionsAtTarget()`.
  * At the end of the event dispatch process, override `ExecuteDefaultActions()`.

### Default actions on a class

Implement your class default actions in `ExecuteDefaultActions()`, if possible. This allows more options to override the class. You can call `PreventDefault()` to override the class during the trickle-down phase or the bubble-up phase of the event propagation process.

You must stop propagation of an event during a default action if the event shouldn’t propagate to the parent element. For example, a text field receives a `KeyDownEvent` that modifies its value, such as the `Delete` key to delete content. This event must not propagate to the parent visual element. Use `ExecuteDefaultActionsAtTarget()` to implement a default action, and call `StopPropagation()` to make sure the event isn’t processed during the bubble-up phase.

Default actions only execute for an event target. For a class to react to events that target their child or parent elements, you must register a callback to receive the event either during the trickle-down or the bubble-up propagation phase. Avoid registering callbacks in your class to improve performance.

### Stop event propagation and cancel default actions

When handling an event inside a callback or a default action, you can stop further event propagation and the execution of default actions. For example, a parent panel could stop propagation during the trickle-down phase to prevent its children from receiving events.

You can’t prevent the execution of the `EventBase.PreDispatch()` and `EventBase.PostDispatch()` methods inside the event class itself.

The following methods affect event propagation and default actions:

  * `StopImmediatePropagation()`: Stops the event propagation process immediately, so no other callbacks execute for the event. However, the `ExecuteDefaultActionAtTarget()` and `ExecuteDefaultAction()` default actions still execute.
  * `StopPropagation()`: Stops the event propagation process after the last callback on the current element. This ensures that all callbacks execute on the current element, but no further elements react to the event. The `ExecuteDefaultActionAtTarget()` and `ExecuteDefaultAction()` default actions still execute.
  * `PreventDefault()`: Prevents the event propagation process from calling the `ExecuteDefaultActionAtTarget()` and `ExecuteDefaultAction()` default actions. `PreventDefault()` doesn’t prevent the execution of other callbacks and doesn’t affect the `ExecuteDefaultActionAtTarget()` action during the bubble-up phase.

## Additional resources

  * Synthesize and send events
  * Events reference
  * Manipulators
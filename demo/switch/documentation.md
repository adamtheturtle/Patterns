# Documentation

It is possible to add or remove classes when a user clicks on an item.
This is done by adding a `pat-switch` class along with a
`data-pat-switch` attribute to the triggering element.

    <button class="pat-switch" data-pat-switch="#status off on">Power on</button>
    <span id="status" class="off"/>

If a user clicks on the *Power on* button the `off` class will be
removed and the `on` class will be added. Note that this is similar to
the toggle pattern. This pattern only triggers once though, while the
toggle pattern toggles between two states.

This pattern takes three arguments:

-   `selector`: the CSS selector identifying the elements that must be
    updated
-   `remove`: the class that should be added
-   `add`: a class that should be removed

You must provide the selector and at least one of *remove* or *add*.

You can use wildcards to identify classes that should be removed by
using a wildcard (the `*` character) in the class name.

    <button class="pat-switch" data-pat-switch=".toolbar icon-*">Remove icons</button>

Multiple changes can be provided if desired by separating them using the
`&&` separator. The example below uses this to remove all icon classes
in both the toolbar and the navigation tree.

    <button class="pat-switch" data-pat-switch=".toolbar icon-* && .navtree; icon-*">Remove icons</button>

Javascript API
--------------

The javascript API is entirely optional since patterns already
autmoatically enables the switching behaviour for all elements with a
`data-pat-switch` attribute. Developers may be interested in using the
API to add behaviour to other elements or trigger switches manually.
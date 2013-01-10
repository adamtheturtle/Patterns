define([
    "../registry",
    "jquery_chosen"
], function(registry) {
    var _ = {
        name: "chosen",
        trigger: "select.pat-chosen",
        init: function($el) {
            $el.chosen();
            return $el;
        },

        destroy: function() {
            // XXX
        }
    };

    registry.register(_);
    return _;
});

// jshint indent: 4, browser: true, jquery: true, quotmark: double
// vim: sw=4 expandtab

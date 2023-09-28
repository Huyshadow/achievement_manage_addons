odoo.define("manage_user_depart.disappear_control_panel", function (require) {
  "use strict";

  var FormView = require("web.FormView");
  var viewRegistry = require("web.view_registry");

  var CustomFormView = FormView.extend({
    config: _.extend({}, FormView.prototype.config, {
      withControlPanel: false,
    }),
  });

  console.log("Huy");

  viewRegistry.add("disappear_control_panel", CustomFormView);
});

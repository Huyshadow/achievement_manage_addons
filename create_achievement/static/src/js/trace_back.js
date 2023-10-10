odoo.define("create_achievement.BackClientAction", function (require) {
  "use strict";

  var core = require("web.core");
  var AbstractAction = require("web.AbstractAction");

  var _t = core._t;

  var BackClientAction = AbstractAction.extend({
    start: function () {
      this._super.apply(this, arguments);
      window.history.back();
    },
  });

  core.action_registry.add(
    "create_achievement.BackClientAction",
    BackClientAction
  );

  return BackClientAction;
});

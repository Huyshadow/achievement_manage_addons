odoo.define("view_achievement_detail_user_order", function (require) {
  "use strict";

  var viewRegistry = require("web.view_registry");
  var KanbanView = require("web.KanbanView");

  var KanbanViewWithoutControlPanel = KanbanView.extend({
    config: _.extend({}, KanbanView.prototype.config, {
      withControlPanel: false,
    }),
  });

  viewRegistry.add(
    "kanban_without_control_panel",
    KanbanViewWithoutControlPanel
  );
});

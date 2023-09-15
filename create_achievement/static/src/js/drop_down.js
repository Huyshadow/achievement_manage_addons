odoo.define(
  "create_achievement.view_cr_group_criteria_form",
  function (require) {
    "use strict";

    var AbstractAction = require("web.AbstractAction");
    var core = require("web.core");
    var QWeb = core.qweb;

    var AchievementAction = AbstractAction.include({
      _onButtonClicked: function (event) {
        this._super.apply(this, arguments);
        if (event.data.attrs.options.toggle_field) {
          var fieldName = event.data.attrs.options.toggle_field;
          var fieldElement = this.renderer.$(
            '.o_field_widget[name="' + fieldName + '"]'
          );
          fieldElement.toggle();
        }
      },
    });

    core.action_registry.add("achievement_detail", AchievementAction);

    return AchievementAction;
  }
);

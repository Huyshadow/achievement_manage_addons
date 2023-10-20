odoo.define("view_submit.disappear_check_box", function (require) {
  "use strict";

  //var _ = require("underscore");
  var ListRenderer = require("web.ListRenderer");
  var ListView = require("web.ListView");
  var viewRegistry = require("web.view_registry");

  var CustomListRenderer = ListRenderer.extend({
    _renderRow: function (record) {
      var tr = this._super(record);
      console.log(record.data.small_category_name_field);
      tr.find("input[type='checkbox']").prop("disabled");
      return tr;
    },
    _disableRecordSelectors: function () {
      this.$(".o_list_record_selector input").attr("disabled", "disabled");
      this.$(".o_control_panel").attr("disabled", "disabled");
    },

    _enableRecordSelectors: function () {
      this.$(".o_list_record_selector input").attr("disabled", false);
      this.$(".o_control_panel").attr("disabled", false);
    },
  });

  var CustomListView = ListView.extend({
    config: _.extend({}, ListView.prototype.config, {
      Renderer: CustomListRenderer,
    }),
  });

  viewRegistry.add("disappear_check_box", CustomListView);

  //document.getElementsByClassName(".o_control_panel").css({ display: "none" });
});

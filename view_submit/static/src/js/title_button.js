odoo.define("view_submit.EditableListRenderer", function (require) {
  "use strict";

  var ListRenderer = require("web.ListRenderer");

  ListRenderer.include({
    _renderHeaderCell: function (node) {
      var $th = this._super.apply(this, arguments);
      if (node.tag === "button_group" && node.attrs.name === "button_group_0") {
        $th.text("Thao tác");
      }

      return $th;
    },
  });
});

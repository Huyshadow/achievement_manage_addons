odoo.define("view_submit.EditableListRenderer", function (require) {
  "use strict";

  var ListRenderer = require("web.ListRenderer");

  ListRenderer.include({
    _renderBodyCell: function (record, node, colIndex, options) {
      var $cell = this._super.apply(this, arguments);
      console.log($cell);
      console.log(node);
      if (node.tag === "button_group" && node.attrs.name === "button_group_0") {
        $cell.text("Xem danh sách nộp - Thao tác");
        console.log("HUY");
      }

      return $cell;
    },
  });
});
// Code for check sell

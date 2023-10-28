odoo.define("view_submit.redefine_achievement", function (require) {
  "use strict";

  var ListRenderer = require("web.ListRenderer");
  var ListView = require("web.ListView");
  var viewRegistry = require("web.view_registry");
  var num = 1;
  var CustomListRenderer = ListRenderer.extend({
    _renderHeader: function () {
      var $header = this._super.apply(this, arguments);
      $header.children("tr").children("th").eq(0).hide();
      var $th = $("<th>STT</th>");
      $header.children("tr").children("th").eq(1).before($th);
      return $header;
    },
    _renderFooter: function () {
      var $footer = this._super.apply(this, arguments);
      $footer.children("tr").children("td").eq(0).hide();
      var $td = $("<td></td>");
      $footer.children("tr").children("td").eq(1).before($td);
      num = 1;
      return $footer;
    },
    _renderRow: function (record) {
      var $tr = this._super(record);
      $.each($tr, function (index) {
        $(this).find("td").eq(0).hide();
        $(this)
          .find("td")
          .eq(1)
          .before("<td>" + num + "</td>");
        num++;
      });
      return $tr;
    },
  });

  var CustomListView = ListView.extend({
    config: _.extend({}, ListView.prototype.config, {
      Renderer: CustomListRenderer,
    }),
  });

  viewRegistry.add("redefine_achievement", CustomListView);
});

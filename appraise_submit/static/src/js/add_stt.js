odoo.define("appraise.add_stt", function (require) {
  "use strict";

  //var _ = require("underscore");
  var ListRenderer = require("web.ListRenderer");
  var ListView = require("web.ListView");
  var viewRegistry = require("web.view_registry");
  var num = 1;
  var CustomListRenderer = ListRenderer.extend({
    _renderHeader: function () {
      var $header = this._super.apply(this, arguments);
      var $th = $("<th>STT</th>");
      $header.children("tr").children("th").eq(0).before($th);
      return $header;
    },
    _renderFooter: function () {
      var $footer = this._super.apply(this, arguments);
      var $td = $("<td></td>");
      $footer.children("tr").children("td").eq(0).before($td);
      return $footer;
    },
    _renderRow: function (record) {
      var $tr = this._super(record);
      $.each($tr, function (index) {
        $(this)
          .find("td")
          .eq(0)
          .before("<td>" + num + "</td>");
        num++;
      });
      $tr.find("input[type='checkbox']").prop("disabled");
      return $tr;
    },
  });

  var CustomListView = ListView.extend({
    config: _.extend({}, ListView.prototype.config, {
      Renderer: CustomListRenderer,
    }),
  });

  viewRegistry.add("add_stt", CustomListView);
});

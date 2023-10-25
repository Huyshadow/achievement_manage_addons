odoo.define("web_list_view_general_buttons.Graph_Buttons", function (require) {
  "use strict";

  var core = require("web.core");
  var ListController = require("web.ListController");

  var QWeb = core.qweb;

  ListController.include({
    init: function (parent, model, renderer) {
      this.context = renderer.state.getContext();
      this._super.apply(this, arguments);
      this.headerGraphButtons = [];
      if (this.context.graph_buttons instanceof Array) {
        this.headerGraphButtons = this.context.graph_buttons;
        console.log(this.context.graph_buttons);
      }
    },

    renderButtons: function () {
      this._super.apply(this, arguments);

      if (this.headerGraphButtons.length > 0) {
        this.$graphButtons = $(
          QWeb.render("ListView.GraphButtons", {
            buttons: this.headerGraphButtons,
          })
        );
        this.$buttons.on(
          "click",
          ".o_graph_button",
          this._onClickGraphButton.bind(this)
        );
        this.$buttons.prepend(this.$graphButtons);
      }
    },

    _onClickGraphButton: function (event) {
      var el = event.target;
      var self = this;
      self
        ._rpc({
          model: $(el).attr("model"),
          method: $(el).attr("action"),
          args: [self.context.active_id],
          context: self.context,
        })
        .then(function (result) {
          self.do_action({
            type: result.type,
            res_model: result.res_model,
            name: result.name,
            view_mode: result.view_mode,
            view_type: result.view_type,
            views: [[false, "graph"]],
            target: result.target,
            res_id: result.res_id,
            context: result.context,
          });
        });
    },
  });
});

odoo.define("web_list_view_general_buttons.ListController", function (require) {
  "use strict";

  var core = require("web.core");
  var ListController = require("web.ListController");

  var QWeb = core.qweb;
  var submit = false;

  ListController.include({
    init: function (parent, model, renderer) {
      this.context = renderer.state.getContext();
      this._super.apply(this, arguments);
      this.headerGeneralButtons = [];
      if (this.context.general_buttons instanceof Array) {
        this.headerGeneralButtons = this.context.general_buttons;
      }
      submit = false;
    },

    renderButtons: function () {
      this._super.apply(this, arguments);

      if (this.headerGeneralButtons.length > 0) {
        this.$generalButtons = $(
          QWeb.render("ListView.GeneralButtons", {
            buttons: this.headerGeneralButtons,
          })
        );
        this.$buttons.on(
          "click",
          ".o_general_button",
          this._onClickGeneralButton.bind(this)
        );
        this.$buttons.prepend(this.$generalButtons);
      }
    },

    _onClickGeneralButton: function (event) {
      var el = event.target;
      var self = this;
      if (submit === false) {
        this.$(".o_general_button").text("Hủy");
        this.$(".o_general_button").removeClass("btn-primary");
        this.$(".o_general_button").addClass("huyButton");
        submit = true;
      } else {
        this.$(".o_general_button").text("Duyệt");
        this.$(".o_general_button").removeClass("huyButton");
        this.$(".o_general_button").addClass("btn-primary");
        submit = false;
      }
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
            views: [[false, "form"]],
            target: result.target,
            res_id: result.res_id,
          });
        });
    },
  });
});

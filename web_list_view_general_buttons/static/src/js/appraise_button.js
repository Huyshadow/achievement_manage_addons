odoo.define(
  "web_list_view_general_buttons.Appraise_Buttons",
  function (require) {
    "use strict";

    var core = require("web.core");
    var ListController = require("web.ListController");

    var QWeb = core.qweb;

    ListController.include({
      init: function (parent, model, renderer) {
        this.context = renderer.state.getContext();
        this._super.apply(this, arguments);
        this.headerAppraiseButtons = [];
        if (this.context.appraise_buttons instanceof Array) {
          this.headerAppraiseButtons = this.context.appraise_buttons;
        }
      },

      renderButtons: function () {
        this._super.apply(this, arguments);

        if (this.headerAppraiseButtons.length > 0) {
          this.$appraiseButtons = $(
            QWeb.render("ListView.AppraiseButtons", {
              buttons: this.headerAppraiseButtons,
            })
          );
          var rpc = require("web.rpc");
          this.$buttons.on(
            "click",
            ".o_appraise_button",
            this._onClickAppraiseButton.bind(this)
          );
          this.$buttons.prepend(this.$appraiseButtons);
        }
      },

      _onClickAppraiseButton: function (event) {
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
              views: [[false, "form"]],
              target: result.target,
              res_id: result.res_id,
              context: result.context,
            });
          });
      },
    });
  }
);
